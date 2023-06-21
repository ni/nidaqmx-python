"""Generates gRPC Python stubs from proto files."""

import os
import pathlib
from typing import Sequence

import grpc_tools.protoc
import pkg_resources


STUBS_NAMESPACE = "nidaqmx._stubs"
PROTO_PARENT_NAMESPACES = ["src.codegen", "protos"]
STUBS_PATH = (
    pathlib.Path(__file__).parent.parent.parent / "generated" / STUBS_NAMESPACE.replace(".", "/")
)
PROTO_PATH = pathlib.Path(__file__).parent.parent.parent / "src" / "codegen" / "protos"
PROTO_FILES = list(PROTO_PATH.rglob("*.proto"))


def generate_stubs():
    """Generate and fixup gRPC Python stubs."""
    generate_python_files(STUBS_PATH, PROTO_PATH, PROTO_FILES)
    fix_import_paths(STUBS_PATH, STUBS_NAMESPACE, PROTO_PARENT_NAMESPACES)
    add_init_files(STUBS_PATH, PROTO_PATH)


def is_relative_to(path: pathlib.PurePath, other: pathlib.PurePath) -> bool:
    """Return whether or not this path is relative to the other path."""
    try:
        path.relative_to(other)
        return True
    except ValueError:
        return False


def generate_python_files(
    stubs_path: pathlib.Path, proto_path: pathlib.Path, proto_files: Sequence[pathlib.Path]
):
    """Generate python files from .proto files with protoc."""
    os.makedirs(stubs_path, exist_ok=True)
    arguments = [
        "protoc",
        f"--proto_path={str(proto_path)}",
        f"--proto_path={pkg_resources.resource_filename('grpc_tools', '_proto')}",
        f"--python_out={str(stubs_path)}",
        f"--mypy_out={str(stubs_path)}",
        f"--grpc_python_out={str(stubs_path)}",
        f"--mypy_grpc_out={str(stubs_path)}",
    ]
    arguments += [str(path.relative_to(proto_path)).replace("\\", "/") for path in proto_files]

    print(proto_files)

    grpc_tools.protoc.main(arguments)


def fix_import_paths(
    stubs_path: pathlib.Path, stubs_namespace: str, proto_parent_namespaces: Sequence[str]
):
    """Fix import paths of generated files."""
    print("Fixing import paths")
    grpc_codegened_file_paths = list(stubs_path.rglob("*pb2*py"))
    imports_to_fix = [path.stem for path in grpc_codegened_file_paths if path.parent == stubs_path]
    grpc_codegened_file_paths.extend(stubs_path.rglob("*pb2*pyi"))
    for path in grpc_codegened_file_paths:
        print(f"Processing {path}")
        data = path.read_bytes()
        for name in imports_to_fix:
            data = data.replace(
                f"import {name}".encode(), f"from {stubs_namespace} import {name}".encode()
            )

        for namespace in proto_parent_namespaces:
            data = data.replace(
                f"from {namespace}".encode(),
                f"from {stubs_namespace}.{namespace}".encode(),
            )
        path.write_bytes(data)


def add_init_files(stubs_path: pathlib.Path, proto_path: pathlib.Path):
    """Add __init__.py files to generated file directories."""
    for dir in stubs_path.rglob(""):
        if not is_relative_to(dir, proto_path) and dir.is_dir():
            init_path = dir / "__init__.py"
            print(f"Creating {init_path}")
            init_path.write_bytes(b'"""Auto generated gRPC files."""\n')
