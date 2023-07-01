"""This contains the helpers methods used in the DAQmx tests."""


# Power uses fixed-point scaling, so we have a pretty wide epsilon.
POWER_ABS_EPSILON = 1e-3


def generate_random_seed():
    """Creates a random integer."""
    # Randomizing the random seed makes the GitHub test reporting action
    # (EnricoMi/publish-unit-test-result-action) report many added/removed
    # tests, so use the same random seed every time.
    return 42
