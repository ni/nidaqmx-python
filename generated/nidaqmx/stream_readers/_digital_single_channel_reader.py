from __future__ import annotations

from typing import Any

import numpy
from nitypes.waveform import DigitalWaveform

from nidaqmx import DaqError
from nidaqmx._feature_toggles import WAVEFORM_SUPPORT, requires_feature
from nidaqmx.constants import READ_ALL_AVAILABLE, FillMode, ReallocationPolicy
from nidaqmx.error_codes import DAQmxErrors
from nidaqmx.stream_readers._channel_reader_base import ChannelReaderBase


class DigitalSingleChannelReader(ChannelReaderBase):
    """Reads samples from a digital input channel in an NI-DAQmx task."""

    def read_many_sample_port_byte(
        self, data, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0
    ):
        """Reads one or more 8-bit unsigned integer samples from a single digital input channel in a task.

        Use this method for devices with up to 8 lines per port.

        This read method accepts a preallocated NumPy array to hold
        the samples requested, which can be advantageous for performance
        and interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            data (numpy.ndarray): Specifies a preallocated 1D NumPy
                array of 8-bit unsigned integer values to hold the
                samples requested.

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
        """  # noqa: W505 - doc line too long (106 > 100 characters) (auto-generated noqa)
        number_of_samples_per_channel = self._task._calculate_num_samps_per_chan(
            number_of_samples_per_channel
        )

        self._verify_array(data, number_of_samples_per_channel, False, True)

        _, samps_per_chan_read = self._interpreter.read_digital_u8(
            self._handle,
            number_of_samples_per_channel,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            data,
        )

        return samps_per_chan_read

    def read_many_sample_port_uint16(
        self, data, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0
    ):
        """Reads one or more 16-bit unsigned integer samples from a single digital input channel in a task.

        Use this method for devices with up to 16 lines per port.

        This read method accepts a preallocated NumPy array to hold
        the samples requested, which can be advantageous for performance
        and interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            data (numpy.ndarray): Specifies a preallocated 1D NumPy
                array of 16-bit unsigned integer values to hold the
                samples requested.

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
        """  # noqa: W505 - doc line too long (107 > 100 characters) (auto-generated noqa)
        number_of_samples_per_channel = self._task._calculate_num_samps_per_chan(
            number_of_samples_per_channel
        )

        self._verify_array(data, number_of_samples_per_channel, False, True)

        _, samps_per_chan_read = self._interpreter.read_digital_u16(
            self._handle,
            number_of_samples_per_channel,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            data,
        )

        return samps_per_chan_read

    def read_many_sample_port_uint32(
        self, data, number_of_samples_per_channel=READ_ALL_AVAILABLE, timeout=10.0
    ):
        """Reads one or more 32-bit unsigned integer samples from a single digital input channel in a task.

        Use this method for devices with up to 32 lines per port.

        This read method accepts a preallocated NumPy array to hold
        the samples requested, which can be advantageous for performance
        and interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            data (numpy.ndarray): Specifies a preallocated 1D NumPy
                array of 32-bit unsigned integer values to hold the
                samples requested.

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
        """  # noqa: W505 - doc line too long (107 > 100 characters) (auto-generated noqa)
        number_of_samples_per_channel = self._task._calculate_num_samps_per_chan(
            number_of_samples_per_channel
        )

        self._verify_array(data, number_of_samples_per_channel, False, True)

        _, samps_per_chan_read = self._interpreter.read_digital_u32(
            self._handle,
            number_of_samples_per_channel,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            data,
        )

        return samps_per_chan_read

    def read_one_sample_multi_line(self, data, timeout=10):
        """Reads a single boolean sample from a single digital input channel in a task.

        The channel can contain multiple digital lines.

        This read method accepts a preallocated NumPy array to hold the
        samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            data (numpy.ndarray): Specifies a preallocated 1D NumPy
                array of boolean values to hold the samples requested.

                Each element in the array corresponds to a sample from
                a line in the channel. The size of the array must be
                large enough to hold all requested samples from the
                channel in the task; otherwise, an error is thrown.
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
        self._verify_array_digital_lines(data, False, True)

        _, samps_per_chan_read, num_bytes_per_samp = self._interpreter.read_digital_lines(
            self._handle, 1, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

    def read_one_sample_one_line(self, timeout=10):
        """Reads a single boolean sample from a single digital input channel in a task.

        The channel can contain only one digital line.

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
            bool:

            Indicates a single boolean sample from the task.
        """
        data = numpy.zeros(1, dtype=bool)
        _, samps_per_chan_read, num_bytes_per_samp = self._interpreter.read_digital_lines(
            self._handle, 1, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

        return bool(data[0])

    def read_one_sample_port_byte(self, timeout=10):
        """Reads a single 8-bit unsigned integer sample from a single digital input channel in a task.

        Use this method for devices with up to 8 lines per port.

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
            int:

            Indicates a single 8-bit unsigned integer sample from the
            task.
        """  # noqa: W505 - doc line too long (102 > 100 characters) (auto-generated noqa)
        data = numpy.zeros(1, dtype=numpy.uint8)
        _, samps_per_chan_read = self._interpreter.read_digital_u8(
            self._handle, 1, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

        return int(data[0])

    def read_one_sample_port_uint16(self, timeout=10):
        """Reads a single 16-bit unsigned integer sample from a single digital input channel in a task.

        Use this method for devices with up to 16 lines per port.

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
            int:

            Indicates a single 16-bit unsigned integer sample from the
            task.
        """  # noqa: W505 - doc line too long (103 > 100 characters) (auto-generated noqa)
        data = numpy.zeros(1, dtype=numpy.uint16)
        _, samps_per_read_chan = self._interpreter.read_digital_u16(
            self._handle, 1, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

        return int(data[0])

    def read_one_sample_port_uint32(self, timeout=10):
        """Reads a single 32-bit unsigned integer sample from a single digital input channel in a task.

        Use this method for devices with up to 32 lines per port.

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
            int:

            Indicates a single 32-bit unsigned integer sample from the
            task.
        """  # noqa: W505 - doc line too long (103 > 100 characters) (auto-generated noqa)
        return self._interpreter.read_digital_scalar_u32(self._handle, timeout)

    @requires_feature(WAVEFORM_SUPPORT)
    def read_waveform(
        self,
        waveform: DigitalWaveform[Any],
        number_of_samples_per_channel: int = READ_ALL_AVAILABLE,
        reallocation_policy: ReallocationPolicy = ReallocationPolicy.TO_GROW,
        timeout: float = 10.0,
    ) -> int:
        """Reads one or more digital samples from a single digital input channel into a waveform.

        Args:
            waveform (DigitalWaveform[Any]): Specifies a
                preallocated DigitalWaveform object to hold the samples
                requested.
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
        number_of_samples_per_channel = self._task._calculate_num_samps_per_chan(
            number_of_samples_per_channel
        )

        if waveform.start_index + number_of_samples_per_channel > waveform.capacity:
            if reallocation_policy == ReallocationPolicy.TO_GROW:
                waveform.capacity = waveform.start_index + number_of_samples_per_channel
            else:
                raise DaqError(
                    f"The waveform does not have enough space ({waveform.capacity - waveform.start_index}) to hold "
                    f"the requested number of samples ({number_of_samples_per_channel}). Please "
                    "provide a larger waveform or adjust the number of samples requested.",
                    DAQmxErrors.READ_BUFFER_TOO_SMALL,
                    task_name=self._task.name,
                )

        return self._interpreter.read_digital_waveform(
            self._handle,
            number_of_samples_per_channel,
            timeout,
            waveform,
            self._in_stream.waveform_attribute_mode,
        )
