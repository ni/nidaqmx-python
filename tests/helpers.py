"""This contains the helpers methods used in the DAQmx tests."""

import contextlib
import pathlib
from typing import Generator, Optional, Union

from nidaqmx.system.physical_channel import PhysicalChannel

# Power uses fixed-point scaling, so we have a pretty wide epsilon.
POWER_ABS_EPSILON = 1e-3


def generate_random_seed():
    """Creates a random integer."""
    # Randomizing the random seed makes the GitHub test reporting action
    # (EnricoMi/publish-unit-test-result-action) report many added/removed
    # tests, so use the same random seed every time.
    return 42


@contextlib.contextmanager
def configure_teds(
    phys_chan: PhysicalChannel, teds_file_path: Optional[Union[str, pathlib.PurePath]] = None
) -> Generator[PhysicalChannel, None, None]:
    """Yields a physical channel with TEDS configured and then clears it after the test is done."""
    phys_chan.configure_teds(teds_file_path)
    try:
        yield phys_chan
    finally:
        phys_chan.clear_teds()
