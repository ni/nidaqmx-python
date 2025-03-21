from __future__ import annotations

import threading
import warnings
from enum import Enum
from typing import List, Tuple, Union

import numpy
from nidaqmx import utils
from nidaqmx.task.channels._channel import Channel
from nidaqmx.task._export_signals import ExportSignals
from nidaqmx.task._in_stream import InStream
from nidaqmx.task._timing import Timing
from nidaqmx.task.triggering._triggers import Triggers
from nidaqmx.task._out_stream import OutStream
from nidaqmx.task.collections._ai_channel_collection import (
    AIChannelCollection)
from nidaqmx.task.collections._ao_channel_collection import (
    AOChannelCollection)
from nidaqmx.task.collections._ci_channel_collection import (
    CIChannelCollection)
from nidaqmx.task.collections._co_channel_collection import (
    COChannelCollection)
from nidaqmx.task.collections._di_channel_collection import (
    DIChannelCollection)
from nidaqmx.task.collections._do_channel_collection import (
    DOChannelCollection)
from nidaqmx.constants import (
    AcquisitionType, ChannelType, FillMode, UsageTypeAI, UsageTypeCI, EveryNSamplesEventType,
    READ_ALL_AVAILABLE, UsageTypeCO, _Save, ShuntCalSelect, ShuntCalSource, ShuntElementLocation)
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.errors import (
    DaqError, DaqResourceWarning)
from nidaqmx.system.device import _DeviceAlternateConstructor
from nidaqmx.types import CtrFreq, CtrTick, CtrTime, PowerMeasurement
from nidaqmx.utils import unflatten_channel_string, flatten_channel_string

__all__ = ['Task']


class UnsetNumSamplesSentinel:
    pass


class UnsetAutoStartSentinel:
    pass


NUM_SAMPLES_UNSET = UnsetNumSamplesSentinel()
AUTO_START_UNSET = UnsetAutoStartSentinel()

del UnsetNumSamplesSentinel
del UnsetAutoStartSentinel


class Task:
    """
    Represents a DAQmx Task.
    """
    __slots__ = ('_handle', '_close_on_exit', '_saved_name', '_grpc_options', '_event_handlers', '_interpreter',
                 '_ai_channels', '_ao_channels', '_ci_channels', '_co_channels', '_di_channels', '_do_channels',
                 '_export_signals', '_in_stream', '_timing', '_triggers', '_out_stream', '_event_handler_lock',
                 '__weakref__')

    def __init__(self, new_task_name='', *, grpc_options=None):
        """
        Creates a DAQmx task.

        Args:
            new_task_name (Optional[str]): Specifies the name to assign to
                the task.

                If you use this method in a loop and specify a name for the
                task, you must use the DAQmx Clear Task method within the loop
                after you are finished with the task. Otherwise, NI-DAQmx
                attempts to create multiple tasks with the same name, which
                results in an error.

            grpc_options (Optional[:class:`~nidaqmx.GrpcSessionOptions`]): Specifies
                the gRPC session options.
        """
        # Initialize the fields that __del__ accesses so it doesn't crash when __init__ raises an exception.
        self._handle = None
        self._close_on_exit = False
        self._saved_name = new_task_name  # _initialize sets this to the name assigned by DAQmx.
        self._grpc_options = grpc_options
        self._event_handlers = {}

        if grpc_options and not (
            grpc_options.session_name == "" or grpc_options.session_name == new_task_name
        ):
            raise DaqError(
                f'Unsupported session name: "{grpc_options.session_name}". If a session name is specified, it must match the task name.',
                DAQmxErrors.UNKNOWN,
                task_name=new_task_name)

        self._interpreter = utils._select_interpreter(grpc_options)
        self._handle, self._close_on_exit = self._interpreter.create_task(new_task_name)

        self._initialize(self._handle, self._interpreter)

    def __del__(self):
        if self._handle is not None and self._close_on_exit and self._grpc_options is None:
            warnings.warn(
                'Task of name "{}" was not explicitly closed before it was '
                'destructed. Resources on the task device may still be '
                'reserved.'.format(self._saved_name),
                DaqResourceWarning
            )
        elif (
            self._grpc_options is not None
            and self._event_handlers
        ):
            warnings.warn(
                'Task of name "{}" was not explicitly closed before it was '
                'destructed. Event handlers may still be active.'.format(self._saved_name),
                DaqResourceWarning
            )

    def __enter__(self):
        return self

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._handle == other._handle
        return False

    def __exit__(self, type, value, traceback):
        if self._close_on_exit:
            self.close()

    def __hash__(self):
        return self._interpreter.hash_task_handle(self._handle)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return f'Task(name={self._saved_name})'

    @property
    def name(self):
        """
        str: Indicates the name of the task.
        """
        val = self._interpreter.get_task_attribute_string(self._handle, 0x1276)
        return val

    @property
    def channels(self):
        """
        :class:`nidaqmx.task.channels.Channel`: Specifies
            a channel object that represents the entire list of virtual
            channels in this task.
        """
        return Channel._factory(
            self._handle, flatten_channel_string(self.channel_names), self._interpreter)

    @property
    def channel_names(self):
        """
        List[str]: Indicates the names of all virtual channels in the task.
        """
        val = self._interpreter.get_task_attribute_string(self._handle, 0x1273)
        return unflatten_channel_string(val)

    @property
    def number_of_channels(self):
        """
        int: Indicates the number of virtual channels in the task.
        """
        val = self._interpreter.get_task_attribute_uint32(self._handle, 0x2181)
        return val

    @property
    def devices(self):
        """
        List[:class:`nidaqmx.system.device.Device`]: Indicates a list
            of Device objects representing all the devices in the task.
        """
        val = self._interpreter.get_task_attribute_string(self._handle, 0x230e)
        return [_DeviceAlternateConstructor(v, self._interpreter) for v in
                unflatten_channel_string(val)]

    @property
    def number_of_devices(self):
        """
        int: Indicates the number of devices in the task.
        """
        val = self._interpreter.get_task_attribute_uint32(self._handle, 0x29ba)
        return val

    @property
    def ai_channels(self) -> AIChannelCollection:
        """
        Gets the collection of analog input channels for this task.
        """
        return self._ai_channels

    @property
    def ao_channels(self) -> AOChannelCollection:
        """
        Gets the collection of analog output channels for this task.
        """
        return self._ao_channels

    @property
    def ci_channels(self) -> CIChannelCollection:
        """
        Gets the collection of counter input channels for this task.
        """
        return self._ci_channels

    @property
    def co_channels(self) -> COChannelCollection:
        """
        Gets the collection of counter output channels for this task.
        """
        return self._co_channels

    @property
    def di_channels(self) -> DIChannelCollection:
        """
        Gets the collection of digital input channels for this task.
        """
        return self._di_channels

    @property
    def do_channels(self) -> DOChannelCollection:
        """
        Gets the collection of digital output channels for this task.
        """
        return self._do_channels

    @property
    def export_signals(self) -> ExportSignals:
        """
        Gets the exported signal configurations for the task.
        """
        return self._export_signals

    @property
    def in_stream(self) -> InStream:
        """
        Gets the read configurations for the task.
        """
        return self._in_stream

    @property
    def out_stream(self) -> OutStream:
        """
        Gets the write configurations for the task.
        """
        return self._out_stream

    @property
    def timing(self) -> Timing:
        """
        Gets the timing configurations for the task.
        """
        return self._timing

    @property
    def triggers(self) -> Triggers:
        """
        Gets the trigger configurations for the task.
        """
        return self._triggers

    def _initialize(self, task_handle, interpreter):
        """
        Instantiates and populates various attributes used by this task.

        Args:
            task_handle (TaskHandle): Specifies the handle for this task.
        """
        # Saved name is used in self.close() to throw graceful error on
        # double closes.
        self._saved_name = self.name

        self._ai_channels = AIChannelCollection(task_handle, interpreter)
        self._ao_channels = AOChannelCollection(task_handle, interpreter)
        self._ci_channels = CIChannelCollection(task_handle, interpreter)
        self._co_channels = COChannelCollection(task_handle, interpreter)
        self._di_channels = DIChannelCollection(task_handle, interpreter)
        self._do_channels = DOChannelCollection(task_handle, interpreter)
        self._export_signals = ExportSignals(task_handle, interpreter)
        self._in_stream = InStream(self, interpreter)
        self._timing = Timing(task_handle, interpreter)
        self._triggers = Triggers(task_handle, interpreter)
        self._out_stream = OutStream(self, interpreter)

        self._event_handler_lock = threading.Lock()

    def _calculate_num_samps_per_chan(self, num_samps_per_chan):
        """
        Calculates the actual number of samples per channel to read.

        This method is necessary because the number of samples per channel
        can be set to NUM_SAMPLES_UNSET or -1, where each value entails a
        different method of calculating the actual number of samples per
        channel to read.

        Args:
            num_samps_per_chan (int): Specifies the number of samples per
                channel.
        """
        if num_samps_per_chan is NUM_SAMPLES_UNSET:
            return 1
        elif num_samps_per_chan == READ_ALL_AVAILABLE:
            acq_type = self.timing.samp_quant_samp_mode

            if (acq_type == AcquisitionType.FINITE and
                    not self.in_stream.read_all_avail_samp):
                return self.timing.samp_quant_samp_per_chan
            else:
                return self.in_stream.avail_samp_per_chan
        else:
            return num_samps_per_chan

    def add_global_channels(self, global_channels):
        """
        Adds global virtual channels from MAX to the given task.

        Args:
            global_channels (List[nidaqmx.system.storage.persisted_channel.PersistedChannel]):
                Specifies the channels to add to the task.

                These channels must be valid channels available from MAX.
                If you pass an invalid channel, NI-DAQmx returns an error.
                This value is ignored if it is empty.
        """
        channels = flatten_channel_string([g._name for g in global_channels])

        self._interpreter.add_global_chans_to_task(self._handle, channels)

    def close(self):
        """
        Clears the task.

        Before clearing, this method aborts the task, if necessary,
        and releases any resources the task reserved. You cannot use a task
        after you clear it unless you recreate the task.

        If you create a DAQmx Task object within a loop, use this method
        within the loop after you are finished with the task to avoid
        allocating unnecessary memory.
        """
        if self._handle is None:
            warnings.warn(
                'Attempted to close NI-DAQmx task of name "{}" but task was '
                'already closed.'.format(self._saved_name), DaqResourceWarning)
            return

        first_exception = None
        try:
            self._interpreter.clear_task(self._handle)
        except Exception as ex:
            first_exception = first_exception or ex
        self._handle = None

        with self._event_handler_lock:
            event_handlers = self._event_handlers
            self._event_handlers = {}

        for event_handler in event_handlers.values():
            try:
                event_handler.close()
            except Exception as ex:
                first_exception = first_exception or ex

        if first_exception:
            raise first_exception

    def control(self, action):
        """
        Alters the state of a task according to the action you specify.

        Args:
            action (nidaqmx.constants.TaskMode): Specifies how to alter
                the task state.
        """
        self._interpreter.task_control(self._handle, action.value)

    def is_task_done(self):
        """
        Queries the status of the task and indicates if it completed
        execution. Use this function to ensure that the specified
        operation is complete before you stop the task.

        Returns:
            bool:

            Indicates if the measurement or generation completed.
        """
        is_task_done = self._interpreter.is_task_done(self._handle)

        return is_task_done

    def perform_bridge_offset_nulling_cal(self, channel="", skip_unsupported_channels=False):
        """
        Perform a bridge offset nulling calibration on the channels in the task.

        If the task measures both bridge-based sensors and non-bridge-based sensors,
        use the channels input to specify the names of the channels that measure
        bridge-based sensors.

        Args:
            channel: is a subset of virtual channels in the task that you want to calibrate.
                Use this input if you do not want to calibrate all the channels in the task or
                if some channels in the task have open thermocouple detection disabled.
                If the input is empty, this VI attempts to calibrate all virtual channels in the task.

            skip_unsupported_channels: specifies whether or not to skip channels that do not
                support calibration.
                If skip unsupported channels is TRUE, this VI calibrates only supported channels.
                If FALSE, this VI calibrates the channels specified by channels. The default is FALSE.
        """

        self._interpreter.perform_bridge_offset_nulling_cal_ex(
            self._handle, channel, skip_unsupported_channels)

    def perform_strain_shunt_cal(
            self, channel="", shunt_resistor_value=100000,
            shunt_resistor_location=ShuntElementLocation.R3, shunt_resistor_select=ShuntCalSelect.A,
            shunt_resistor_source=ShuntCalSource.DEFAULT, skip_unsupported_channels=False):
        """
        Perform shunt calibration for the specified channels using a strain
        gage sensor.

        Refer to the calibration procedure for your module for detailed
        calibration instructions.

        Args:
            channel: Specifies a subset of virtual channels in the task that you
                want to calibrate. Use this input if you do not want to calibrate
                all the channels in the task or if some channels in the task measure
                non-bridge-based sensors. If the input is empty, this method attempts
                to calibrate all virtual channels in the task.
            shunt_resistor_value: Specifies the shunt resistance in ohms.
            shunt_resistor_location: Specifies the location of the shunt resistor.
            shunt_resistor_select: Specifies which shunt calibration switch to enable.
            shunt_resistor_source: Specifies which shunt to use.
            skip_unsupported_channels: Specifies whether or not to skip channels that
                do not support calibration. If skip_unsupported_channels is True, this
                method calibrates only supported channels. If False, this method calibrates
                the channels specified by channels. The default is False.
        """
        self._interpreter.perform_strain_shunt_cal_ex(
            self._handle, channel, shunt_resistor_value,
            shunt_resistor_location.value, shunt_resistor_select.value,
            shunt_resistor_source.value, skip_unsupported_channels)

    def perform_bridge_shunt_cal(
            self, channel="", shunt_resistor_value=100000,
            shunt_resistor_location=ShuntElementLocation.R3, shunt_resistor_select=ShuntCalSelect.A,
            shunt_resistor_source=ShuntCalSource.DEFAULT, bridge_resistance=120,
            skip_unsupported_channels=False):
        """
        Perform shunt calibration for the specified channels using a bridge sensor.

        Refer to the calibration procedure for your module for detailed
        calibration instructions.

        Args:
            channel: Specifies a subset of virtual channels in the task that you
                want to calibrate. Use this input if you do not want to calibrate
                all the channels in the task or if some channels in the task measure
                non-bridge-based sensors. If the input is empty, this method attempts
                to calibrate all virtual channels in the task.
            shunt_resistor_value: Specifies the shunt resistance in ohms.
            shunt_resistor_location: Specifies the location of the shunt resistor.
            shunt_resistor_select: Specifies which shunt calibration switch to enable.
            shunt_resistor_source: Specifies which shunt to use.
            bridge_resistance: Specifies the bridge resistance in ohms. A value of -1
                means to use the nominal bridge resistance specified when you created
                the virtual channel.
            skip_unsupported_channels: Specifies whether or not to skip channels that
                do not support calibration. If skip_unsupported_channels is True, this
                method calibrates only supported channels. If False, this method calibrates
                the channels specified by channels. The default is False.
        """
        self._interpreter.perform_bridge_shunt_cal_ex(
            self._handle, channel, shunt_resistor_value,
            shunt_resistor_location.value, shunt_resistor_select.value,
            shunt_resistor_source.value, bridge_resistance,
            skip_unsupported_channels)

    def perform_thrmcpl_lead_offset_nulling_cal(self, channel="", skip_unsupported_channels=False):
        """
        Perform thermocouple lead offset nulling calibration on the channels in the task.

        This is to compensate for offsets introduced by open thermocouple detection.
        Keep the measured temperature as constant as possible while performing this
        adjustment.

        Args:
            channel: is a subset of virtual channels in the task that you want to calibrate.
                Use this input if you do not want to calibrate all the channels in the task or
                if some channels in the task have open thermocouple detection disabled.
                If the input is empty, this VI attempts to calibrate all virtual channels in the task.

            skip_unsupported_channels: specifies whether or not to skip channels that do not
                support calibration.
                If skip unsupported channels is TRUE, this VI calibrates only supported channels.
                If FALSE, this VI calibrates the channels specified by channels. The default is FALSE.
        """

        self._interpreter.perform_thrmcpl_lead_offset_nulling_cal(
            self._handle, channel, skip_unsupported_channels)

    def read(self, number_of_samples_per_channel=NUM_SAMPLES_UNSET,
             timeout=10.0):
        """
        Reads samples from the task or virtual channels you specify.

        This read method is dynamic, and is capable of inferring an appropriate
        return type based on these factors:
        - The channel type of the task.
        - The number of channels to read.
        - The number of samples per channel.

        The data type of the samples returned is independently determined by
        the channel type of the task.

        For digital input measurements, the data type of the samples returned
        is determined by the line grouping format of the digital lines.
        If the line grouping format is set to "one channel for all lines", the
        data type of the samples returned is int. If the line grouping
        format is set to "one channel per line", the data type of the samples
        returned is boolean.

        If you do not set the number of samples per channel, this method
        assumes one sample was requested. This method then returns either a
        scalar (1 channel to read) or a list (N channels to read).

        If you set the number of samples per channel to ANY value (even 1),
        this method assumes multiple samples were requested. This method then
        returns either a list (1 channel to read) or a list of lists (N
        channels to read).

        Args:
            number_of_samples_per_channel (Optional[int]): Specifies the
                number of samples to read. If this input is not set,
                assumes samples to read is 1. Conversely, if this input
                is set, assumes there are multiple samples to read.

                If you set this input to nidaqmx.constants.
                READ_ALL_AVAILABLE, NI-DAQmx determines how many samples
                to read based on if the task acquires samples
                continuously or acquires a finite number of samples.

                If the task acquires samples continuously and you set
                this input to nidaqmx.constants.READ_ALL_AVAILABLE, this
                method reads all the samples currently available in the
                buffer.

                If the task acquires a finite number of samples and you
                set this input to nidaqmx.constants.READ_ALL_AVAILABLE,
                the method waits for the task to acquire all requested
                samples, then reads those samples. If you set the
                "read_all_avail_samp" property to True, the method reads
                the samples currently available in the buffer and does
                not wait for the task to acquire all requested samples.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for samples to become available. If the
                time elapses, the method returns an error and any
                samples read before the timeout elapsed. The default
                timeout is 10 seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to read the requested samples and returns an error
                if it is unable to.
        Returns:
            dynamic:

            The samples requested in the form of a scalar, a list, or a
            list of lists. See method docstring for more info.

            NI-DAQmx scales the data to the units of the measurement,
            including any custom scaling you apply to the channels. Use a
            DAQmx Create Channel method to specify these units.

        Example:
            >>> task = Task()
            >>> task.ai_channels.add_ai_voltage_chan('Dev1/ai0:3')
            >>> data = task.read()
            >>> type(data)
            <type 'list'>
            >>> type(data[0])
            <type 'float'>
        """
        channels_to_read = self.in_stream.channels_to_read
        number_of_channels = len(channels_to_read.channel_names)
        read_chan_type = channels_to_read.chan_type

        num_samples_not_set = (number_of_samples_per_channel is
                               NUM_SAMPLES_UNSET)

        number_of_samples_per_channel = self._calculate_num_samps_per_chan(
            number_of_samples_per_channel)

        # Determine the array shape and size to create
        if number_of_channels > 1:
            if not num_samples_not_set:
                array_shape: tuple[int, ...] = (
                    number_of_channels, number_of_samples_per_channel
                )
            else:
                array_shape = (number_of_channels,)
        else:
            array_shape = (number_of_samples_per_channel,)

        if read_chan_type == ChannelType.ANALOG_INPUT:
            if any(chan.ai_meas_type == UsageTypeAI.POWER for chan in channels_to_read):
                return self._read_power(
                    array_shape, number_of_channels, number_of_samples_per_channel, timeout
                )
            else:
                data: numpy.typing.NDArray = numpy.zeros(array_shape, dtype=numpy.float64)
                _, samples_read = self._interpreter.read_analog_f64(
                    self._handle, number_of_samples_per_channel, timeout,
                    FillMode.GROUP_BY_CHANNEL.value, data)

        elif (read_chan_type == ChannelType.DIGITAL_INPUT or
                read_chan_type == ChannelType.DIGITAL_OUTPUT):
            if self.in_stream.di_num_booleans_per_chan == 1:
                data = numpy.zeros(array_shape, dtype=bool)
                _, samples_read, _ = self._interpreter.read_digital_lines(
                    self._handle, number_of_samples_per_channel, timeout,
                    FillMode.GROUP_BY_CHANNEL.value, data)
            else:
                data = numpy.zeros(array_shape, dtype=numpy.uint32)
                _, samples_read = self._interpreter.read_digital_u32(
                    self._handle, number_of_samples_per_channel, timeout,
                    FillMode.GROUP_BY_CHANNEL.value, data)

        elif read_chan_type == ChannelType.COUNTER_INPUT:
            meas_type = channels_to_read.ci_meas_type

            if meas_type in [UsageTypeCI.PULSE_FREQ, UsageTypeCI.PULSE_TIME, UsageTypeCI.PULSE_TICKS]:
                return self._read_ctr_pulse(
                    array_shape,
                    meas_type,
                    number_of_channels,
                    number_of_samples_per_channel,
                    num_samples_not_set,
                    timeout
                )

            else:
                data = numpy.zeros(array_shape, dtype=numpy.float64)

                _, samples_read = self._interpreter.read_counter_f64_ex(
                    self._handle, number_of_samples_per_channel, timeout,
                    FillMode.GROUP_BY_CHANNEL.value, data)
        else:
            raise DaqError(
                'Read failed, because there are no channels in this task from '
                'which data can be read.',
                DAQmxErrors.READ_NO_INPUT_CHANS_IN_TASK,
                task_name=self.name)

        if num_samples_not_set and array_shape == (1,):
            return data.tolist()[0]

        if samples_read != number_of_samples_per_channel:
            if number_of_channels > 1:
                return data[:,:samples_read].tolist()
            else:
                return data[:samples_read].tolist()

        return data.tolist()

    def _read_ctr_pulse(
        self,
        array_shape: tuple[int, ...],
        meas_type: UsageTypeCI,
        number_of_channels: int,
        number_of_samples_per_channel: int,
        num_samples_not_set: bool,
        timeout: float,
    ) -> CtrFreq | CtrTick | CtrTime | list[CtrFreq] | list[CtrTick] | list[CtrTime]:
        if meas_type == UsageTypeCI.PULSE_FREQ:
            frequencies = numpy.zeros(array_shape, dtype=numpy.float64)
            duty_cycles = numpy.zeros(array_shape, dtype=numpy.float64)

            _, _, samples_read = self._interpreter.read_ctr_freq(
                self._handle, number_of_samples_per_channel, timeout,
                FillMode.GROUP_BY_CHANNEL.value, frequencies, duty_cycles)

            data: list[CtrFreq] | list[CtrTick] | list[CtrTime] = [
                CtrFreq(freq=f, duty_cycle=d) for f, d in zip(frequencies, duty_cycles)
            ]

        elif meas_type == UsageTypeCI.PULSE_TIME:
            high_times = numpy.zeros(array_shape, dtype=numpy.float64)
            low_times = numpy.zeros(array_shape, dtype=numpy.float64)

            _, _, samples_read = self._interpreter.read_ctr_time(
                self._handle, number_of_samples_per_channel, timeout,
                FillMode.GROUP_BY_CHANNEL.value, high_times, low_times)
            data = [CtrTime(high_time=h, low_time=l) for h, l in zip(high_times, low_times)]

        elif meas_type == UsageTypeCI.PULSE_TICKS:
            high_ticks = numpy.zeros(array_shape, dtype=numpy.uint32)
            low_ticks = numpy.zeros(array_shape, dtype=numpy.uint32)

            _, _ , samples_read = self._interpreter.read_ctr_ticks(
                self._handle, number_of_samples_per_channel, timeout,
                FillMode.GROUP_BY_CHANNEL.value, high_ticks, low_ticks)
            data = [CtrTick(high_tick=h, low_tick=l) for h, l in zip(high_ticks, low_ticks)]

        else:
            assert False, f"{meas_type} is not a counter pulse measurement type."

        if num_samples_not_set and array_shape == (1,):
            return data[0]

        # Counter pulse measurements should not have N channel versions.
        #
        # https://github.com/ni/nidaqmx-python/issues/498 - Missing support for
        # multi-channel counter reads in stream_readers and task
        if samples_read != number_of_samples_per_channel:
            assert number_of_channels == 1
            return data[:samples_read]

        return data

    def _read_power(
        self,
        array_shape: tuple[int, ...],
        number_of_channels: int,
        number_of_samples_per_channel: int,
        timeout: float,
    ) -> PowerMeasurement | list[PowerMeasurement] | list[list[PowerMeasurement]]:
        voltages = numpy.zeros(array_shape, dtype=numpy.float64)
        currents = numpy.zeros(array_shape, dtype=numpy.float64)

        _, _, samples_read = self._interpreter.read_power_f64(
            self._handle, number_of_samples_per_channel, timeout,
            FillMode.GROUP_BY_CHANNEL.value, voltages, currents)

        if number_of_channels > 1:
            if number_of_samples_per_channel == 1:
                # n channel, 1 sample
                return [
                    PowerMeasurement(voltage=v, current=i)
                    for v, i in zip(voltages, currents)
                ]
            else:
                # n channel, n samples
                return [
                    [
                        PowerMeasurement(voltage=v, current=i)
                        for v, i in zip(voltages[channel_index], currents[channel_index])
                    ]
                    for channel_index in range(number_of_channels)
                ]
        else:
            if number_of_samples_per_channel == 1:
                # 1 channel, 1 sample
                return PowerMeasurement(voltage=voltages[0], current=currents[0])
            else:
                # 1 channel, n samples
                return [
                    PowerMeasurement(voltage=v, current=i)
                    for v, i in zip(voltages, currents)
                ][:samples_read]

    def register_done_event(self, callback_method):
        """
        Registers a callback function to receive an event when a task stops due
        to an error or when a finite acquisition task or finite generation task
        completes execution. A Done event does not occur when a task is stopped
        explicitly, such as by calling DAQmx Stop Task.

        Args:
            callback_method (function): Specifies the function that you want
                DAQmx to call when the event occurs. The function you pass in
                this parameter must have the following prototype:

                >>> def callback(task_handle, status, callback_data):
                >>>     return 0

                Upon entry to the callback, the task_handle parameter contains
                the handle to the task on which the event occurred. The status
                parameter contains the status of the task when the event
                occurred. If the status value is negative, it indicates an
                error. If the status value is zero, it indicates no error.
                If the status value is positive, it indicates a warning. The
                callbackData parameter contains the value you passed in the
                callbackData parameter of this function.

                Passing None for this parameter unregisters the event callback
                function.
        """
        if callback_method is not None:
            # If the event is already registered, the interpreter should raise DaqError with code
            # DAQmxErrors.DONE_EVENT_ALREADY_REGISTERED.
            event_handler = self._interpreter.register_done_event(self._handle, 0, callback_method, None)
            with self._event_handler_lock:
                assert _TaskEventType.DONE not in self._event_handlers, "Event already registered."
                self._event_handlers[_TaskEventType.DONE] = event_handler
        else:
            self._interpreter.unregister_done_event(self._handle)
            with self._event_handler_lock:
                event_handler = self._event_handlers.pop(_TaskEventType.DONE, None)
            if event_handler is not None:
                event_handler.close()  # may raise an exception

    def register_every_n_samples_acquired_into_buffer_event(
            self, sample_interval, callback_method):
        """
        Registers a callback function to receive an event when the specified
        number of samples is written from the device to the buffer. This
        function only works with devices that support buffered tasks.

        When you stop a task explicitly any pending events are discarded. For
        example, if you call DAQmx Stop Task then you do not receive any
        pending events.

        Args:
            sample_interval (int): Specifies the number of samples after
                which each event should occur.
            callback_method (function): Specifies the function that you want
                DAQmx to call when the event occurs. The function you pass in
                this parameter must have the following prototype:

                >>> def callback(task_handle, every_n_samples_event_type,
                >>>         number_of_samples, callback_data):
                >>>     return 0

                Upon entry to the callback, the task_handle parameter contains
                the handle to the task on which the event occurred. The
                every_n_samples_event_type parameter contains the
                EveryNSamplesEventType.ACQUIRED_INTO_BUFFER value. The
                number_of_samples parameter contains the value you passed in
                the sample_interval parameter of this function. The
                callback_data parameter contains the value you passed in the
                callback_data parameter of this function.

                Passing None for this parameter unregisters the event callback
                function.
        """
        if callback_method is not None:
            # If the event is already registered, the interpreter should raise DaqError with code
            # DAQmxErrors.EVERY_N_SAMPS_ACQ_INTO_BUFFER_EVENT_ALREADY_REGISTERED.
            event_handler = self._interpreter.register_every_n_samples_event(
                self._handle, EveryNSamplesEventType.ACQUIRED_INTO_BUFFER.value,
                sample_interval, 0, callback_method, None)
            with self._event_handler_lock:
                assert _TaskEventType.EVERY_N_SAMPLES_ACQUIRED_INTO_BUFFER not in self._event_handlers, "Event already registered."
                self._event_handlers[_TaskEventType.EVERY_N_SAMPLES_ACQUIRED_INTO_BUFFER] = event_handler
        else:
            self._interpreter.unregister_every_n_samples_event(
                self._handle, EveryNSamplesEventType.ACQUIRED_INTO_BUFFER.value)
            with self._event_handler_lock:
                event_handler = self._event_handlers.pop(_TaskEventType.EVERY_N_SAMPLES_ACQUIRED_INTO_BUFFER, None)
            if event_handler is not None:
                event_handler.close()  # may raise an exception

    def register_every_n_samples_transferred_from_buffer_event(
            self, sample_interval, callback_method):
        """
        Registers a callback function to receive an event when the specified
        number of samples is written from the buffer to the device. This
        function only works with devices that support buffered tasks.

        When you stop a task explicitly any pending events are discarded. For
        example, if you call DAQmx Stop Task then you do not receive any
        pending events.

        Args:
            sample_interval (int): Specifies the number of samples after
                which each event should occur.
            callback_method (function): Specifies the function that you want
                DAQmx to call when the event occurs. The function you pass in
                this parameter must have the following prototype:

                >>> def callback(task_handle, every_n_samples_event_type,
                >>>         number_of_samples, callback_data):
                >>>     return 0

                Upon entry to the callback, the task_handle parameter contains
                the handle to the task on which the event occurred. The
                every_n_samples_event_type parameter contains the
                EveryNSamplesEventType.TRANSFERRED_FROM_BUFFER value. The
                number_of_samples parameter contains the value you passed in
                the sample_interval parameter of this function. The
                callback_data parameter contains the value you passed in the
                callback_data parameter of this function.

                Passing None for this parameter unregisters the event callback
                function.
        """
        if callback_method is not None:
            # If the event is already registered, the interpreter should raise DaqError with code
            # DAQmxErrors.EVERY_N_SAMPS_TRANSFERRED_FROM_BUFFER_EVENT_ALREADY_REGISTERED.
            event_handler = self._interpreter.register_every_n_samples_event(
                self._handle, EveryNSamplesEventType.TRANSFERRED_FROM_BUFFER.value,
                sample_interval, 0, callback_method, None)
            with self._event_handler_lock:
                assert _TaskEventType.EVERY_N_SAMPLES_TRANSFERRED_FROM_BUFFER not in self._event_handlers, "Event already registered."
                self._event_handlers[_TaskEventType.EVERY_N_SAMPLES_TRANSFERRED_FROM_BUFFER] = event_handler
        else:
            self._interpreter.unregister_every_n_samples_event(
                self._handle, EveryNSamplesEventType.TRANSFERRED_FROM_BUFFER.value)
            with self._event_handler_lock:
                event_handler = self._event_handlers.pop(_TaskEventType.EVERY_N_SAMPLES_TRANSFERRED_FROM_BUFFER, None)
            if event_handler is not None:
                event_handler.close()  # may raise an exception

    def register_signal_event(self, signal_type, callback_method):
        """
        Registers a callback function to receive an event when the specified
        hardware event occurs.

        When you stop a task explicitly any pending events are discarded. For
        example, if you call DAQmx Stop Task then you do not receive any
        pending events.

        Args:
            signal_type (nidaqmx.constants.Signal): Specifies the type of
                signal for which you want to receive results.
            callback_method (function): Specifies the function that you want
                DAQmx to call when the event occurs. The function you pass in
                this parameter must have the following prototype:

                >>> def callback(task_handle, signal_type, callback_data):
                >>>     return 0

                Upon entry to the callback, the task_handle parameter contains
                the handle to the task on which the event occurred. The
                signal_type parameter contains the integer value you passed in
                the signal_type parameter of this function. The callback_data
                parameter contains the value you passed in the callback_data
                parameter of this function.

                Passing None for this parameter unregisters the event callback
                function.
        """
        if callback_method is not None:
            # If the event is already registered, the interpreter should raise DaqError with code
            # DAQmxErrors.SIGNAL_EVENT_ALREADY_REGISTERED.
            event_handler = self._interpreter.register_signal_event(
                self._handle, signal_type.value, 0, callback_method, None)
            with self._event_handler_lock:
                assert _TaskEventType.SIGNAL not in self._event_handlers, "Event already registered."
                self._event_handlers[_TaskEventType.SIGNAL] = event_handler
        else:
            self._interpreter.unregister_signal_event(self._handle, signal_type.value)
            with self._event_handler_lock:
                event_handler = self._event_handlers.pop(_TaskEventType.SIGNAL, None)
            if event_handler is not None:
                event_handler.close()  # may raise an exception

    def save(self, save_as="", author="", overwrite_existing_task=False,
             allow_interactive_editing=True, allow_interactive_deletion=True):
        """
        Saves this task and any local channels it contains to MAX.

        This function does not save global channels. Use the DAQmx Save
        Global Channel function to save global channels.

        Args:
            save_as (Optional[str]): Is the name to save the task,
                global channel, or custom scale as. If you do not
                specify a value for this input, NI-DAQmx uses the name
                currently assigned to the task, global channel, or
                custom scale.
            author (Optional[str]): Is a name to store with the task,
                global channel, or custom scale.
            overwrite_existing_task (Optional[bool]): Specifies whether to
                overwrite a task of the same name if one is already saved in
                MAX. If this input is False and a task of the same name is
                already saved in MAX, this function returns an error.
            allow_interactive_editing (Optional[bool]): Specifies whether to
                allow the task, global channel, or custom scale to be edited
                in the DAQ Assistant. If allow_interactive_editing is True,
                the DAQ Assistant must support all task or global channel
                settings.
            allow_interactive_deletion (Optional[bool]): Specifies whether
                to allow the task, global channel, or custom scale to be
                deleted through MAX.
        """
        options = 0
        if overwrite_existing_task:
            options |= _Save.OVERWRITE.value
        if allow_interactive_editing:
            options |= _Save.ALLOW_INTERACTIVE_EDITING.value
        if allow_interactive_deletion:
            options |= _Save.ALLOW_INTERACTIVE_DELETION.value

        self._interpreter.save_task(self._handle, save_as, author, options)

    def start(self):
        """
        Transitions the task to the running state to begin the measurement
        or generation. Using this method is required for some applications and
        is optional for others.

        If you do not use this method, a measurement task starts automatically
        when the DAQmx Read method runs. The autostart input of the DAQmx Write
        method determines if a generation task starts automatically when the
        DAQmx Write method runs.

        If you do not use the DAQmx Start Task method and the DAQmx Stop Task
        method when you use the DAQmx Read method or the DAQmx Write method
        multiple times, such as in a loop, the task starts and stops
        repeatedly. Starting and stopping a task repeatedly reduces the
        performance of the application.
        """
        self._interpreter.start_task(self._handle)

    def stop(self):
        """
        Stops the task and returns it to the state the task was in before the
        DAQmx Start Task method ran or the DAQmx Write method ran with the
        autostart input set to TRUE.

        If you do not use the DAQmx Start Task method and the DAQmx Stop Task
        method when you use the DAQmx Read method or the DAQmx Write method
        multiple times, such as in a loop, the task starts and stops
        repeatedly. Starting and stopping a task repeatedly reduces the
        performance of the application.
        """
        self._interpreter.stop_task(self._handle)

    def wait_for_valid_timestamp(self, timestamp_event, timeout=10.0):
        """
        Wait until the specified timestamp has a value.

        Use this method to ensure the timestamp has a valid value to prevent an error when querying a timestamp value.

        Args:
            timestamp_event(nidaqmx.constants.TimestampEvent): Specifies the timestamp type to wait on.
            timeout (float): Specifies the maximum amount of time in
                seconds to wait for a valid timestamp.
                This method returns an error if the time elapses. The
                default is 10. If you set timeout (sec) to
                nidaqmx.WAIT_INFINITELY, the method waits indefinitely.

        Returns:
            datetime:

            The timestamp value of timestamp_event.
        """
        return self._interpreter.wait_for_valid_timestamp(self._handle, timestamp_event.value, timeout)

    def wait_until_done(self, timeout=10.0):
        """
        Waits for the measurement or generation to complete.

        Use this method to ensure that the specified operation is complete
        before you stop the task.

        Args:
            timeout (Optional[float]): Specifies the maximum amount of time in
                seconds to wait for the measurement or generation to complete.
                This method returns an error if the time elapses. The
                default is 10. If you set timeout (sec) to
                nidaqmx.WAIT_INFINITELY, the method waits indefinitely. If you
                set timeout (sec) to 0, the method checks once and returns
                an error if the measurement or generation is not done.
        """
        self._interpreter.wait_until_task_done(self._handle, timeout)

    def _raise_invalid_num_lines_error(
            self, num_lines_expected, num_lines_in_data):
        raise DaqError(
            'Specified read or write operation failed, because the number '
            'of lines in the data for a channel does not match the number '
            'of lines in the channel.\n\n'
            'If you are using boolean data, make sure the array dimension '
            'for lines in the data matches the number of lines in the '
            'channel.\n\n'
            'Number of Lines Per Channel in Task: {}\n'
            'Number of Lines Per Channel in Data: {}'
            .format(num_lines_expected, num_lines_in_data),
            DAQmxErrors.NUM_LINES_MISMATCH_IN_READ_OR_WRITE,
            task_name=self.name)

    def _raise_invalid_write_num_chans_error(
            self, number_of_channels, number_of_channels_in_data):

        raise DaqError(
            'Write cannot be performed, because the number of channels in the '
            'data does not match the number of channels in the task.\n\n'
            'When writing, supply data for all channels in the task. '
            'Alternatively, modify the task to contain the same number of '
            'channels as the data written.\n\n'
            'Number of Channels in Task: {}\n'
            'Number of Channels in Data: {}'
            .format(number_of_channels, number_of_channels_in_data),
            DAQmxErrors.WRITE_NUM_CHANS_MISMATCH, task_name=self.name)

    def write(self, data, auto_start=AUTO_START_UNSET, timeout=10.0):
        """
        Writes samples to the task or virtual channels you specify.

        This write method is dynamic, and is capable of accepting the
        samples to write in the various forms for most operations:

        - Scalar: Single sample for 1 channel.
        - List/1D numpy.ndarray: Multiple samples for 1 channel or 1
          sample for multiple channels.
        - List of lists/2D numpy.ndarray: Multiple samples for multiple
          channels.

        The data type of the samples passed in must be appropriate for
        the channel type of the task.

        For counter output pulse operations, this write method only
        accepts samples in these forms:

        - Scalar CtrFreq, CtrTime, CtrTick (from nidaqmx.types):
          Single sample for 1 channel.
        - List of CtrFreq, CtrTime, CtrTick (from nidaqmx.types):
          Multiple samples for 1 channel or 1 sample for multiple
          channels.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            data (dynamic): Contains the samples to write to the task.

                The data you write must be in the units of the
                generation, including any custom scales. Use the DAQmx
                Create Channel methods to specify these units.
            auto_start (Optional[bool]): Specifies if this method
                automatically starts the task if you did not explicitly
                start it with the DAQmx Start Task method.

                The default value of this parameter depends on whether
                you specify one sample or many samples to write to each
                channel. If one sample per channel was specified, the
                default value is True. If multiple samples per channel
                were specified, the default value is False.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.
        Returns:
            int:

            Specifies the actual number of samples this method
            successfully wrote.
        """
        channels_to_write = self.channels
        number_of_channels = len(channels_to_write.channel_names)
        write_chan_type = channels_to_write.chan_type

        element = None
        if number_of_channels == 1:
            if isinstance(data, list):
                if isinstance(data[0], list):
                    self._raise_invalid_write_num_chans_error(
                        number_of_channels, len(data))

                number_of_samples_per_channel = len(data)
                element = data[0]

            elif isinstance(data, numpy.ndarray):
                if len(data.shape) == 2:
                    self._raise_invalid_write_num_chans_error(
                        number_of_channels, data.shape[0])

                number_of_samples_per_channel = len(data)
                element = data[0]

            else:
                number_of_samples_per_channel = 1
                element = data

        else:
            if isinstance(data, list):
                if len(data) != number_of_channels:
                    self._raise_invalid_write_num_chans_error(
                        number_of_channels, len(data))

                if isinstance(data[0], list):
                    number_of_samples_per_channel = len(data[0])
                    element = data[0][0]
                else:
                    number_of_samples_per_channel = 1
                    element = data[0]

            elif isinstance(data, numpy.ndarray):
                if data.shape[0] != number_of_channels:
                    self._raise_invalid_write_num_chans_error(
                        number_of_channels, data.shape[0])

                if len(data.shape) == 2:
                    number_of_samples_per_channel = data.shape[1]
                    element = data[0][0]
                else:
                    number_of_samples_per_channel = 1
                    element = data[0]

            else:
                self._raise_invalid_write_num_chans_error(
                    number_of_channels, 1)

        if auto_start is AUTO_START_UNSET:
            if number_of_samples_per_channel > 1:
                auto_start = False
            else:
                auto_start = True

        if write_chan_type == ChannelType.ANALOG_OUTPUT:
            data = numpy.asarray(data, dtype=numpy.float64)
            return self._interpreter.write_analog_f64(
                self._handle, number_of_samples_per_channel, auto_start,
                timeout, FillMode.GROUP_BY_CHANNEL.value, data)

        elif write_chan_type == ChannelType.DIGITAL_OUTPUT:
            if self.out_stream.do_num_booleans_per_chan == 1:
                if (not isinstance(element, bool) and
                        not isinstance(element, numpy.bool_)):
                    raise DaqError(
                        'Write failed, because this write method only accepts '
                        'boolean samples when there is one digital line per '
                        'channel in a task.\n\n'
                        'Requested sample type: {}'.format(type(element)),
                        DAQmxErrors.UNKNOWN, task_name=self.name)

                data = numpy.asarray(data, dtype=bool)
                return self._interpreter.write_digital_lines(
                    self._handle, number_of_samples_per_channel,
                    auto_start, timeout, FillMode.GROUP_BY_CHANNEL.value, data)
            else:
                if (not isinstance(element, int) and
                        not isinstance(element, numpy.uint32)):
                    raise DaqError(
                        'Write failed, because this write method only accepts '
                        'unsigned 32-bit integer samples when there are '
                        'multiple digital lines per channel in a task.\n\n'
                        'Requested sample type: {}'.format(type(element)),
                        DAQmxErrors.UNKNOWN, task_name=self.name)

                data = numpy.asarray(data, dtype=numpy.uint32)
                return self._interpreter.write_digital_u32(
                    self._handle, number_of_samples_per_channel,
                    auto_start, timeout, FillMode.GROUP_BY_CHANNEL.value, data)

        elif write_chan_type == ChannelType.COUNTER_OUTPUT:
            output_type = channels_to_write.co_output_type

            if number_of_samples_per_channel == 1:
                data = [data]

            if output_type == UsageTypeCO.PULSE_FREQUENCY:
                if not all(isinstance(sample, CtrFreq) for sample in data):
                    raise TypeError(f"Output type {output_type} requires samples of type CtrFreq.")

                frequencies = numpy.array([sample.freq for sample in data], dtype=numpy.float64)
                duty_cycles = numpy.array([sample.duty_cycle for sample in data], dtype=numpy.float64)

                return self._interpreter.write_ctr_freq(
                    self._handle, number_of_samples_per_channel, auto_start, timeout,
                    FillMode.GROUP_BY_CHANNEL.value, frequencies, duty_cycles)

            elif output_type == UsageTypeCO.PULSE_TIME:
                if not all(isinstance(sample, CtrTime) for sample in data):
                    raise TypeError(f"Output type {output_type} requires samples of type CtrTime.")

                high_times = numpy.array([sample.high_time for sample in data], dtype=numpy.float64)
                low_times = numpy.array([sample.low_time for sample in data], dtype=numpy.float64)

                return self._interpreter.write_ctr_time(
                    self._handle, number_of_samples_per_channel, auto_start, timeout,
                    FillMode.GROUP_BY_CHANNEL.value, high_times, low_times)

            elif output_type == UsageTypeCO.PULSE_TICKS:
                if not all(isinstance(sample, CtrTick) for sample in data):
                    raise TypeError(f"Output type {output_type} requires samples of type CtrTick.")

                high_ticks = numpy.array([sample.high_tick for sample in data], dtype=numpy.uint32)
                low_ticks = numpy.array([sample.low_tick for sample in data], dtype=numpy.uint32)

                return self._interpreter.write_ctr_ticks(
                    self._handle, number_of_samples_per_channel, auto_start, timeout,
                    FillMode.GROUP_BY_CHANNEL.value, high_ticks, low_ticks)

            else:
                raise DaqError(
                    "Write failed, because the output type is not supported.\n\n"
                    f"Output type: {output_type}",
                    DAQmxErrors.UNKNOWN,
                    task_name=self.name,
                )

        else:
            raise DaqError(
                'Write failed, because there are no output channels in this '
                'task to which data can be written.',
                DAQmxErrors.WRITE_NO_OUTPUT_CHANS_IN_TASK,
                task_name=self.name)


class _TaskAlternateConstructor(Task):
    """
    Provide an alternate constructor for the Task object.

    This is a private API used to instantiate a Task with an existing task handle and interpreter.
    """
    # Setting __slots__ avoids TypeError: __class__ assignment: 'Base' object layout differs from 'Derived'.
    __slots__ = ()

    def __init__(self, task_handle, interpreter, close_on_exit):
        """
        Args:
            task_handle: Specifies the task handle from which to create a
                Task object.
            interpreter: Specifies the interpreter instance.
            close_on_exit: Specifies whether the task's context manager closes the task.

        """
        # Initialize the fields that __del__ accesses so it doesn't crash when _initialize raises an exception.
        self._handle = task_handle
        self._close_on_exit = close_on_exit
        self._saved_name = ""  # _initialize sets this to the name assigned by DAQmx.
        self._grpc_options = getattr(interpreter, "_grpc_options", None)
        self._event_handlers = {}

        self._interpreter = interpreter
        self._initialize(self._handle, self._interpreter)

        # Use meta-programming to change the type of this object to Task,
        # so the user isn't confused when doing introspection.
        self.__class__ = Task  # type: ignore[assignment]


class _TaskEventType(Enum):
    """Internal enum for task event bookkeeping."""
    DONE = 1
    EVERY_N_SAMPLES_ACQUIRED_INTO_BUFFER = 2
    EVERY_N_SAMPLES_TRANSFERRED_FROM_BUFFER = 3
    SIGNAL = 4