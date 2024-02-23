"""Tests for validating systems collections."""

import collections.abc

import nidaqmx
import nidaqmx.system
from nidaqmx.system._collections.device_collection import DeviceCollection
from nidaqmx.system._collections.persisted_channel_collection import (
    PersistedChannelCollection,
)
from nidaqmx.system._collections.persisted_scale_collection import (
    PersistedScaleCollection,
)
from nidaqmx.system._collections.persisted_task_collection import (
    PersistedTaskCollection,
)
from nidaqmx.system._collections.physical_channel_collection import (
    PhysicalChannelCollection,
)


class TestSystemCollections:
    """Contains a collection of pytest tests.

    These validate the system collections functionality in the NI-DAQmx Python API.
    """

    def test_devices_collection_property(self, system):
        """Test to validate device collection property."""
        devices = system.devices
        assert isinstance(devices, DeviceCollection)
        assert isinstance(devices, collections.abc.Sequence)

        assert isinstance(devices[0], nidaqmx.system.Device)
        assert isinstance(devices[0].is_simulated, bool)

    def test_persisted_scale_collection_property(self, system):
        """Test to validate persisted scale property."""
        scales = system.scales
        assert isinstance(scales, PersistedScaleCollection)
        assert isinstance(scales, collections.abc.Sequence)

        if len(scales) > 0:
            assert isinstance(scales[0], nidaqmx.system.storage.PersistedScale)

            # Test specific property on object.
            assert isinstance(scales[0].author, str)

    def test_persisted_task_collection_property(self, system):
        """Test to validate persisted task collection property."""
        tasks = system.tasks
        assert isinstance(tasks, PersistedTaskCollection)
        assert isinstance(tasks, collections.abc.Sequence)

        if len(tasks) > 0:
            assert isinstance(tasks[0], nidaqmx.system.storage.PersistedTask)

            # Test specific property on object.
            assert isinstance(tasks[0].author, str)

    def test_persisted_channel_collection_property(self, system):
        """Test to validate persisted channel collection property."""
        global_channels = system.global_channels
        assert isinstance(global_channels, PersistedChannelCollection)
        assert isinstance(global_channels, collections.abc.Sequence)

        if len(global_channels) > 0:
            assert isinstance(global_channels[0], nidaqmx.system.storage.PersistedChannel)

            # Test specific property on object.
            assert isinstance(global_channels[0].author, str)

    def test_physical_channel_collection_property(self, sim_6363_device):
        """Test to validate physical channel collection property."""
        phys_chans = sim_6363_device.ai_physical_chans

        assert isinstance(phys_chans, PhysicalChannelCollection)
        assert isinstance(phys_chans, collections.abc.Sequence)

        assert isinstance(phys_chans[0], nidaqmx.system.PhysicalChannel)

        # Test specific property on object.
        assert isinstance(phys_chans[0].ai_meas_types, list)
