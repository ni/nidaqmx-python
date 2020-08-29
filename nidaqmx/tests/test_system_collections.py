import pytest
import six

if six.PY2:
    from collections import Sequence
else:
    from collections.abc import Sequence

import nidaqmx
import nidaqmx.system
from nidaqmx.system._device_collection import DeviceCollection
from nidaqmx.system._persisted_channel_collection import (
    PersistedChannelCollection)
from nidaqmx.system._persisted_task_collection import (
    PersistedTaskCollection)
from nidaqmx.system._persisted_scale_collection import (
    PersistedScaleCollection)
from nidaqmx.system._physical_channel_collection import (
    PhysicalChannelCollection)
from nidaqmx.tests.fixtures import x_series_device


class TestSystemCollections(object):
    """
    Contains a collection of pytest tests that validate the system
    collections functionality in the NI-DAQmx Python API.
    """

    def test_devices_collection_property(self):
        system = nidaqmx.system.System.local()

        devices = system.devices
        assert isinstance(devices, DeviceCollection)
        assert isinstance(devices, Sequence)

        assert isinstance(devices[0], nidaqmx.system.Device)
        assert isinstance(devices[0].dev_is_simulated, bool)

    def test_persisted_scale_collection_property(self):
        system = nidaqmx.system.System.local()

        scales = system.scales
        assert isinstance(scales, PersistedScaleCollection)
        assert isinstance(scales, Sequence)

        if len(scales) > 0:
            assert isinstance(scales[0], nidaqmx.system.storage.PersistedScale)

            # Test specific property on object.
            assert isinstance(scales[0].author, six.string_types)

    def test_persisted_task_collection_property(self):
        system = nidaqmx.system.System.local()

        tasks = system.tasks
        assert isinstance(tasks, PersistedTaskCollection)
        assert isinstance(tasks, Sequence)

        if len(tasks) > 0:
            assert isinstance(tasks[0], nidaqmx.system.storage.PersistedTask)

            # Test specific property on object.
            assert isinstance(tasks[0].author, six.string_types)

    def test_persisted_channel_collection_property(self):
        system = nidaqmx.system.System.local()

        global_channels = system.global_channels
        assert isinstance(global_channels, PersistedChannelCollection)
        assert isinstance(global_channels, Sequence)

        if len(global_channels) > 0:
            assert isinstance(global_channels[0],
                              nidaqmx.system.storage.PersistedChannel)

            # Test specific property on object.
            assert isinstance(global_channels[0].author, six.string_types)

    def test_physical_channel_collection_property(self, x_series_device):
        phys_chans = x_series_device.ai_physical_chans

        assert isinstance(phys_chans, PhysicalChannelCollection)
        assert isinstance(phys_chans, Sequence)

        assert isinstance(phys_chans[0], nidaqmx.system.PhysicalChannel)

        # Test specific property on object.
        assert isinstance(phys_chans[0].ai_meas_types, list)
