import weakref

import pytest

import nidaqmx
import nidaqmx.system
from nidaqmx.constants import ShuntCalSelect, ShuntCalSource, ShuntElementLocation
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.system.storage import PersistedChannel


@pytest.fixture
def ai_bridge_task(task: nidaqmx.Task, device) -> nidaqmx.Task:
    task.ai_channels.add_ai_bridge_chan(device.ai_physical_chans[0].name)
    return task


@pytest.fixture
def ai_strain_gage_task(task: nidaqmx.Task, device) -> nidaqmx.Task:
    task.ai_channels.add_ai_strain_gage_chan(
        device.ai_physical_chans[0].name, initial_bridge_voltage=0.002
    )
    return task


@pytest.fixture
def ai_thermocouple_task(task: nidaqmx.Task, device) -> nidaqmx.Task:
    task.ai_channels.add_ai_thrmcpl_chan(device.ai_physical_chans[0].name)
    return task


@pytest.fixture
def ai_on_demand_task(task: nidaqmx.Task, sim_6363_device: nidaqmx.system.Device) -> nidaqmx.Task:
    """Gets an AI task."""
    task.ai_channels.add_ai_voltage_chan(
        f"{sim_6363_device.name}/ai0:3", name_to_assign_to_channel="MyChannel"
    )
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
@pytest.mark.parametrize("skip_unsupported_channels", [True, False])
def test___arguments_specified___perform_bridge_offset_nulling_cal___no_errors(
    ai_bridge_task: nidaqmx.Task, skip_unsupported_channels
) -> None:
    ai_bridge_task.perform_bridge_offset_nulling_cal(
        ai_bridge_task.channels.name, skip_unsupported_channels
    )


@pytest.mark.device_name("bridgeTester")
def test___default_arguments___perform_bridge_offset_nulling_cal___no_errors(
    ai_bridge_task: nidaqmx.Task,
) -> None:
    ai_bridge_task.perform_bridge_offset_nulling_cal()


@pytest.mark.device_name("bridgeTester")
@pytest.mark.parametrize(
    "shunt_resistor_value, shunt_resistor_location, shunt_resistor_select, shunt_resistor_source, bridge_resistance, skip_unsupported_channels",
    [
        (100000, ShuntElementLocation.R1, ShuntCalSelect.A, ShuntCalSource.DEFAULT, 0.2, True),
        (100000, ShuntElementLocation.R1, ShuntCalSelect.A, ShuntCalSource.DEFAULT, 0.2, False),
        (100000, ShuntElementLocation.R3, ShuntCalSelect.A, ShuntCalSource.DEFAULT, 0.2, True),
        (100000, ShuntElementLocation.R3, ShuntCalSelect.A, ShuntCalSource.DEFAULT, 0.2, False),
    ],
)
def test___perform_bridge_shunt_cal___no_errors(
    ai_bridge_task: nidaqmx.Task,
    shunt_resistor_value,
    shunt_resistor_location,
    shunt_resistor_select,
    shunt_resistor_source,
    bridge_resistance,
    skip_unsupported_channels,
) -> None:
    try:
        ai_bridge_task.perform_bridge_shunt_cal(
            ai_bridge_task.channels.name,
            shunt_resistor_value,
            shunt_resistor_location,
            shunt_resistor_select,
            shunt_resistor_source,
            bridge_resistance,
            skip_unsupported_channels,
        )
    except nidaqmx.DaqError as e:
        if e.error_code != DAQmxErrors.SHUNT_CAL_FAILED_OUT_OF_RANGE:
            raise


@pytest.mark.device_name("bridgeTester")
def test___perform_bridge_shunt_cal_default___no_errors(
    ai_bridge_task: nidaqmx.Task,
) -> None:
    try:
        ai_bridge_task.perform_bridge_shunt_cal(ai_bridge_task.channels.name)
    except nidaqmx.DaqError as e:
        if e.error_code != DAQmxErrors.SHUNT_CAL_FAILED_OUT_OF_RANGE:
            raise


@pytest.mark.device_name("bridgeTester")
@pytest.mark.parametrize(
    "shunt_resistor_value, shunt_resistor_location, shunt_resistor_select, shunt_resistor_source, skip_unsupported_channels",
    [
        (100000, ShuntElementLocation.R1, ShuntCalSelect.A, ShuntCalSource.DEFAULT, False),
        (100000, ShuntElementLocation.R1, ShuntCalSelect.A, ShuntCalSource.DEFAULT, False),
        (100000, ShuntElementLocation.R3, ShuntCalSelect.A, ShuntCalSource.DEFAULT, True),
        (100000, ShuntElementLocation.R3, ShuntCalSelect.A, ShuntCalSource.DEFAULT, False),
    ],
)
def test___perform_strain_shunt_cal___no_errors(
    ai_strain_gage_task: nidaqmx.Task,
    shunt_resistor_value,
    shunt_resistor_location,
    shunt_resistor_select,
    shunt_resistor_source,
    skip_unsupported_channels,
) -> None:
    try:
        ai_strain_gage_task.perform_strain_shunt_cal(
            ai_strain_gage_task.channels.name,
            shunt_resistor_value,
            shunt_resistor_location,
            shunt_resistor_select,
            shunt_resistor_source,
            skip_unsupported_channels,
        )
    except nidaqmx.DaqError as e:
        if e.error_code != DAQmxErrors.SHUNT_CAL_FAILED_OUT_OF_RANGE:
            raise


@pytest.mark.device_name("bridgeTester")
def test___perform_strain_shunt_cal_default___no_errors(
    ai_strain_gage_task: nidaqmx.Task,
) -> None:
    try:
        ai_strain_gage_task.perform_strain_shunt_cal(ai_strain_gage_task.channels.name)
    except nidaqmx.DaqError as e:
        if e.error_code != DAQmxErrors.SHUNT_CAL_FAILED_OUT_OF_RANGE:
            raise


@pytest.mark.device_name("cDAQ1Mod2")
@pytest.mark.parametrize("skip_unsupported_channels", [True, False])
def test___arguments_specified___perform_thrmcpl_lead_offset_nulling_cal___no_errors(
    ai_thermocouple_task: nidaqmx.Task, skip_unsupported_channels
) -> None:
    ai_thermocouple_task.perform_thrmcpl_lead_offset_nulling_cal(
        ai_thermocouple_task.channels.name, skip_unsupported_channels
    )


@pytest.mark.device_name("cDAQ1Mod2")
def test___default_arguments___perform_thrmcpl_lead_offset_nulling_cal___no_errors(
    ai_thermocouple_task: nidaqmx.Task,
) -> None:
    ai_thermocouple_task.perform_thrmcpl_lead_offset_nulling_cal()


def test___on_demand_task_is_done___is_task_done___returns_true(ai_on_demand_task: nidaqmx.Task):
    assert ai_on_demand_task.is_task_done()
    ai_on_demand_task.start()
    ai_on_demand_task.wait_until_done()

    assert ai_on_demand_task.is_task_done()


def test___task___add_global_channels___adds_to_channel_names(task: nidaqmx.Task):
    persisted_channel = PersistedChannel("VoltageTesterChannel")
    persisted_channel2 = PersistedChannel("VoltageTesterChannel2")

    task.add_global_channels([persisted_channel, persisted_channel2])

    assert task.channel_names == [persisted_channel.name, persisted_channel2.name]


def test___task___create_weakref___succeeds(task: nidaqmx.Task):
    ref = weakref.ref(task)
    task2 = ref()
    assert task is task2
