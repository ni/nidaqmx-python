"""Check the documented NI-DAQmx API without importing driver code."""

from __future__ import annotations

import argparse
import io
import os
import posixpath
import subprocess
import sys
import tarfile
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath

import griffe
from docutils import nodes
from docutils.core import publish_doctree
from docutils.parsers.rst import Directive, directives, roles


@dataclass
class DocumentedApi:
    """Public declarations read from one snapshot's documentation sources."""

    modules: set[str] = field(default_factory=set)
    objects: dict[str, str] = field(default_factory=dict)
    members: dict[str, dict[str, bool]] = field(default_factory=dict)


def _qualified(name: str, module: str) -> str:
    return name if name == "nidaqmx" or name.startswith("nidaqmx.") else f"{module}.{name}"


class _ApiDirective(Directive):
    required_arguments = 1
    final_argument_whitespace = True
    has_content = True
    option_spec = {
        "canonical": directives.unchanged,
        "members": directives.unchanged,
        "undoc-members": directives.flag,
        "special-members": directives.unchanged,
        "inherited-members": directives.unchanged,
        "member-order": directives.unchanged,
        "show-inheritance": directives.flag,
    }

    def run(self):
        document = self.state.document
        api = document.settings.documented_api
        kind = self.name.removeprefix("py:").removeprefix("auto")
        name = self.arguments[0].partition("(")[0].strip()
        if "members" in self.options and (
            not self.name.startswith("auto") or kind not in ("module", "class")
        ):
            raise ValueError(f"Unsupported members option for {self.name}")
        if kind == "currentmodule":
            document["api_module"] = name
            return []
        if kind == "module":
            api.modules.add(name)
            document["api_module"] = name
        else:
            module = document.get("api_module", "")
            parent = document.get("api_class")
            if parent and not name.startswith("nidaqmx."):
                relative = name.removeprefix(parent[0].rsplit(".", 1)[-1] + ".")
                published = f"{parent[0]}.{relative}"
                target = f"{parent[1]}.{relative}"
            else:
                published = _qualified(name, module)
                target = published
            target = self.options.get("canonical", target)
            if not published.startswith("nidaqmx.") or not target.startswith("nidaqmx."):
                raise ValueError(f"API declaration needs an NI-DAQmx module context: {name}")
            if published in api.objects and api.objects[published] != target:
                raise ValueError(f"Conflicting documented targets for {published}")
            api.objects[published] = target
            if kind == "class":
                document["api_class"] = (published, target)
        if "members" in self.options:
            selection = self.options["members"]
            if selection:
                owner = name if kind == "module" else published
                members = api.members.setdefault(owner, {})
                for member in (part.strip() for part in selection.split(",")):
                    if not member.isidentifier():
                        raise ValueError(f"Unsupported explicit member selection: {member!r}")
                    members[member] = members.get(member, False) or "undoc-members" in self.options
        container = nodes.container()
        self.state.nested_parse(self.content, self.content_offset, container)
        if kind == "class":
            if parent is None:
                del document["api_class"]
            else:
                document["api_class"] = parent
        return [container]


class _NavigationDirective(Directive):
    has_content = True
    option_spec = {"maxdepth": directives.nonnegative_int, "caption": directives.unchanged}

    def run(self):
        return []


class _IncludeDirective(Directive):
    required_arguments = 1

    def run(self):
        source = self.state.document["source"]
        target = posixpath.normpath(str(PurePosixPath(source).parent / self.arguments[0]))
        if target not in self.state.document.settings.api_sources:
            raise ValueError(f"Included documentation source is unavailable: {target}")
        return []


def _reference_role(name, rawtext, text, lineno, inliner, options=None, content=None):
    return [nodes.inline(rawtext, text)], []


def documented_api(sources: dict[str, str]) -> DocumentedApi:
    """Parse source RST declarations; included RST files are parsed separately."""
    for name in (
        "automodule",
        "autoclass",
        "autofunction",
        "automethod",
        "autoattribute",
        "autodata",
        "py:module",
        "py:currentmodule",
        "py:class",
        "py:function",
        "py:method",
        "py:attribute",
        "py:data",
    ):
        directives.register_directive(name, _ApiDirective)
    directives.register_directive("toctree", _NavigationDirective)
    directives.register_directive("include", _IncludeDirective)
    for name in (
        "class",
        "func",
        "meth",
        "mod",
        "attr",
        "data",
        "const",
        "exc",
        "obj",
        "term",
        "ref",
        "doc",
        "py:class",
        "py:func",
        "py:meth",
        "py:mod",
        "py:attr",
        "py:data",
        "py:const",
        "py:exc",
        "py:obj",
    ):
        roles.register_local_role(name, _reference_role)
    api = DocumentedApi()
    for source, text in sorted(sources.items()):
        document = publish_doctree(
            text,
            source_path=source,
            settings_overrides={
                "documented_api": api,
                "api_sources": sources,
                "file_insertion_enabled": False,
                "raw_enabled": False,
                "halt_level": 6,
                "report_level": 5,
                "warning_stream": io.StringIO(),
            },
        )
        errors = [
            message.astext()
            for message in document.findall(nodes.system_message)
            if message["level"] >= 3
        ]
        if errors:
            raise ValueError("Invalid documentation source:\n" + "\n".join(errors))
    return api


def documentation_sources(base: str | None = None) -> dict[str, str]:
    """Read source RST without building docs or extracting a Git archive."""
    if base is None:
        sources = {
            path.as_posix(): path.read_text(encoding="utf-8")
            for path in Path("docs").rglob("*.rst")
            if "_build" not in path.parts
        }
        sources["README.rst"] = Path("README.rst").read_text(encoding="utf-8")
        return sources
    archive = subprocess.check_output(["git", "archive", base, "docs", "README.rst"])
    with tarfile.open(fileobj=io.BytesIO(archive), mode="r:") as contents:
        sources = {}
        for entry in contents:
            if (
                entry.isfile()
                and entry.name.endswith(".rst")
                and "_build" not in PurePosixPath(entry.name).parts
            ):
                source = contents.extractfile(entry)
                if source is None:
                    raise ValueError(f"Cannot read documentation source {entry.name}")
                sources[entry.name] = source.read().decode("utf-8")
        return sources


def _member(root, path, seen=None, expose=False):
    if path != root.path and not path.startswith(root.path + "."):
        raise ValueError(f"Documented target is outside {root.path}: {path}")
    current = root
    for part in path.split(".")[1:]:
        current = _internal_target(root, current, seen)
        if current is None:
            return None
        try:
            current = current.members[part]
        except KeyError as error:
            raise ValueError(f"Unresolved API target: {path}") from error
        if expose:
            current.public = True
    return current


def _internal_target(root, current, seen=None):
    if current is None:
        return None
    seen = set() if seen is None else set(seen)
    while current.is_alias:
        if not current.target_path.startswith(root.path + "."):
            return None
        if current.path in seen:
            raise ValueError(f"Cyclic API alias: {current.path}")
        seen.add(current.path)
        current = _member(root, current.target_path, seen)
        if current is None:
            return None
    return current


def _public_modules(module):
    if module.is_public:
        yield module
        for member in module.members.values():
            if isinstance(member, griffe.Module):
                yield from _public_modules(member)


def _required_target(root, member):
    target = _internal_target(root, member)
    if target is None:
        path = member.path if member is not None else "unresolved member"
        raise ValueError(f"Cannot safely resolve documented/public external API target: {path}")
    return target


def expose_documented_api(root, api: DocumentedApi) -> None:
    """Apply documentation visibility to one model without changing Python exports."""
    if not isinstance(root, griffe.Module):
        raise TypeError("Expected a Griffe package module")
    targets = set()
    for path in sorted(api.modules):
        module = _internal_target(root, _member(root, path, expose=True))
        if not isinstance(module, griffe.Module):
            raise ValueError(f"Documented module is unresolved or not a module: {path}")
        for member in module.members.values():
            if member.is_public:
                required = member.public is True or member.name in (module.exports or ())
                target = (
                    _required_target(root, member) if required else _internal_target(root, member)
                )
                if target is not None:
                    targets.add(target.path)
    for published, canonical in sorted(api.objects.items()):
        target = _required_target(root, _member(root, canonical, expose=True))
        alias = _required_target(root, _member(root, published, expose=True))
        if alias.path != target.path:
            raise ValueError(f"Documented alias does not resolve to {canonical}: {published}")
        targets.add(target.path)
    for owner, selections in sorted(api.members.items()):
        for name, include_undocumented in sorted(selections.items()):
            path = f"{owner}.{name}"
            target = _required_target(root, _member(root, path))
            has_docstring = target.docstring is not None and bool(target.docstring.value.strip())
            if include_undocumented or has_docstring:
                _member(root, path, expose=True)
                targets.add(target.path)
    for module in _public_modules(root):
        facade = isinstance(module.filepath, Path) and module.filepath.name == "__init__.py"
        for name, member in module.members.items():
            if member.is_alias and (member.is_public or (facade and not name.startswith("_"))):
                required = member.public is True or name in (module.exports or ())
                target = (
                    _required_target(root, member) if required else _internal_target(root, member)
                )
                if facade and target is not None and target.path in targets:
                    member.public = True


def resolve_baseline(base: str) -> tuple[str, str]:
    """Resolve the configured reference or Griffe's default newest tag."""
    if not base:
        tags = subprocess.check_output(
            ["git", "tag", "--sort=-creatordate"], text=True
        ).splitlines()
        if not tags:
            raise RuntimeError("No release tag; specify the base input.")
        base = tags[0]
    sha = subprocess.check_output(
        ["git", "rev-parse", "--verify", "--end-of-options", f"{base}^{{commit}}"], text=True
    ).strip()
    return base, sha


def check(base: str = "", approved: bool = False) -> int:
    """Compare the root once; only confirmed findings can be approved."""
    reference, sha = resolve_baseline(base)
    print(f"Checking against {reference} ({sha})", flush=True)
    old = griffe.load_git(
        "nidaqmx",
        ref=sha,
        search_paths=["generated"],
        allow_inspection=False,
        resolve_aliases=True,
        resolve_external=False,
    )
    new = griffe.load(
        "nidaqmx",
        search_paths=["generated"],
        allow_inspection=False,
        resolve_aliases=True,
        resolve_external=False,
        store_source=False,
    )
    expose_documented_api(old, documented_api(documentation_sources(sha)))
    expose_documented_api(new, documented_api(documentation_sources()))
    has_breakages = False
    for breakage in griffe.find_breaking_changes(old, new):
        message = f"{breakage.obj.path}: {breakage.explain(style=griffe.ExplanationStyle.MARKDOWN)}"
        message = message.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
        print(f"::warning::{message}")
        has_breakages = True
    if has_breakages and approved:
        print("::notice::The breaking-change label approves the compatibility findings above.")
    return int(has_breakages and not approved)


def main() -> int:
    """Run the reusable workflow's check from the repository root."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", default="", help="Git ref; default: most recently created tag")
    args = parser.parse_args()
    return check(args.base, os.environ.get("BREAKING_CHANGE_APPROVED", "false") == "true")


if __name__ == "__main__":
    sys.exit(main())
