"""Import fixtures from component tests for benchmark tests."""

# Import all fixtures from component conftest.py to make them available for benchmark tests
from tests.component.conftest import *  # noqa: F403, F401
