import pytest

from nidaqmx import DaqError
from nidaqmx.constants import AcquisitionType, Edge, SampleTimingType
from nidaqmx.error_codes import DAQmxErrors


def test___timing___get_boolean_property___returns_value(task, sim_6363_device):
    task.ao_channels.add_ao_voltage_chan(sim_6363_device.ao_physical_chans[0].name)
    task.timing.samp_timing_type = SampleTimingType.ON_DEMAND

    assert not task.timing.simultaneous_ao_enable


def test___timing___get_boolean_property_with_device_context___throw_daqerror(
    task, sim_6363_device
):
    task.ao_channels.add_ao_voltage_chan(sim_6363_device.ao_physical_chans[0].name)

    with pytest.raises(DaqError) as e:
        task.timing[sim_6363_device].simultaneous_ao_enable

    assert e.value.error_type == DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT


def test___timing___set_boolean_property___returns_assigned_value(task, sim_6363_device):
    task.ao_channels.add_ao_voltage_chan(sim_6363_device.ao_physical_chans[0].name)
    task.timing.samp_timing_type = SampleTimingType.ON_DEMAND

    task.timing.simultaneous_ao_enable = True

    assert task.timing.simultaneous_ao_enable


def test___timing___set_boolean_property_with_device_context___throw_daqerror(
    task, sim_6363_device
):
    task.ao_channels.add_ao_voltage_chan(sim_6363_device.ao_physical_chans[0].name)
    task.timing.samp_timing_type = SampleTimingType.ON_DEMAND

    with pytest.raises(DaqError) as e:
        task.timing[sim_6363_device].simultaneous_ao_enable = True

    assert e.value.error_type == DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT


def test___timing___reset_boolean_property___returns_default_value(task, sim_6363_device):
    task.ao_channels.add_ao_voltage_chan(sim_6363_device.ao_physical_chans[0].name)
    task.timing.samp_timing_type = SampleTimingType.ON_DEMAND
    task.timing.simultaneous_ao_enable = True

    del task.timing.simultaneous_ao_enable

    assert not task.timing.simultaneous_ao_enable


def test___timing___reset_boolean_property_with_device_context___throw_daqerror(
    task, sim_6363_device
):
    task.ao_channels.add_ao_voltage_chan(sim_6363_device.ao_physical_chans[0].name)
    task.timing.samp_timing_type = SampleTimingType.ON_DEMAND
    task.timing.simultaneous_ao_enable = True

    with pytest.raises(DaqError) as e:
        del task.timing[sim_6363_device].simultaneous_ao_enable

    assert e.value.error_type == DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT


def test___timing___get_string_property___returns_value(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000)

    assert task.timing.samp_clk_src == f"/{sim_6363_device.name}/ai/SampleClockTimebase"


def test___timing___get_string_property_with_device_context___throw_daqerror(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000)

    with pytest.raises(DaqError) as e:
        _ = task.timing[sim_6363_device].samp_clk_src

    assert e.value.error_type == DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT


def test___timing___set_string_property___returns_assigned_value(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000)

    task.timing.samp_clk_src = "PFI0"

    assert task.timing.samp_clk_src == f"/{sim_6363_device.name}/PFI0"


def test___timing___set_string_property_with_device_context___throw_daqerror(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000)

    with pytest.raises(DaqError) as e:
        task.timing[sim_6363_device].samp_clk_src = "PFI0"

    assert e.value.error_type == DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT


def test___timing___reset_string_property___returns_default_value(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000, source="PFI0")

    del task.timing.samp_clk_src

    assert task.timing.samp_clk_src == f"/{sim_6363_device.name}/ai/SampleClockTimebase"


def test___timing___reset_string_property_with_device_context___throw_daqerror(
    task, sim_6363_device
):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000, source="PFI0")

    with pytest.raises(DaqError) as e:
        del task.timing[sim_6363_device].samp_clk_src

    assert e.value.error_type == DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT


def test___timing___set_invalid_source_terminal_name___throws_daqerror(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)

    task.timing.cfg_samp_clk_timing(1000, source="Test_Invalid_Device_Source")

    with pytest.raises(DaqError) as e:
        _ = task.timing.samp_clk_src
    assert e.value.error_type == DAQmxErrors.INVALID_ROUTING_SOURCE_TERMINAL_NAME_ROUTING


def test___timing___get_enum_property___returns_value(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000, sample_mode=AcquisitionType.CONTINUOUS)

    assert task.timing.samp_quant_samp_mode == AcquisitionType.CONTINUOUS


def test___timing___get_enum_property_with_device_context___returns_value(task, sim_9205_device):
    task.ai_channels.add_ai_voltage_chan(sim_9205_device.ai_physical_chans[0].name)

    assert task.timing[sim_9205_device].ai_conv_active_edge == Edge.RISING


def test___timing___get_enum_property_with_device_context___throws_daqerror(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000, sample_mode=AcquisitionType.CONTINUOUS)

    with pytest.raises(DaqError) as e:
        _ = task.timing[sim_6363_device].samp_quant_samp_mode

    assert e.value.error_type == DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT


def test___timing___set_enum_property___returns_assigned_value(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000, sample_mode=AcquisitionType.CONTINUOUS)

    task.timing.samp_quant_samp_mode = AcquisitionType.FINITE

    assert task.timing.samp_quant_samp_mode == AcquisitionType.FINITE


def test___timing___set_enum_property_with_device_context___returns_assigned_value(
    task, sim_9205_device
):
    task.ai_channels.add_ai_voltage_chan(sim_9205_device.ai_physical_chans[0].name)

    task.timing[sim_9205_device].ai_conv_active_edge = Edge.FALLING

    assert task.timing[sim_9205_device].ai_conv_active_edge == Edge.FALLING


def test___timing___set_enum_property_with_device_context___throw_daqerror(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000, sample_mode=AcquisitionType.CONTINUOUS)

    with pytest.raises(DaqError) as e:
        task.timing[sim_6363_device].samp_quant_samp_mode = AcquisitionType.FINITE

    assert e.value.error_type == DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT


def test___timing___reset_enum_property___returns_default_value(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000, sample_mode=AcquisitionType.FINITE)

    del task.timing.samp_quant_samp_mode

    assert task.timing.samp_quant_samp_mode == AcquisitionType.CONTINUOUS


def test___timing___reset_enum_property_with_device_context___returns_default_value(
    task, sim_9205_device
):
    task.ai_channels.add_ai_voltage_chan(sim_9205_device.ai_physical_chans[0].name)
    default_value = task.timing[sim_9205_device].ai_conv_active_edge
    task.timing[sim_9205_device].ai_conv_active_edge = Edge.FALLING

    del task.timing[sim_9205_device].ai_conv_active_edge

    assert task.timing[sim_9205_device].ai_conv_active_edge == default_value


def test___timing___reset_enum_property_with_device_context___throws_daqerror(
    task, sim_6363_device
):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000, sample_mode=AcquisitionType.FINITE)

    with pytest.raises(DaqError) as e:
        del task.timing[sim_6363_device].samp_quant_samp_mode

    assert e.value.error_type == DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT


def test___timing___get_float64_property___returns_value(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000)

    assert task.timing.samp_clk_rate == 1000


def test___timing___get_float64_property_with_device_context___returns_value(task, sim_9205_device):
    task.ai_channels.add_ai_voltage_chan(sim_9205_device.ai_physical_chans[0].name)

    assert task.timing[sim_9205_device].ai_conv_max_rate == 250000.0


def test___timing___get_float64_property_with_device_context___throws_daqerror(
    task, sim_6363_device
):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000)

    with pytest.raises(DaqError) as e:
        _ = task.timing[sim_6363_device].samp_clk_rate

    assert e.value.error_type == DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT


def test___timing___set_float64_property___returns_assigned_value(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000)

    task.timing.samp_clk_rate = 2000

    assert task.timing.samp_clk_rate == 2000


def test___timing___set_float64_property_with_device_context___returns_assigned_value(
    task, sim_9205_device
):
    task.ai_channels.add_ai_voltage_chan(sim_9205_device.ai_physical_chans[0].name)
    task.timing[sim_9205_device].ai_conv_rate = 1000.0

    assert task.timing[sim_9205_device].ai_conv_rate == 1000.0


def test___timing___set_float64_property_with_device_context___throws_daqerror(
    task, sim_6363_device
):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000)

    with pytest.raises(DaqError) as e:
        task.timing[sim_6363_device].samp_clk_rate = 2000

    assert e.value.error_type == DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT


def test___timing___reset_float64_property___returns_default_value(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    default_value = task.timing.samp_clk_rate
    task.timing.cfg_samp_clk_timing(10000)

    del task.timing.samp_clk_rate

    assert task.timing.samp_clk_rate == default_value


def test___timing___reset_float64_property_with_device_context___returns_default_value(
    task, sim_9205_device
):
    task.ai_channels.add_ai_voltage_chan(sim_9205_device.ai_physical_chans[0].name)
    default_value = task.timing[sim_9205_device].ai_conv_rate
    task.timing[sim_9205_device].ai_conv_rate = 123456.0

    del task.timing[sim_9205_device].ai_conv_rate

    assert task.timing[sim_9205_device].ai_conv_rate == default_value


def test___timing___reset_float64_property_with_device_context___throws_daqerror(
    task, sim_6363_device
):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(10000)

    with pytest.raises(DaqError) as e:
        del task.timing[sim_6363_device].samp_clk_rate

    assert e.value.error_type == DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT


def test___timing___get_uint32_property___returns_value(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000)

    assert task.timing.samp_clk_timebase_div == 100000


def test___timing___get_uint32_property_with_device_context___returns_value(task, sim_9205_device):
    task.ai_channels.add_ai_voltage_chan(sim_9205_device.ai_physical_chans[0].name)

    assert task.timing[sim_9205_device].ai_conv_timebase_div == 1121


def test___timing___get_uint32_property_with_device_context___throws_daqerror(
    task, sim_6363_device
):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000)

    with pytest.raises(DaqError) as e:
        _ = task.timing[sim_6363_device].samp_clk_timebase_div

    assert e.value.error_type == DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT


def test___timing___set_uint32_property___returns_assigned_value(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000)

    task.timing.samp_clk_timebase_div = 500

    assert task.timing.samp_clk_timebase_div == 500


def test___timing___set_uint32_property_with_device_context___returns_assigned_value(
    task, sim_9205_device
):
    task.ai_channels.add_ai_voltage_chan(sim_9205_device.ai_physical_chans[0].name)

    task.timing[sim_9205_device].ai_conv_timebase_div = 1150

    assert task.timing[sim_9205_device].ai_conv_timebase_div == 1150


def test___timing___set_uint32_property_with_device_context___throws_daqerror(
    task, sim_6363_device
):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000)

    with pytest.raises(DaqError) as e:
        task.timing[sim_6363_device].samp_clk_timebase_div = 500

    assert e.value.error_type == DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT


def test___timing___reset_uint32_property___returns_default_value(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000)
    default_value = task.timing.samp_clk_timebase_div
    task.timing.samp_clk_timebase_div = 200000
    assert task.timing.samp_clk_rate == 500

    del task.timing.samp_clk_timebase_div

    assert task.timing.samp_clk_timebase_div == default_value


def test___timing___reset_uint32_property_with_device_context___returns_default_value(
    task, sim_9205_device
):
    task.ai_channels.add_ai_voltage_chan(sim_9205_device.ai_physical_chans[0].name)
    default_value = task.timing[sim_9205_device].ai_conv_timebase_div
    task.timing[sim_9205_device].ai_conv_timebase_div = 1150

    del task.timing[sim_9205_device].ai_conv_timebase_div

    assert task.timing[sim_9205_device].ai_conv_timebase_div == default_value


def test___timing___reset_uint32_property_with_device_context___throws_daqerror(
    task, sim_6363_device
):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(10000)

    with pytest.raises(DaqError) as e:
        del task.timing[sim_6363_device].samp_clk_timebase_div

    assert e.value.error_type == DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT


def test___timing___get_uint64_property___returns_value(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000, samps_per_chan=100)

    assert task.timing.samp_quant_samp_per_chan == 100


def test___timing___get_uint64_property_with_device_context___throws_daqerror(
    task, sim_6363_device
):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000, samps_per_chan=100)

    with pytest.raises(DaqError) as e:
        _ = task.timing[sim_6363_device].samp_quant_samp_per_chan

    assert e.value.error_type == DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT


def test___timing___set_uint64_property___returns_assigned_value(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)

    task.timing.samp_quant_samp_per_chan = 10000

    assert task.timing.samp_quant_samp_per_chan == 10000


def test___timing___set_uint64_property_with_device_context___throws_daqerror(
    task, sim_6363_device
):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)

    with pytest.raises(DaqError) as e:
        task.timing[sim_6363_device].samp_quant_samp_per_chan = 10000

    assert e.value.error_type == DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT


def test___timing___reset_uint64_property___returns_default_value(task, sim_6363_device):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    default_value = task.timing.samp_quant_samp_per_chan
    task.timing.cfg_samp_clk_timing(1000, samps_per_chan=10000)

    del task.timing.samp_quant_samp_per_chan

    assert task.timing.samp_quant_samp_per_chan == default_value


def test___timing___reset_uint64_property_with_device_context___throws_daqerror(
    task, sim_6363_device
):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.cfg_samp_clk_timing(1000, samps_per_chan=10000)

    with pytest.raises(DaqError) as e:
        del task.timing[sim_6363_device].samp_quant_samp_per_chan

    assert e.value.error_type == DAQmxErrors.M_STUDIO_OPERATION_DOES_NOT_SUPPORT_DEVICE_CONTEXT


def test___timing___set_unint64_property_out_of_range_value___throws_daqerror(
    task, sim_6363_device
):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)

    task.timing.cfg_samp_clk_timing(1000, samps_per_chan=1)

    with pytest.raises(DaqError) as e:
        _ = task.timing.samp_quant_samp_per_chan
    assert e.value.error_type == DAQmxErrors.INVALID_ATTRIBUTE_VALUE
