from pathlib import Path

import pytest

from nidaqmx import _dotenv_path


@pytest.mark.parametrize("dotenv_exists", [False, True])
def test___dotenv_exists_varies___has_dotenv_file___matches_dotenv_exists(
    dotenv_exists: bool, tmp_path: Path
) -> None:
    if dotenv_exists:
        (tmp_path / ".env").write_text("")
    subdirs = [tmp_path / "a", tmp_path / "a" / "b", tmp_path / "a" / "b" / "c"]
    for dir in subdirs:
        dir.mkdir()

    assert _dotenv_path._has_dotenv_file(tmp_path) == dotenv_exists
    assert all([_dotenv_path._has_dotenv_file(p) == dotenv_exists for p in subdirs])


def test___get_caller_path___returns_this_modules_path() -> None:
    assert _dotenv_path._get_caller_path() == Path(__file__)


def test___get_package_path___returns_package_dir() -> None:
    assert _dotenv_path._get_package_path() == Path(_dotenv_path.__file__).parent


def test___get_script_or_exe_path___returns_pytest_path() -> None:
    path = _dotenv_path._get_script_or_exe_path()

    assert path is not None
    assert "pytest" in path.parts or "pytest.exe" in path.parts or "vscode_pytest" in path.parts
