"""Focused tests for documentation-driven API compatibility policy."""

import io
import subprocess
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

import griffe
from check_api_compatibility import (
    check,
    documented_api,
    expose_documented_api,
    resolve_baseline,
)


class DocumentationTests(unittest.TestCase):
    """Validate the supported source-documentation declaration grammar."""

    def test_source_directives_and_canonical_objects(self):
        """Canonical and nested declarations retain their public paths."""
        api = documented_api(
            {
                "docs/api.rst": """
.. automodule:: nidaqmx.system._collections.device_collection
   :members:
   :show-inheritance:

.. py:currentmodule:: nidaqmx

.. py:class:: GrpcSessionOptions(channel)
   :canonical: nidaqmx.grpc_session_options.GrpcSessionOptions

.. py:class:: SessionInitializationBehavior
   :canonical: nidaqmx.grpc_session_options.SessionInitializationBehavior

   .. py:attribute:: SessionInitializationBehavior.AUTO
"""
            }
        )
        self.assertIn("nidaqmx.system._collections.device_collection", api.modules)
        self.assertEqual(
            api.objects["nidaqmx.GrpcSessionOptions"],
            "nidaqmx.grpc_session_options.GrpcSessionOptions",
        )
        self.assertEqual(
            api.objects["nidaqmx.SessionInitializationBehavior.AUTO"],
            "nidaqmx.grpc_session_options.SessionInitializationBehavior.AUTO",
        )

    def test_literal_examples_are_not_declarations(self):
        """Examples must not silently expand the compatibility contract."""
        api = documented_api(
            {
                "docs/example.rst": """
Example::

    .. automodule:: nidaqmx.not_a_documented_module
"""
            }
        )
        self.assertEqual(api.modules, set())

    def test_included_sources_are_validated_and_parsed(self):
        """Every included source must be available in the same snapshot."""
        api = documented_api(
            {
                "docs/index.rst": ".. include:: api.rst\n",
                "docs/api.rst": ".. automodule:: nidaqmx.utils\n",
            }
        )
        self.assertEqual(api.modules, {"nidaqmx.utils"})
        with self.assertRaisesRegex(ValueError, "unavailable"):
            documented_api({"docs/index.rst": ".. include:: missing.rst\n"})

    def test_invalid_api_directive_is_fatal(self):
        """Malformed declarations must not produce partial coverage."""
        with self.assertRaisesRegex(ValueError, "Invalid documentation"):
            documented_api({"docs/api.rst": ".. automodule::\n"})

    def test_named_members_and_undoc_flag_are_retained(self):
        """An explicit list retains names and the presence of the flag."""
        api = documented_api(
            {
                "docs/api.rst": ".. automodule:: nidaqmx.task\n   :members: first, _second\n   :undoc-members:\n"
            }
        )
        self.assertEqual(api.members["nidaqmx.task"], {"first": True, "_second": True})

    def test_unsupported_selections_fail_clearly(self):
        """Invalid syntax and unsupported directive options cannot be ignored."""
        for directive, selection in (
            ("automodule", "*"),
            ("automodule", "first.child"),
            ("automodule", ","),
            ("py:module", "first"),
            ("py:currentmodule", "first"),
        ):
            with self.subTest(directive=directive, selection=selection):
                source = f".. {directive}:: nidaqmx.task\n   :members: {selection}\n"
                with self.assertRaisesRegex(ValueError, "Unsupported"):
                    documented_api({"docs/api.rst": source})


def package(collection=True, alias=True, chain=False):
    """Build synthetic package models without importing driver code."""
    root = griffe.visit("nidaqmx", Path("generated/nidaqmx/__init__.py"), "__all__ = []\n")
    modules = {
        "task": "class Task:\n    pass\n",
        "grpc_session_options": "class GrpcSessionOptions:\n    pass\n",
        "system": "__all__ = []\n",
        "system._collections": "",
        "system._collections.device_collection": (
            "class DeviceCollection:\n    @property\n    def device_names(self): return []\n"
            if collection
            else "class DeviceCollection:\n    pass\n"
        ),
    }
    for path, source in modules.items():
        current = root
        for part in path.split(".")[:-1]:
            child = current.members[part]
            assert isinstance(child, griffe.Module)
            current = child
        name = path.rsplit(".", 1)[-1]
        filepath = Path("generated/nidaqmx") / path.replace(".", "/")
        filepath = (
            filepath / "__init__.py"
            if path in ("system", "system._collections")
            else filepath.with_suffix(".py")
        )
        current.set_member(name, griffe.visit(name, filepath, source))
    if alias:
        root.set_member(
            "Task", griffe.Alias("Task", "nidaqmx.Forward" if chain else "nidaqmx.task.Task")
        )
        root.set_member(
            "GrpcSessionOptions",
            griffe.Alias("GrpcSessionOptions", "nidaqmx.grpc_session_options.GrpcSessionOptions"),
        )
    if chain:
        root.set_member("Forward", griffe.Alias("Forward", "nidaqmx.task.Task"))
    return root


API_DOCS = {
    "docs/api.rst": """
.. automodule:: nidaqmx.task
   :members:

.. automodule:: nidaqmx.system._collections.device_collection
   :members:

.. py:currentmodule:: nidaqmx

.. py:class:: GrpcSessionOptions(channel)
   :canonical: nidaqmx.grpc_session_options.GrpcSessionOptions
"""
}


class VisibilityTests(unittest.TestCase):
    """Protect documented paths across independently defined snapshots."""

    def compare(self, old, new, old_docs=API_DOCS, new_docs=API_DOCS):
        """Apply each snapshot's own documentation before a root comparison."""
        expose_documented_api(old, documented_api(old_docs))
        expose_documented_api(new, documented_api(new_docs))
        return [change.obj.path for change in griffe.find_breaking_changes(old, new)]

    def test_device_names_regression(self):
        """Private implementation paths must not hide documented properties."""
        changes = self.compare(package(), package(collection=False))
        self.assertIn(
            "nidaqmx.system._collections.device_collection.DeviceCollection.device_names", changes
        )

    def test_documented_root_aliases(self):
        """Removing a public import path must fail even if its target remains."""
        changes = self.compare(package(), package(alias=False), new_docs={})
        self.assertIn("nidaqmx.Task", changes)
        self.assertIn("nidaqmx.GrpcSessionOptions", changes)

    def test_removed_documentation_does_not_hide_breakage(self):
        """The baseline contract survives deleted candidate documentation."""
        changes = self.compare(package(), package(collection=False), new_docs={})
        self.assertIn(
            "nidaqmx.system._collections.device_collection.DeviceCollection.device_names", changes
        )

    def test_removed_documented_module(self):
        """Deleted modules remain part of the baseline comparison."""
        old, new = package(), package()
        del new.members["system"].members["_collections"].members["device_collection"]
        changes = self.compare(old, new, new_docs={})
        self.assertIn("nidaqmx.system._collections.device_collection", changes)

    def test_internal_alias_chain(self):
        """Intermediate aliases must not hide a documented public facade."""
        changes = self.compare(package(chain=True), package(alias=False), new_docs={})
        self.assertIn("nidaqmx.Task", changes)

    def test_unresolved_documented_target_is_fatal(self):
        """Missing documentation targets are not compatibility waivers."""
        with self.assertRaisesRegex(ValueError, "Unresolved API target"):
            expose_documented_api(
                package(), documented_api({"docs/api.rst": ".. automodule:: nidaqmx.missing\n"})
            )

    def test_unresolved_internal_alias_is_fatal(self):
        """Broken internal aliases must not be silently discarded."""
        root = package()
        root.set_member("Broken", griffe.Alias("Broken", "nidaqmx.missing"))
        with self.assertRaisesRegex(ValueError, "Unresolved API target"):
            expose_documented_api(root, documented_api(API_DOCS))

    def test_cyclic_alias_is_fatal(self):
        """Cyclic resolution must terminate with an operational error."""
        root = package(chain=True)
        root.set_member("Forward", griffe.Alias("Forward", "nidaqmx.Task"))
        with self.assertRaisesRegex(ValueError, "Cyclic API alias"):
            expose_documented_api(root, documented_api(API_DOCS))

    def test_external_alias_is_not_public(self):
        """External imports are not promoted into the NI-DAQmx contract."""
        root = package()
        root.set_member("version", griffe.Alias("version", "importlib.metadata.version"))
        expose_documented_api(root, documented_api(API_DOCS))
        self.assertIsNone(root.members["version"].public)

    def test_alias_chain_ending_externally_is_not_public(self):
        """Internal forwarding must not turn an external symbol into an API."""
        root = package()
        root.members["task"].set_member(
            "external", griffe.Alias("external", "__future__.annotations")
        )
        root.set_member("External", griffe.Alias("External", "nidaqmx.task.external"))
        expose_documented_api(root, documented_api(API_DOCS))
        self.assertIsNone(root.members["External"].public)

    def test_visibility_does_not_change_exports(self):
        """Analysis metadata must not redefine the package's Python exports."""
        root = package()
        exports = list(root.exports)
        expose_documented_api(root, documented_api(API_DOCS))
        self.assertEqual(root.exports, exports)

    def test_documentation_removal_alone_is_not_breaking(self):
        """Visibility metadata changes alone do not remove an existing API."""
        self.assertEqual(self.compare(package(), package(), new_docs={}), [])

    def test_canonical_target_mismatch_is_fatal(self):
        """A canonical declaration must identify the actual alias target."""
        api = documented_api(
            {
                "docs/api.rst": """
.. py:currentmodule:: nidaqmx

.. py:class:: GrpcSessionOptions
   :canonical: nidaqmx.task.Task
"""
            }
        )
        with self.assertRaisesRegex(ValueError, "does not resolve"):
            expose_documented_api(package(), api)

    def test_explicit_private_member_survives_deleted_documentation(self):
        """A selected undocumented member remains in the baseline contract."""
        old, new = package(), package()
        old.members["task"].set_member("_selected", griffe.Function("_selected"))
        docs = {
            "docs/api.rst": ".. automodule:: nidaqmx.task\n   :members: _selected\n   :undoc-members:\n"
        }
        self.assertIn("nidaqmx.task._selected", self.compare(old, new, old_docs=docs, new_docs={}))

    def test_missing_explicit_selection_is_fatal(self):
        """A selected name must resolve even when it has no documentation."""
        docs = {
            "docs/api.rst": ".. automodule:: nidaqmx.task\n   :members: missing\n   :undoc-members:\n"
        }
        with self.assertRaisesRegex(ValueError, "Unresolved API target"):
            expose_documented_api(package(), documented_api(docs))

    def test_publicly_exported_external_alias_is_fatal(self):
        """Public exports cannot silently disappear at an external boundary."""
        root = package()
        module = root.members["task"]
        module.exports = ["External"]
        module.set_member("External", griffe.Alias("External", "missing_external.PublicType"))
        docs = {"docs/api.rst": ".. automodule:: nidaqmx.task\n   :members:\n   :undoc-members:\n"}
        with self.assertRaisesRegex(ValueError, "external"):
            expose_documented_api(root, documented_api(docs))

    def test_selected_private_member_respects_undoc_members(self):
        """The flag includes members without docstrings, not otherwise."""
        for description, include_undocumented, expected in (
            (None, False, False),
            ("", False, False),
            (None, True, True),
            ("Documented function.", False, True),
            ("Documented function.", True, True),
        ):
            with self.subTest(description=description, include_undocumented=include_undocumented):
                root = package()
                docstring = None if description is None else griffe.Docstring(description)
                root.members["task"].set_member(
                    "_selected", griffe.Function("_selected", docstring=docstring)
                )
                source = ".. automodule:: nidaqmx.task\n   :members: _selected\n"
                if include_undocumented:
                    source += "   :undoc-members:\n"
                expose_documented_api(root, documented_api({"docs/api.rst": source}))
                self.assertEqual(root.members["task"].members["_selected"].is_public, expected)

    def test_undoc_members_alone_does_not_select_private_members(self):
        """The flag does not enable member selection or private discovery."""
        root = package()
        root.members["task"].set_member("_hidden", griffe.Function("_hidden"))
        api = documented_api({"docs/api.rst": ".. automodule:: nidaqmx.task\n   :undoc-members:\n"})
        expose_documented_api(root, api)
        self.assertEqual(api.members, {})
        self.assertFalse(root.members["task"].members["_hidden"].is_public)

    def test_class_member_selections_are_resolved(self):
        """Class-level named selections use the documented class owner."""
        old, new = package(), package()
        old.members["task"].members["Task"].set_member("_selected", griffe.Function("_selected"))
        docs = {
            "docs/api.rst": ".. autoclass:: nidaqmx.Task\n   :members: _selected\n   :undoc-members:\n"
        }
        self.assertIn(
            "nidaqmx.task.Task._selected", self.compare(old, new, old_docs=docs, new_docs={})
        )

    def test_public_member_removal_without_documentation(self):
        """Native public API checks do not require a documentation entry."""
        old, new = package(alias=False), package(alias=False)
        old.members["task"].set_member("public_function", griffe.Function("public_function"))
        self.assertIn(
            "nidaqmx.task.public_function", self.compare(old, new, old_docs={}, new_docs={})
        )

    def test_selected_external_alias_is_fatal_without_export(self):
        """Explicit selection requires resolution even outside __all__."""
        root = package()
        root.members["task"].set_member(
            "External", griffe.Alias("External", "missing_external.PublicType")
        )
        docs = {
            "docs/api.rst": ".. automodule:: nidaqmx.task\n   :members: External\n   :undoc-members:\n"
        }
        with self.assertRaisesRegex(ValueError, "external"):
            expose_documented_api(root, documented_api(docs))

    def test_public_external_alias_chain_is_fatal(self):
        """Forwarding through an internal module cannot hide a public export."""
        root = package()
        root.members["task"].set_member(
            "External", griffe.Alias("External", "missing_external.PublicType")
        )
        root.set_member("External", griffe.Alias("External", "nidaqmx.task.External"))
        root.exports = ["External"]
        with self.assertRaisesRegex(ValueError, "external"):
            expose_documented_api(root, documented_api(API_DOCS))

    def test_explicit_object_external_alias_is_fatal(self):
        """Direct object declarations cannot skip an external target."""
        root = package()
        root.set_member("External", griffe.Alias("External", "missing_external.PublicType"))
        docs = {"docs/api.rst": ".. autoclass:: nidaqmx.External\n"}
        with self.assertRaisesRegex(ValueError, "external"):
            expose_documented_api(root, documented_api(docs))


class RunnerTests(unittest.TestCase):
    """Verify fail-closed execution and workflow-command output."""

    def execute(self, *, approved=False, broken=False, failure=None):
        """Capture a complete comparison with isolated snapshot providers."""
        old, new = package(), package(collection=not broken)
        self.output = io.StringIO()
        with (
            patch("check_api_compatibility.resolve_baseline", return_value=("BASE", "SHA")),
            patch(
                "check_api_compatibility.griffe.load_git", autospec=True, return_value=old
            ) as load_old,
            patch(
                "check_api_compatibility.griffe.load", autospec=True, return_value=new
            ) as load_new,
            patch("check_api_compatibility.documentation_sources", return_value=API_DOCS) as docs,
            redirect_stdout(self.output),
        ):
            if failure == "load":
                load_old.side_effect = ImportError("loading failed")
            if failure == "candidate":
                load_new.side_effect = SyntaxError("parsing failed")
            if failure == "docs":
                docs.side_effect = ValueError("invalid documentation")
            if failure == "unresolved":
                docs.return_value = {"docs/api.rst": ".. automodule:: nidaqmx.missing\n"}
            if failure == "selection":
                docs.return_value = {
                    "docs/api.rst": ".. automodule:: nidaqmx.task\n   :members: missing\n"
                }
            if failure == "external":
                old.members["task"].set_member(
                    "External", griffe.Alias("External", "missing_external.PublicType")
                )
                old.members["task"].exports = ["External"]
            status = check("BASE", approved)
            load_old.assert_called_once()
            load_new.assert_called_once()
            self.assertEqual(docs.call_args_list[0].args, ("SHA",))
            self.assertEqual(docs.call_args_list[1].args, ())
        return status, self.output.getvalue()

    def test_unchanged_and_approved_regressions(self):
        """Approval changes findings' exit status without hiding them."""
        status, output = self.execute()
        self.assertEqual(status, 0)
        self.assertNotIn("::warning::", output)
        for approved, expected in ((False, 1), (True, 0), (False, 1)):
            status, output = self.execute(approved=approved, broken=True)
            self.assertEqual(status, expected)
            self.assertIn(
                "::warning::nidaqmx.system._collections.device_collection.DeviceCollection.device_names",
                output,
            )
            self.assertEqual("::notice::" in output, approved)

    def test_loading_and_documentation_errors_are_not_approved(self):
        """The approval label cannot waive an incomplete API comparison."""
        for failure, expected in (
            ("load", ImportError),
            ("candidate", SyntaxError),
            ("docs", ValueError),
            ("unresolved", ValueError),
            ("selection", ValueError),
            ("external", ValueError),
        ):
            with self.subTest(failure=failure):
                with self.assertRaises(expected):
                    self.execute(approved=True, failure=failure)
                self.assertNotIn("::notice::", self.output.getvalue())

    def test_analysis_and_annotation_errors_are_not_approved(self):
        """Approval requires successful analysis and annotation formatting."""
        for target in ("find_breaking_changes", "Breakage.explain"):
            with self.subTest(target=target):
                with patch(
                    f"check_api_compatibility.griffe.{target}",
                    side_effect=RuntimeError("analysis failed"),
                ):
                    with self.assertRaises(RuntimeError):
                        self.execute(approved=True, broken=True)
                self.assertNotIn("::notice::", self.output.getvalue())

    def test_annotation_escaping_and_single_root_comparison(self):
        """A finding produces one command, not an injected second command."""
        module = griffe.Module("nidaqmx.utils", filepath=Path("generated/nidaqmx/utils.py"))
        attribute = griffe.Attribute("VALUE", parent=module, lineno=1)
        finding = griffe.AttributeChangedValueBreakage(
            attribute, "50%\r\n::error::injected", "100%"
        )
        with patch(
            "check_api_compatibility.griffe.find_breaking_changes", return_value=iter([finding])
        ) as compare:
            status, output = self.execute(broken=True)
            compare.assert_called_once()
        self.assertEqual(status, 1)
        warnings = [line for line in output.splitlines() if line.startswith("::warning::")]
        self.assertEqual(len(warnings), 1)
        self.assertIn("50%25%0D%0A::error::injected", warnings[0])
        self.assertFalse(any(line.startswith("::error::") for line in output.splitlines()))

    def test_default_and_explicit_baselines(self):
        """Default tags and explicit refs use the same verified Git resolver."""
        with patch(
            "check_api_compatibility.subprocess.check_output",
            side_effect=["1.6.0\n1.5.0\n", "SHA\n"],
        ) as git:
            self.assertEqual(resolve_baseline(""), ("1.6.0", "SHA"))
            self.assertEqual(git.call_args.args[0][-1], "1.6.0^{commit}")
        with patch("check_api_compatibility.subprocess.check_output", return_value="SHA\n") as git:
            self.assertEqual(resolve_baseline("--untrusted"), ("--untrusted", "SHA"))
            self.assertIn("--end-of-options", git.call_args.args[0])
        with patch("check_api_compatibility.subprocess.check_output", return_value=""):
            with self.assertRaisesRegex(RuntimeError, "No release tag"):
                resolve_baseline("")

    def test_git_failure_remains_fatal(self):
        """Unavailable baselines cannot be approved as compatibility findings."""
        with patch(
            "check_api_compatibility.subprocess.check_output",
            side_effect=subprocess.CalledProcessError(128, "git"),
        ):
            with self.assertRaises(subprocess.CalledProcessError):
                check("BASE", approved=True)


if __name__ == "__main__":
    unittest.main()
