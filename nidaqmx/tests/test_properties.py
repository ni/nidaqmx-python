import pytest
import random
import six

import nidaqmx
import nidaqmx.system
from nidaqmx import DaqError
from nidaqmx.constants import AcquisitionType, UsageTypeAI
from nidaqmx.tests.fixtures import x_series_device, bridge_device
from nidaqmx.tests.helpers import generate_random_seed


class TestPropertyBasicDataTypes(object):
    """
    Contains a collection of pytest tests that validate the property getter,
    setter and deleter methods for different basic data types.
    """

    def test_boolean_property(self, x_series_device):

        with nidaqmx.Task() as task:
            task.ai_channels.add_ai_voltage_chan(
                x_series_device.ai_physical_chans[0].name)

            task.timing.cfg_samp_clk_timing(1000)
            task.triggers.start_trigger.cfg_dig_edge_start_trig(
                '/{0}/Ctr0InternalOutput'.format(x_series_device.name))

            # Test property initial value.
            assert not task.triggers.start_trigger.retriggerable

            # Test property setter and getter.
            task.triggers.start_trigger.retriggerable = True
            assert task.triggers.start_trigger.retriggerable

            # Test property deleter.
            del task.triggers.start_trigger.retriggerable
            assert not task.triggers.start_trigger.retriggerable

    def test_enum_property(self, x_series_device):

        with nidaqmx.Task() as task:
            task.ai_channels.add_ai_voltage_chan(
                x_series_device.ai_physical_chans[0].name)

            task.timing.cfg_samp_clk_timing(
                1000, sample_mode=AcquisitionType.CONTINUOUS)

            # Test property initial value.
            assert (task.timing.samp_quant_samp_mode ==
                    AcquisitionType.CONTINUOUS)

            # Test property setter and getter.
            task.timing.samp_quant_samp_mode = AcquisitionType.FINITE
            assert (task.timing.samp_quant_samp_mode ==
                    AcquisitionType.FINITE)

            # Test property deleter.
            del task.timing.samp_quant_samp_mode
            assert (task.timing.samp_quant_samp_mode ==
                    AcquisitionType.CONTINUOUS)

    def test_float_property(self, x_series_device):

        with nidaqmx.Task() as task:
            ai_channel = task.ai_channels.add_ai_voltage_chan(
                x_series_device.ai_physical_chans[0].name, max_val=5)

            # Test property default value.
            assert ai_channel.ai_max == 5

            # Test property setter and getter.
            max_value = 10
            ai_channel.ai_max = max_value
            assert ai_channel.ai_max == max_value

            # Test property deleter. Reading this property will throw an
            # error after being reset.
            del ai_channel.ai_max
            with pytest.raises(DaqError) as e:
                read_value = ai_channel.ai_max
            assert e.value.error_code == -200695

    @pytest.mark.parametrize('seed', [generate_random_seed()])
    def test_int_property(self, x_series_device, seed):
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        with nidaqmx.Task() as task:
            task.ci_channels.add_ci_count_edges_chan(
                x_series_device.ci_physical_chans[0].name)

            # Test property default value.
            assert task.in_stream.offset == 0

            # Test property setter and getter.
            value_to_test = random.randint(0, 100)
            task.in_stream.offset = value_to_test
            assert task.in_stream.offset == value_to_test

            value_to_test = random.randint(-100, 0)
            task.in_stream.offset = value_to_test
            assert task.in_stream.offset == value_to_test

            # Test property deleter.
            del task.in_stream.offset
            assert task.in_stream.offset == 0

    def test_string_property(self, x_series_device):

        with nidaqmx.Task() as task:
            ai_channel = task.ai_channels.add_ai_voltage_chan(
                x_series_device.ai_physical_chans[0].name)

            # Test property default value.
            assert ai_channel.description == ''

            # Test property setter and getter.
            description = 'Channel description.'
            ai_channel.description = description
            assert ai_channel.description == description

            # Test property deleter.
            del ai_channel.description
            assert ai_channel.description == ''

    @pytest.mark.parametrize('seed', [generate_random_seed()])
    def test_uint_property(self, x_series_device, seed):
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        with nidaqmx.Task() as task:
            task.ai_channels.add_ai_voltage_chan(
                x_series_device.ai_physical_chans[0].name)

            task.timing.cfg_samp_clk_timing(1000)

            # Test property initial value.
            assert task.timing.samp_clk_timebase_div == 100000

            # Test property setter and getter.
            value_to_test = random.randint(500, 10000)
            task.timing.samp_clk_timebase_div = value_to_test
            assert task.timing.samp_clk_timebase_div == value_to_test

            # Test property deleter.
            del task.timing.samp_clk_timebase_div
            assert task.timing.samp_clk_timebase_div == 100000


class TestPropertyListDataTypes(object):
    """
    Contains a collection of pytest tests that validate the property getter
    setter, and deleter methods for list data types.

    There are almost no setter and deleter methods for properties that have
    list data types.
    """

    def test_list_of_strings_property(self, x_series_device):

        terminals = x_series_device.terminals

        assert isinstance(terminals, list)
        assert isinstance(terminals[0], six.string_types)

    def test_list_of_enums_property(self, x_series_device):

        terminals = x_series_device.ai_meas_types

        assert isinstance(terminals, list)
        assert isinstance(terminals[0], UsageTypeAI)

    @pytest.mark.skipif(bridge_device() is None, 
                        reason="requires bridge device")
    @pytest.mark.parametrize('seed', [generate_random_seed()])
    def test_list_of_floats_property(self, bridge_device, seed):
        # Reset the pseudorandom number generator with seed.
        random.seed(seed)

        with nidaqmx.Task() as task:
            ai_channel = task.ai_channels.add_ai_bridge_chan(
                bridge_device.ai_physical_chans[0].name)

            # Test default property value.
            assert isinstance(ai_channel.ai_bridge_poly_forward_coeff, list)
            assert len(ai_channel.ai_bridge_poly_forward_coeff) == 0

            # Test property setter and getter.
            value_to_test = [random.randint(-10, 10) for _ in
                             range(random.randint(2, 5))]
            ai_channel.ai_bridge_poly_forward_coeff = value_to_test
            assert ai_channel.ai_bridge_poly_forward_coeff == value_to_test

            # Test property deleter.
            del ai_channel.ai_bridge_poly_forward_coeff
            assert isinstance(ai_channel.ai_bridge_poly_forward_coeff, list)
            assert len(ai_channel.ai_bridge_poly_forward_coeff) == 0
