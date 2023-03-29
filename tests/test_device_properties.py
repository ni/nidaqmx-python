"""Tests for validating device properties for different basic data types."""
from nidaqmx.constants import BusType, TriggerUsage


class TestDevicePropertyDataTypes(object):
    """Contains a collection of pytest tests.

    This validates the property getter,setter and deleter methods for different
    data types of device properties.
    """

    def test_boolean_property(self, bridge_device):
        """Test for validating the device property of boolean type."""
        # The PXIe-4331 supports analog triggering
        assert bridge_device.anlg_trig_supported

    def test_float_property(self, bridge_device):
        """Test for validating the device property of float type."""
        # The ai max single channel rate of the NI PXIe-4331 device is 102400.0
        assert bridge_device.ai_max_single_chan_rate == 102400.0

    def test_uint_property(self, bridge_device):
        """Test for validating the device property of uint type."""
        assert bridge_device.product_num == 1957283012

    def test_string_property(self, bridge_device):
        """Test for validating a device property of string type."""
        assert bridge_device.product_type == "PXIe-4331"

    def test_enum_property(self, bridge_device):
        """Test for validating a device property of enum type."""
        assert bridge_device.bus_type == BusType.PXIE

    def test_list_of_float_property(self, bridge_device):
        """Test for validating the device property of a float array type."""
        assert len(bridge_device.ai_bridge_rngs) == 4
        assert bridge_device.ai_bridge_rngs == [-0.025, 0.025, -0.1, 0.1]

    def test_list_of_enums_property(self, bridge_device):
        """Test for validating the device property of a enum array type."""
        assert len(bridge_device.ai_trig_usage) == 2
        assert bridge_device.ai_trig_usage == [TriggerUsage.REFERENCE, TriggerUsage.START]

    def test_list_of_uint_property(self, bridge_device):
        """Test for validating the device property of uint array type."""
        assert len(bridge_device.accessory_product_nums) == 1
        assert bridge_device.accessory_product_nums == [31122]
