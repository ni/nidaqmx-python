import pytest

from nidaqmx.constants import SampleTimingType
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.errors import DaqError


def test___ai_task___set_valid_value_to_unsupported_property___unsupported_error_raised(
    task,
    sim_6363_device,
):
    task.ai_channels.add_ai_voltage_chan(sim_6363_device.ai_physical_chans[0].name)
    task.timing.samp_timing_type = SampleTimingType.SAMPLE_CLOCK

    with pytest.raises(DaqError) as exc_info:
        task.out_stream.output_buf_size = 2000

    assert exc_info.value.error_code == DAQmxErrors.ATTRIBUTE_NOT_SUPPORTED_IN_TASK_CONTEXT
