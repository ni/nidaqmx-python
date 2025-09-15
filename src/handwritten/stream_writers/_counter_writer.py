from nidaqmx.constants import FillMode
from nidaqmx.stream_writers._channel_writer_base import (
    AUTO_START_UNSET,
    ChannelWriterBase,
)


class CounterWriter(ChannelWriterBase):
    """Writes samples to a counter output channel in an NI-DAQmx task."""

    def write_many_sample_pulse_frequency(self, frequencies, duty_cycles, timeout=10.0):
        """Writes one or more pulse samples in terms of frequency to a single counter output channel in a task.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            frequencies (numpy.ndarray): Contains a 1D NumPy array of
                floating-point values that holds the frequency portion
                of the pulse samples to write to the task. Each element
                of the array corresponds to a sample to write.
            duty_cycles (numpy.ndarray): Contains a 1D NumPy array of
                floating-point values that holds the duty cycle portion
                of the pulse samples to write to the task. Each element
                of the array corresponds to a sample to write.
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
        """  # noqa: W505 - doc line too long (111 > 100 characters) (auto-generated noqa)
        self._verify_array(frequencies, False, True)
        self._verify_array(duty_cycles, False, True)

        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else False

        return self._interpreter.write_ctr_freq(
            self._handle,
            frequencies.shape[0],
            auto_start,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            frequencies,
            duty_cycles,
        )

    def write_many_sample_pulse_ticks(self, high_ticks, low_ticks, timeout=10.0):
        """Writes one or more pulse samples in terms of ticks to a single counter output channel in a task.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            high_ticks (numpy.ndarray): Contains a 1D NumPy array of
                32-bit unsigned integer values that holds the high ticks
                portion of the pulse samples to write to the task. Each
                element of the array corresponds to a sample to write.
            low_ticks (numpy.ndarray): Contains a 1D NumPy array of
                32-bit unsigned integer values that holds the low ticks
                portion of the pulse samples to write to the task. Each
                element of the array corresponds to a sample to write.
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
        """  # noqa: W505 - doc line too long (107 > 100 characters) (auto-generated noqa)
        self._verify_array(high_ticks, False, True)
        self._verify_array(low_ticks, False, True)

        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else False

        return self._interpreter.write_ctr_ticks(
            self._handle,
            high_ticks.shape[0],
            auto_start,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            high_ticks,
            low_ticks,
        )

    def write_many_sample_pulse_time(self, high_times, low_times, timeout=10.0):
        """Writes one or more pulse samples in terms of time to a single counter output channel in a task.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            high_times (numpy.ndarray): Contains a 1D NumPy array of
                floating-point values that holds the high time portion
                of the pulse samples to write to the task. Each element
                of the array corresponds to a sample to write.
            low_times (numpy.ndarray): Contains a 1D NumPy array of
                floating-point values that holds the low time portion
                of the pulse samples to write to the task. Each element
                of the array corresponds to a sample to write.
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
        """  # noqa: W505 - doc line too long (106 > 100 characters) (auto-generated noqa)
        self._verify_array(high_times, False, True)
        self._verify_array(low_times, False, True)

        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else False

        return self._interpreter.write_ctr_time(
            self._handle,
            high_times.shape[0],
            auto_start,
            timeout,
            FillMode.GROUP_BY_CHANNEL.value,
            high_times,
            low_times,
        )

    def write_one_sample_pulse_frequency(self, frequency, duty_cycle, timeout=10):
        """Writes a new pulse frequency and duty cycle to a single counter output channel in a task.

        Args:
            frequency (float): Specifies at what frequency to generate
                pulses.
            duty_cycle (float): Specifies the width of the pulse divided
                by the pulse period. NI-DAQmx uses this ratio combined
                with frequency to determine pulse width and the interval
                between pulses.
            auto_start (Optional[bool]): Specifies if this method
                automatically starts the task if you did not explicitly
                start it with the DAQmx Start Task method.
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
        """
        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else True

        return self._interpreter.write_ctr_freq_scalar(
            self._handle, auto_start, timeout, frequency, duty_cycle
        )

    def write_one_sample_pulse_ticks(self, high_ticks, low_ticks, timeout=10):
        """Writes a new pulse high tick count and low tick count to a single counter output channel in a task.

        Args:
            high_ticks (float): Specifies the number of ticks the pulse
                is high.
            low_ticks (float): Specifies the number of ticks the pulse
                is low.
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
        """  # noqa: W505 - doc line too long (110 > 100 characters) (auto-generated noqa)
        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else True

        return self._interpreter.write_ctr_ticks_scalar(
            self._handle, auto_start, timeout, high_ticks, low_ticks
        )

    def write_one_sample_pulse_time(self, high_time, low_time, timeout=10):
        """Writes a new pulse high time and low time to a single counter output channel in a task.

        Args:
            high_time (float): Specifies the amount of time the pulse
                is high.
            low_time (float): Specifies the amount of time the pulse
                is low.
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
        """
        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else True

        return self._interpreter.write_ctr_time_scalar(
            self._handle, auto_start, timeout, high_time, low_time
        )
