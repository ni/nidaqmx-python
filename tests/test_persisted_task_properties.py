"""Tests for validating persisted task properties for different data types."""
import random

import pytest
import six

import nidaqmx
import nidaqmx.system
from nidaqmx import DaqError
from nidaqmx.constants import AcquisitionType, UsageTypeAI
from nidaqmx.tests.helpers import generate_random_seed


class TestPersistedTaskPropertyDataTypes(object):
    """Contains a collection of pytest tests.

    This validates the property getter,setter and deleter methods for persisted task properties for different data types.
    """
    @pytest.fixture(scope="class")
    def voltage_tester_task(self):
        system = nidaqmx.system.System.local()
        voltage_tester_task = system.tasks[0]
        return voltage_tester_task

    def test_boolean_property(self, voltage_tester_task):
        """Test for validating boolean properties in persisted task."""
        assert voltage_tester_task.allow_interactive_editing
    
    def test_string_property(self, voltage_tester_task):
        """Test for validating boolean properties in persisted task."""
        author = voltage_tester_task.author

        assert isinstance(author, str)


