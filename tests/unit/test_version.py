import importlib.metadata

import nidaqmx


def test___version_attribute___matches_importlib_metadata() -> None:
    assert nidaqmx.__version__ == importlib.metadata.version("nidaqmx")
