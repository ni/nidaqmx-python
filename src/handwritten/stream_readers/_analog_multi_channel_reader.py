from __future__ import annotations

import numpy
from nitypes.waveform import AnalogWaveform

from nidaqmx import DaqError
from nidaqmx._feature_toggles import WAVEFORM_SUPPORT, requires_feature
from nidaqmx.constants import READ_ALL_AVAILABLE, FillMode, ReallocationPolicy
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.stream_readers._channel_reader_base import ChannelReaderBase


class AnalogMultiChannelReader(ChannelReaderBase):
    """
    Reads samples from one or more analog input channels in an NI-DAQmx
    task.
    """

    def read_many_sample(
        self, data, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0
    ):
        """
        Reads one or more floating-point samples from one or more analog
        input channels in a task.

        This read method accepts a preallocated NumPy array to hold the
        samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            data (numpy.ndarray): Specifies a preallocated 2D NumPy
                array of floating-point values to hold the samples
                requested. The size of the array must be large enough to
                hold all requested samples from all channels in the
                task; otherwise, an error is thrown.

                Each row corresponds to a channel in the task. Each
                column corresponds to a sample from each channel. The
                order of the channels in the array corresponds to the
                order in which you add the channels to the task or to
                the order of the channels you specify with the
                "channels_to_read" property.

                If the size of the array is too large or the array is
                shaped incorrectly, the previous statement may not hold
                true as the samples read may not be separated into rows
                and columns properly. Set the "verify_array_shape"
                property on this channel reader object to True to
                validate that the NumPy array object is shaped properly.
                Setting this property to True may marginally adversely
                impact the performance of the method.
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
        number_of_samples_per_channel = self._task._calculate_num_samps_per_chan(
            number_of_samples_per_channel
        )

        self._verify_array(data, number_of_samples_per_channel, True, True)

        _, samps_per_chan_read = self._interpreter.read_analog_f64(
            self._handle,
            number_of_samples_per_channel,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            data,
        )

        return samps_per_chan_read

    def read_one_sample(self, data, timeout=10):
        """
        Reads a single floating-point sample from one or more analog
        input channels in a task.

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
                each channel. The size of the array must be large enough
                to hold all requested samples from the channel in the
                task; otherwise, an error is thrown.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for samples to become available. If the
                time elapses, the method returns an error and any
                samples read before the timeout elapsed. The default
                timeout is 10 seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to read the requested samples and returns an error
                if it is unable to.
        """
        self._verify_array(data, 1, True, False)

        self._interpreter.read_analog_f64(
            self._handle, 1, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

    @requires_feature(WAVEFORM_SUPPORT)
    def read_waveforms(
        self,
        waveforms: list[AnalogWaveform[numpy.float64]],
        number_of_samples_per_channel: int = READ_ALL_AVAILABLE,
        reallocation_policy: ReallocationPolicy = ReallocationPolicy.TO_GROW,
        timeout: int = 10,
    ) -> int:
        """
        Reads one or more floating-point samples from one or more analog
        input channels into a list of waveforms.

        This read method optionally accepts a preallocated list of waveforms to hold
        the samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated list of waveforms is valuable in continuous
        acquisition scenarios, where the same waveforms can be used
        repeatedly in each call to the method.

        Args:
            waveforms (list[AnalogWaveform]): Specifies a list of AnalogWaveform
                objects to use for reading samples into.
                The list must contain one waveform for each channel in the task.
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

            Indicates the number of samples acquired by each channel.
            NI-DAQmx returns a single value because this value is the
            same for all channels.
        """
        number_of_channels = self._in_stream.num_chans
        number_of_samples_per_channel = self._task._calculate_num_samps_per_chan(
            number_of_samples_per_channel
        )

        if len(waveforms) != number_of_channels:
            raise DaqError(
                f"The number of waveforms provided ({len(waveforms)}) does not match "
                f"the number of channels in the task ({number_of_channels}). Please provide "
                "one waveform for each channel.",
                DAQmxErrors.MISMATCHED_INPUT_ARRAY_SIZES,
                task_name=self._task.name,
            )

        for i, waveform in enumerate(waveforms):
            if waveform.start_index + number_of_samples_per_channel > waveform.capacity:
                if reallocation_policy == ReallocationPolicy.TO_GROW:
                    waveform.capacity = waveform.start_index + number_of_samples_per_channel
                else:
                    raise DaqError(
                        f"The waveform at index {i} does not have enough space ({waveform.capacity - waveform.start_index}) to hold "
                        f"the requested number of samples ({number_of_samples_per_channel}). Please provide larger "
                        "waveforms or adjust the number of samples requested.",
                        DAQmxErrors.READ_BUFFER_TOO_SMALL,
                        task_name=self._task.name,
                    )

        return self._interpreter.read_analog_waveforms(
            self._handle,
            number_of_samples_per_channel,
            timeout,
            waveforms,
            self._in_stream.waveform_attribute_mode,
        )
