"""Tests for validating device properties for different basic data types."""
import pytest

from nidaqmx.constants import BusType, TriggerUsage


class TestDevicePropertyDataTypes(object):
    """Contains a collection of pytest tests.

    This validates the property getter,setter and deleter methods for different
    data types of device properties.
    """

    @pytest.mark.parametrize("test_device", ["bridgeTester"], indirect=True)
    def test_boolean_property(self, test_device):
        """Test for validating the device property of boolean type."""
        # The PXIe-4331 supports analog triggering
        assert test_device.anlg_trig_supported

    @pytest.mark.parametrize("test_device", ["bridgeTester"], indirect=True)
    def test_float_property(self, test_device):
        """Test for validating the device property of float type."""
        # The ai max single channel rate of the NI PXIe-4331 device is 102400.0
        assert test_device.ai_max_single_chan_rate == 102400.0

    @pytest.mark.parametrize("test_device", ["bridgeTester"], indirect=True)
    def test_uint_property(self, test_device):
        """Test for validating the device property of uint type."""
        assert test_device.product_num == 0x74A9C4C4

    @pytest.mark.parametrize("test_device", ["bridgeTester"], indirect=True)
    def test_string_property(self, test_device):
        """Test for validating a device property of string type."""
        assert test_device.product_type == "PXIe-4331"

    @pytest.mark.parametrize("test_device", ["bridgeTester"], indirect=True)
    def test_enum_property(self, test_device):
        """Test for validating a device property of enum type."""
        assert test_device.bus_type == BusType.PXIE

    @pytest.mark.parametrize("test_device", ["bridgeTester"], indirect=True)
    def test_list_of_float_property(self, test_device):
        """Test for validating the device property of a float array type."""
        ai_bridge_ranges = test_device.ai_bridge_rngs

        assert isinstance(ai_bridge_ranges, list)
        assert ai_bridge_ranges == [-0.025, 0.025, -0.1, 0.1]

    @pytest.mark.parametrize("test_device", ["bridgeTester"], indirect=True)
    def test_list_of_enums_property(self, test_device):
        """Test for validating the device property of a enum array type."""
        ai_trigger_usage = test_device.ai_trig_usage

        assert isinstance(ai_trigger_usage, list)
        assert ai_trigger_usage == [TriggerUsage.REFERENCE, TriggerUsage.START]

    @pytest.mark.parametrize("test_device", ["bridgeTester"], indirect=True)
    def test_list_of_uint_property(self, test_device):
        """Test for validating the device property of uint array type."""
        accessory_product_numbers = test_device.accessory_product_nums

        assert isinstance(accessory_product_numbers, list)
        assert accessory_product_numbers == [0x7992]
