"""Generates gRPC Python stubs from proto files."""

import os
import pathlib
from collections.abc import Sequence

import grpc_tools.protoc
import pkg_resources


STUBS_NAMESPACE = "nidaqmx._stubs"
PROTO_PARENT_NAMESPACES = ["src.codegen", "protos"]
STUBS_PATH = (
    pathlib.Path(__file__).parent.parent.parent / "generated" / STUBS_NAMESPACE.replace(".", "/")
)
PROTO_PATH = pathlib.Path(__file__).parent.parent.parent / "src" / "codegen" / "protos"
NI_APIS_PATH = pathlib.Path(__file__).parent.parent.parent / "third_party" / "ni-apis"
PROTO_FILES = list(PROTO_PATH.rglob("*.proto"))


def generate_stubs():
    """Generate and fixup gRPC Python stubs."""
    generate_python_files(STUBS_PATH, PROTO_PATH, PROTO_FILES)
    generate_waveform_stubs(STUBS_PATH)
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
        f"--proto_path={str(NI_APIS_PATH / 'ni' / 'grpcdevice' / 'v1')}",  # ni-apis session.proto location for import resolution
        f"--proto_path={str(NI_APIS_PATH)}",  # ni-apis root for ni/protobuf/types/waveform.proto resolution
        f"--proto_path={pkg_resources.resource_filename('grpc_tools', '_proto')}",
        f"--python_out={str(stubs_path)}",
        f"--mypy_out={str(stubs_path)}",
        f"--grpc_python_out={str(stubs_path)}",
        f"--mypy_grpc_out={str(stubs_path)}",
    ]
    arguments += [str(path.relative_to(proto_path)).replace("\\", "/") for path in proto_files]

    print(proto_files)

    grpc_tools.protoc.main(arguments)


def generate_waveform_stubs(stubs_path: pathlib.Path):
    """Generate waveform protobuf stubs from ni-apis."""
    waveform_stubs_path = stubs_path / "ni" / "protobuf" / "types"
    os.makedirs(waveform_stubs_path, exist_ok=True)
    
    # Generate all protobuf files from ni/protobuf/types
    ni_types_protos = [
        "ni/protobuf/types/precision_timestamp.proto",
        "ni/protobuf/types/waveform.proto"
    ]
    
    for proto_file in ni_types_protos:
        arguments = [
            "protoc",
            f"--proto_path={str(NI_APIS_PATH)}",
            f"--proto_path={pkg_resources.resource_filename('grpc_tools', '_proto')}",
            f"--python_out={str(stubs_path)}",
            proto_file
        ]
        
        print(f"Generating {proto_file} stubs:", arguments)
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
        data = path.read_text(encoding='utf-8')
        
        # Fix import statements - only modify lines that don't already have the namespace
        for name in imports_to_fix:
            # Skip session_pb2 as it should use the installed package
            if name == "session_pb2":
                continue
                
            # Only replace standalone import statements, not ones already prefixed with namespace
            import_pattern = f"import {name}"
            replacement = f"from {stubs_namespace} import {name}"
            
            # Split into lines to process line by line
            lines = data.split('\n')
            for i, line in enumerate(lines):
                # Only replace if line doesn't already contain the namespace
                if import_pattern in line and stubs_namespace not in line:
                    lines[i] = line.replace(import_pattern, replacement)
            data = '\n'.join(lines)

        for namespace in proto_parent_namespaces:
            # Similar fix for namespace imports
            from_pattern = f"from {namespace}"
            replacement = f"from {stubs_namespace}.{namespace}"
            
            lines = data.split('\n')
            for i, line in enumerate(lines):
                # Only replace if line doesn't already contain the stubs namespace
                if from_pattern in line and f"{stubs_namespace}.{namespace}" not in line:
                    lines[i] = line.replace(from_pattern, replacement)
            data = '\n'.join(lines)
        
        # Fix ni.protobuf.types imports to use stubs namespace
        ni_types_pattern = "from ni.protobuf.types"
        ni_types_replacement = f"from {stubs_namespace}.ni.protobuf.types"
        
        lines = data.split('\n')
        for i, line in enumerate(lines):
            if ni_types_pattern in line and stubs_namespace not in line:
                lines[i] = line.replace(ni_types_pattern, ni_types_replacement)
        data = '\n'.join(lines)
            
        path.write_text(data, encoding='utf-8')


def add_init_files(stubs_path: pathlib.Path, proto_path: pathlib.Path):
    """Add __init__.py files to generated file directories."""
    for dir in stubs_path.rglob(""):
        if not is_relative_to(dir, proto_path) and dir.is_dir():
            python_files = list(dir.glob("*.py"))
            if python_files:
                init_path = dir / "__init__.py"
                print(f"Creating {init_path}")
                init_path.write_bytes(b'"""Auto generated gRPC files."""\n')
