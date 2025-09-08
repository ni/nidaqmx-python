from __future__ import annotations

import numpy
from nidaqmx import DaqError

from nidaqmx._feature_toggles import WAVEFORM_SUPPORT, requires_feature
from nidaqmx.constants import FillMode, READ_ALL_AVAILABLE, ReallocationPolicy
from nidaqmx.error_codes import DAQmxErrors
from nitypes.waveform import AnalogWaveform

from ._channel_reader_base import ChannelReaderBase


class AnalogSingleChannelReader(ChannelReaderBase):
    """
    Reads samples from an analog input channel in an NI-DAQmx task.
    """

    def read_many_sample(
            self, data, number_of_samples_per_channel=READ_ALL_AVAILABLE,
            timeout=10.0):
        """
        Reads one or more floating-point samples from a single analog
        input channel in a task.

        This read method accepts a preallocated NumPy array to hold the
        samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            data (numpy.ndarray): Specifies a preallocated 1D NumPy
                array of floating-point values to hold the samples
                requested.

                Each element in the array corresponds to a sample from
                the channel. The size of the array must be large enough
                to hold all requested samples from the channel in the
                task; otherwise, an error is thrown.
            number_of_samples_per_channel (Optional[int]): Specifies the
                number of samples to read.

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
            int:

            Indicates the number of samples acquired by each channel.
            NI-DAQmx returns a single value because this value is the
            same for all channels.
        """
        number_of_samples_per_channel = (
            self._task._calculate_num_samps_per_chan(
                number_of_samples_per_channel))

        self._verify_array(data, number_of_samples_per_channel, False, True)

        _, samps_per_chan_read = self._interpreter.read_analog_f64(
            self._handle, number_of_samples_per_channel,
            timeout, FillMode.GROUP_BY_CHANNEL.value, data)
        
        return samps_per_chan_read

    def read_one_sample(self, timeout=10):
        """
        Reads a single floating-point sample from a single analog input
        channel in a task.

        Args:
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
            float:

            Indicates a single floating-point sample from the task.
        """
        return self._interpreter.read_analog_scalar_f64(self._handle, timeout)

    @requires_feature(WAVEFORM_SUPPORT)
    def read_waveform(
        self, 
        waveform: AnalogWaveform[numpy.float64],
        number_of_samples_per_channel: int = READ_ALL_AVAILABLE, 
        reallocation_policy: ReallocationPolicy = ReallocationPolicy.DO_NOT_REALLOCATE,
        timeout: int = 10, 
    ) -> int:
        """
        Reads one or more floating-point samples from a single analog
        input channel into a waveform.

        This read method optionally accepts a preallocated waveform to hold
        the samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated waveform is valuable in continuous
        acquisition scenarios, where the same waveform can be used
        repeatedly in each call to the method.

        Args:
            waveform (AnalogWaveform): Specifies an AnalogWaveform object
                to use for reading samples into.
            number_of_samples_per_channel (Optional[int]): Specifies the
                number of samples to read.

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
            reallocation_policy (Optional[ReallocationPolicy]): Specifies
                the reallocation policy to use when the read yields more
                samples than the current capacity of the waveform.
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
            int:

            Indicates the number of samples acquired.
        """
        number_of_samples_per_channel = (
            self._task._calculate_num_samps_per_chan(
                number_of_samples_per_channel))

        if number_of_samples_per_channel > waveform.capacity:
            if reallocation_policy == ReallocationPolicy.TO_GROW:
                waveform.capacity = number_of_samples_per_channel
            else:
                raise DaqError(
                    f'The provided waveform does not have enough space ({waveform.capacity}) to hold '
                    f'the requested number of samples ({number_of_samples_per_channel}). Please provide a larger '
                    'waveform or adjust the number of samples requested.',
                DAQmxErrors.READ_BUFFER_TOO_SMALL, task_name=self._task.name)

        waveform.sample_count = number_of_samples_per_channel

        return self._interpreter.read_analog_waveform(
            self._handle,
            number_of_samples_per_channel,
            timeout,
            waveform,
            self._in_stream.waveform_attribute_mode,
        )
