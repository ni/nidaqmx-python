import pytest

import nidaqmx
from nidaqmx.error_codes import DAQmxErrors

@pytest.fixture
def ai_bridge_task(task: nidaqmx.Task, device) -> nidaqmx.Task:
    task.ai_channels.add_ai_bridge_chan(device.ai_physical_chans[0].name)
    return task

@pytest.fixture
def ai_strain_gage_task(task: nidaqmx.Task, device) -> nidaqmx.Task:
    task.ai_channels.add_ai_strain_gage_chan(device.ai_physical_chans[0].name, initial_bridge_voltage=0.002)
    return task

@pytest.mark.library_only(reason="Default gRPC initialization behavior is auto (create or attach)")
def test___task___create_task_with_same_name___raises_duplicate_task(init_kwargs):
    task1 = nidaqmx.Task("MyTask1", **init_kwargs)

    with task1, pytest.raises(nidaqmx.DaqError) as exc_info:
        _ = nidaqmx.Task("MyTask1", **init_kwargs)

    assert exc_info.value.error_code == DAQmxErrors.DUPLICATE_TASK


def test___tasks_with_different_names___compare___not_equal(generate_task):
    task1 = generate_task("MyTask1")
    task2 = generate_task("MyTask2")

    assert task1 != task2


def test___tasks_with_different_names___hash___not_equal(generate_task):
    task1 = generate_task("MyTask1")
    task2 = generate_task("MyTask2")

    assert hash(task1) != hash(task2)

@pytest.mark.device_name("bridgeTester")
@pytest.mark.parametrize(
    "shunt_resistor_value, shunt_resistor_location, bridge_resistance, skip_unsupported_channels",
    [
        (100000, 12465, 0.2, True),
        (100000, 12465, 0.2, False),
        (100000, 12467, 0.2, True),
        (100000, 12467, 0.2, False),
    ]
)
def test___perform_bridge_shunt_cal___no_errors(
        ai_bridge_task: nidaqmx.Task, shunt_resistor_value,
        shunt_resistor_location, bridge_resistance,
        skip_unsupported_channels)-> None:

    ai_bridge_task.perform_bridge_shunt_cal(
        ai_bridge_task.channels.name, shunt_resistor_value, 
        shunt_resistor_location, bridge_resistance, 
        skip_unsupported_channels)

@pytest.mark.device_name("bridgeTester")
@pytest.mark.parametrize(
    "shunt_resistor_value, shunt_resistor_location, shunt_resistor_select, shunt_resistor_source, bridge_resistance, skip_unsupported_channels",
    [
        (100000, 12465, 0, 0, 0.2, True),
        (100000, 12465, 0, 0, 0.2, False),
        (100000, 12467, 0, 0, 0.2, True),
        (100000, 12467, 0, 0, 0.2, False),
    ]
)
def test___perform_bridge_shunt_cal_ex___no_errors(
        ai_bridge_task: nidaqmx.Task, shunt_resistor_value,
        shunt_resistor_location, shunt_resistor_select, 
        shunt_resistor_source, bridge_resistance,
        skip_unsupported_channels)-> None:

    ai_bridge_task.perform_bridge_shunt_cal_ex(
        ai_bridge_task.channels.name, shunt_resistor_value, 
        shunt_resistor_location, shunt_resistor_select,  
        shunt_resistor_source, bridge_resistance, 
        skip_unsupported_channels)

@pytest.mark.device_name("bridgeTester")
@pytest.mark.parametrize(
    "shunt_resistor_value, shunt_resistor_location, skip_unsupported_channels",
    [
        (100000, 12465, True),
        (100000, 12465, False),
        (100000, 12467, True),
        (100000, 12467, False),
    ],
)
def test___perform_strain_shunt_cal___no_errors(ai_strain_gage_task: nidaqmx.Task, shunt_resistor_value, shunt_resistor_location, skip_unsupported_channels)-> None:
    ai_strain_gage_task.perform_strain_shunt_cal(ai_strain_gage_task.channels.name, shunt_resistor_value, shunt_resistor_location,skip_unsupported_channels)

@pytest.mark.device_name("bridgeTester")
@pytest.mark.parametrize(
    "shunt_resistor_value, shunt_resistor_location, shunt_resistor_select, shunt_resistor_source, skip_unsupported_channels",
    [
        (100000, 12465, 0, 0, True),
        (100000, 12465, 0, 0, False),
        (100000, 12467, 0, 0, True),
        (100000, 12467, 0, 0, False),
    ],
)
def test___perform_strain_shunt_cal_ex___no_errors(ai_strain_gage_task: nidaqmx.Task, shunt_resistor_value, shunt_resistor_location, shunt_resistor_select, shunt_resistor_source, skip_unsupported_channels)-> None:
    ai_strain_gage_task.perform_strain_shunt_cal_ex(ai_strain_gage_task.channels.name, shunt_resistor_value, shunt_resistor_location,shunt_resistor_select, shunt_resistor_source, skip_unsupported_channels)
