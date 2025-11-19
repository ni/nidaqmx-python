from __future__ import annotations

import inspect
import sys
import traceback
from pathlib import Path


def get_dotenv_search_path() -> Path:
    """Get the search path for loading the `.env` file."""
    # Prefer to load the `.env` file from the current directory or its parents.
    # If the current directory doesn't have a `.env` file, fall back to the
    # script/EXE path or the TestStand code module path.
    cwd = Path.cwd()
    if not _has_dotenv_file(cwd):
        if script_or_exe_path := _get_script_or_exe_path():
            return script_or_exe_path.resolve().parent
        if caller_path := _get_caller_path():
            return caller_path.resolve().parent
    return cwd


def _has_dotenv_file(dir: Path) -> bool:
    """Check whether the dir or its parents contains a `.env` file."""
    return (dir / ".env").exists() or any((p / ".env").exists() for p in dir.parents)


def _get_script_or_exe_path() -> Path | None:
    """Get the path of the top-level script or PyInstaller EXE, if possible."""
    if getattr(sys, "frozen", False):
        return Path(sys.executable)

    main_module = sys.modules.get("__main__")
    if main_module:
        script_path = getattr(main_module, "__file__", "")
        if script_path:
            return Path(script_path)

    return None


def _get_caller_path() -> Path | None:
    """Get the path of the module calling into this package, if possible."""
    package_path = _get_package_path()
    for frame, _ in traceback.walk_stack(inspect.currentframe()):
        if frame.f_code.co_filename:
            module_path = Path(frame.f_code.co_filename)
            if _exists(module_path) and not module_path.is_relative_to(package_path):
                return module_path

    return None


# Path.exists() throws OSError when the path has invalid file characters.
# https://github.com/python/cpython/issues/79487
if sys.version_info >= (3, 10):

    def _exists(path: Path) -> bool:
        return path.exists()

else:

    def _exists(path: Path) -> bool:
        import os

        return os.path.exists(path)


def _get_package_path() -> Path:
    """Get the path of this package."""
    module = sys.modules[__package__]
    assert module.__file__ and module.__file__.endswith("__init__.py")
    return Path(module.__file__).parent
