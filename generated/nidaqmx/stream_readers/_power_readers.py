from __future__ import annotations

from nidaqmx.constants import READ_ALL_AVAILABLE, FillMode
from nidaqmx.stream_readers._channel_reader_base import ChannelReaderBase
from nidaqmx.types import PowerMeasurement


class PowerSingleChannelReader(ChannelReaderBase):
    """Reads samples from an analog input power channel in an NI-DAQmx task."""

    def read_many_sample(
        self,
        voltage_data,
        current_data,
        number_of_samples_per_channel=READ_ALL_AVAILABLE,
        timeout=10.0,
    ):
        """Reads one or more floating-point power samples from a single analog input power channel in a task.

        This read method accepts a preallocated NumPy array to hold the
        samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            voltage_data (numpy.ndarray): Specifies a preallocated 1D NumPy
                array of floating-point values to hold the voltage samples
                requested.

                Each element in the array corresponds to a sample from
                the channel. The size of the array must be large enough
                to hold all requested samples from the channel in the
                task; otherwise, an error is thrown.
            current_data (numpy.ndarray): Specifies a preallocated 1D NumPy
                array of floating-point values to hold the current samples
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
        """  # noqa: W505 - doc line too long (109 > 100 characters) (auto-generated noqa)
        number_of_samples_per_channel = self._task._calculate_num_samps_per_chan(
            number_of_samples_per_channel
        )

        self._verify_array(voltage_data, number_of_samples_per_channel, False, True)
        self._verify_array(current_data, number_of_samples_per_channel, False, True)

        _, _, samps_per_chan_read = self._interpreter.read_power_f64(
            self._handle,
            number_of_samples_per_channel,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            voltage_data,
            current_data,
        )

        return samps_per_chan_read

    def read_one_sample(self, timeout=10):
        """Reads a single floating-point power sample from a single analog input power channel in a task.

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

            Indicates a single floating-point power sample from the task.
        """  # noqa: W505 - doc line too long (105 > 100 characters) (auto-generated noqa)
        voltage, current = self._interpreter.read_power_scalar_f64(self._handle, timeout)
        return PowerMeasurement(voltage=voltage, current=current)


class PowerMultiChannelReader(ChannelReaderBase):
    """Reads samples from one or more analog input power channels in an NI-DAQmx task."""

    def read_many_sample(
        self,
        voltage_data,
        current_data,
        number_of_samples_per_channel=READ_ALL_AVAILABLE,
        timeout=10.0,
    ):
        """Reads one or more floating-point power samples from one or more analog input power channels in a task.

        This read method accepts a preallocated NumPy array to hold the
        samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            voltage_data (numpy.ndarray): Specifies a preallocated 2D NumPy
                array of floating-point values to hold the voltage samples
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
            current_data (numpy.ndarray): Specifies a preallocated 2D NumPy
                array of floating-point values to hold the current samples
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
        """  # noqa: W505 - doc line too long (113 > 100 characters) (auto-generated noqa)
        number_of_samples_per_channel = self._task._calculate_num_samps_per_chan(
            number_of_samples_per_channel
        )

        self._verify_array(voltage_data, number_of_samples_per_channel, True, True)
        self._verify_array(current_data, number_of_samples_per_channel, True, True)

        _, _, samps_per_chan_read = self._interpreter.read_power_f64(
            self._handle,
            number_of_samples_per_channel,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            voltage_data,
            current_data,
        )

        return samps_per_chan_read

    def read_one_sample(self, voltage_data, current_data, timeout=10):
        """Reads a single floating-point power sample from one or more analog input channels in a task.

        This read method accepts a preallocated NumPy array to hold the
        samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            voltage_data (numpy.ndarray): Specifies a preallocated 1D NumPy
                array of floating-point values to hold the voltage samples
                requested.

                Each element in the array corresponds to a sample from
                each channel. The size of the array must be large enough
                to hold all requested samples from the channel in the
                task; otherwise, an error is thrown.
            current_data (numpy.ndarray): Specifies a preallocated 1D NumPy
                array of floating-point values to hold the voltage samples
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
        """  # noqa: W505 - doc line too long (103 > 100 characters) (auto-generated noqa)
        self._verify_array(voltage_data, 1, True, False)
        self._verify_array(current_data, 1, True, False)

        self._interpreter.read_power_f64(
            self._handle, 1, timeout, FillMode.GROUP_BY_CHANNEL.value, voltage_data, current_data
        )


class PowerBinaryReader(ChannelReaderBase):
    """Reads binary samples from one or more analog input power channels in an NI-DAQmx task."""

    def read_many_sample(
        self,
        voltage_data,
        current_data,
        number_of_samples_per_channel=READ_ALL_AVAILABLE,
        timeout=10.0,
    ):
        """Reads one or more binary int16 samples from one or more analog input power channel in a task.

        This read method accepts a preallocated NumPy array to hold the
        samples requested, which can be advantageous for performance and
        interoperability with NumPy and SciPy.

        Passing in a preallocated array is valuable in continuous
        acquisition scenarios, where the same array can be used
        repeatedly in each call to the method.

        Args:
            voltage_data (numpy.ndarray): Specifies a preallocated 1D NumPy
                array of i16 values to hold the voltage samples requested.

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
            current_data (numpy.ndarray): Specifies a preallocated 1D NumPy
                array of i16 values to hold the current samples requested.

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
        """  # noqa: W505 - doc line too long (104 > 100 characters) (auto-generated noqa)
        number_of_samples_per_channel = self._task._calculate_num_samps_per_chan(
            number_of_samples_per_channel
        )

        self._verify_array(voltage_data, number_of_samples_per_channel, True, True)
        self._verify_array(current_data, number_of_samples_per_channel, True, True)

        _, _, samps_per_chan_read = self._interpreter.read_power_binary_i16(
            self._handle,
            number_of_samples_per_channel,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            voltage_data,
            current_data,
        )

        return samps_per_chan_read
