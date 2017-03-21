from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import numpy
from nidaqmx import DaqError
from nidaqmx._task_modules.write_functions import (
    _write_analog_f_64, _write_analog_scalar_f_64, _write_binary_i_16,
    _write_binary_i_32, _write_binary_u_16, _write_binary_u_32,
    _write_ctr_freq, _write_ctr_ticks, _write_ctr_time, _write_ctr_freq_scalar,
    _write_ctr_ticks_scalar, _write_ctr_time_scalar, _write_digital_u_8,
    _write_digital_u_16, _write_digital_u_32, _write_digital_lines,
    _write_digital_scalar_u_32)
from nidaqmx.error_codes import DAQmxErrors

__all__ = ['AnalogSingleChannelWriter', 'AnalogMultiChannelWriter',
           'AnalogUnscaledWriter', 'CounterWriter',
           'DigitalSingleChannelWriter', 'DigitalMultiChannelWriter']


class UnsetAutoStartSentinel(object):
    pass


AUTO_START_UNSET = UnsetAutoStartSentinel()

del UnsetAutoStartSentinel


class ChannelWriterBase(object):
    """
    Defines base class for all NI-DAQmx stream writers.
    """

    def __init__(self, task_out_stream, auto_start=AUTO_START_UNSET):
        """
        Args:
            task_out_stream: Specifies the output stream associated with
                an NI-DAQmx task which to write samples.
            auto_start (Optional[bool]): Specifies if the write method
                automatically starts the task if you did not explicitly
                start it with the DAQmx Start Task method.
                
                If you do not specify a value for this parameter, 
                NI-DAQmx determines its value based on the type of write
                method used. If you use a one sample write method, the
                value is True; conversely, if you use a many sample 
                write method, the value is False.
        """
        self._out_stream = task_out_stream
        self._task = task_out_stream._task
        self._handle = task_out_stream._task._handle

        self._verify_array_shape = True
        self._auto_start = auto_start

    @property
    def auto_start(self):
        """
        bool: Specifies if the write method automatically starts the 
            task if you did not explicitly start it with the DAQmx Start
            Task method.

            If you do not specify a value for this parameter, NI-DAQmx 
            determines its value based on the type of write method used. 
            If you use a one sample write method, its value is True; 
            conversely, if you use a many sample write method, its value
            is False.
        """
        return self._auto_start

    @auto_start.setter
    def auto_start(self, val):
        self._auto_start = val

    @auto_start.deleter
    def auto_start(self):
        self._auto_start = AUTO_START_UNSET

    @property
    def verify_array_shape(self):
        """
        bool: Indicates whether the size and shape of the user-defined
            NumPy arrays passed to read methods are verified. Defaults
            to True when this object is instantiated.

            Setting this property to True may marginally adversely
            impact the performance of read methods.
        """
        return self._verify_array_shape

    @verify_array_shape.setter
    def verify_array_shape(self, val):
        self._verify_array_shape = val

    def _verify_array(self, data, is_many_chan, is_many_samp):
        """
        Verifies that the shape of the specified NumPy array can be used
        with the specified write method type, if the
        "verify_array_shape" property is set to True.

        Args:
            data (numpy.ndarray): Specifies the NumPy array to verify.
            is_many_chan (bool): Specifies if the write method is a many
                channel version.
            is_many_samp (bool): Specifies if the write method is a many
                sample version.
        """
        if not self._verify_array_shape:
            return

        channels_to_write = self._task.channels
        number_of_channels = len(channels_to_write.channel_names)

        expected_num_dimensions = None
        if is_many_chan:
            if is_many_samp:
                expected_num_dimensions = 2
            else:
                expected_num_dimensions = 1

            if data.shape[0] != number_of_channels:
                self._task._raise_invalid_write_num_chans_error(
                    number_of_channels, data.shape[0])
        else:
            if is_many_samp:
                expected_num_dimensions = 1

        if expected_num_dimensions is not None:
            self._raise_error_if_invalid_write_dimensions(
                expected_num_dimensions, len(data.shape))

    def _verify_array_digital_lines(
            self, data, is_many_chan, is_many_line):
        """
        Verifies that the shape of the specified NumPy array can be used
        to read samples from the current task which contains one or more
        channels that have one or more digital lines per channel, if the
        "verify_array_shape" property is set to True.

        Args:
            data (numpy.ndarray): Specifies the NumPy array to verify.
            is_many_chan (bool): Specifies if the write method is a
                many channel version.
            is_many_line (bool): Specifies if the write method is a
                many line version.
        """
        if not self._verify_array_shape:
            return

        channels_to_write = self._task.channels
        number_of_channels = len(channels_to_write.channel_names)
        number_of_lines = self._out_stream.do_num_booleans_per_chan

        expected_num_dimensions = None
        if is_many_chan:
            if data.shape[0] != number_of_channels:
                self._task._raise_invalid_write_num_chans_error(
                    number_of_channels, data.shape[0])

            if is_many_line:
                expected_num_dimensions = 2
                if data.shape[1] != number_of_lines:
                    self._task._raise_invalid_num_lines_error(
                        number_of_lines, data.shape[1])
            else:
                expected_num_dimensions = 1
        else:
            if is_many_line:
                expected_num_dimensions = 1
                if data.shape[0] != number_of_lines:
                    self._task._raise_invalid_num_lines_error(
                        number_of_lines, data.shape[0])

        if expected_num_dimensions is not None:
            self._raise_error_if_invalid_write_dimensions(
                expected_num_dimensions, len(data.shape))

    def _raise_error_if_invalid_write_dimensions(
            self, num_dimensions_expected, num_dimensions_in_data):
        if num_dimensions_expected != num_dimensions_in_data:
            raise DaqError(
                'Write cannot be performed because the NumPy array passed '
                'into this function is not shaped correctly. '
                'You must pass in a NumPy array of the correct number of '
                'dimensions based on the write method you use.\n\n'
                'No. of dimensions of NumPy Array provided: {0}\n'
                'No. of dimensions of NumPy Array required: {1}'
                .format(num_dimensions_in_data, num_dimensions_expected),
                DAQmxErrors.UNKNOWN.value, task_name=self._task.name)


class AnalogSingleChannelWriter(ChannelWriterBase):
    """
    Writes samples to an analog output channel in an NI-DAQmx task.
    """

    def write_many_sample(self, data, timeout=10.0):
        """
        Writes one or more floating-point samples to a single analog
        output channel in a task.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            data (numpy.ndarray): Contains a 1D NumPy array of
                floating-point samples to write to the task. Each
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
        """
        self._verify_array(data, False, True)
        
        auto_start = (self._auto_start if self._auto_start is not 
                      AUTO_START_UNSET else False)

        return _write_analog_f_64(
            self._handle, data, data.shape[0], auto_start, timeout)

    def write_one_sample(self, data, timeout=10):
        """
        Writes a single floating-point sample to a single analog output
        channel in a task.

        Args:
            data (float): Specifies the floating-point sample to write
                to the task.
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
        auto_start = (self._auto_start if self._auto_start is not 
                      AUTO_START_UNSET else True)
        
        return _write_analog_scalar_f_64(
            self._handle, data, auto_start, timeout)


class AnalogMultiChannelWriter(ChannelWriterBase):
    """
    Writes samples to one or more analog output channels in an NI-DAQmx
    task.
    """

    def write_many_sample(self, data, timeout=10.0):
        """
        Writes one or more floating-point samples to one or more analog
        output channels in a task.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            data (numpy.ndarray): Contains a 2D NumPy array of
                floating-point samples to write to the task.

                Each row corresponds to a channel in the task. Each
                column corresponds to a sample to write to each channel.
                The order of the channels in the array corresponds to
                the order in which you add the channels to the task.
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
            successfully wrote to each channel in the task.
        """
        self._verify_array(data, True, True)
        
        auto_start = (self._auto_start if self._auto_start is not 
                      AUTO_START_UNSET else False)

        return _write_analog_f_64(
            self._handle, data, data.shape[1], auto_start, timeout)

    def write_one_sample(self, data, timeout=10):
        """
        Writes a single floating-point sample to one or more analog
        output channels in a task.

        Args:
            data (numpy.ndarray): Contains a 1D NumPy array of
                floating-point samples to write to the task.

                Each element of the array corresponds to a channel in
                the task. The order of the channels in the array
                corresponds to the order in which you add the channels
                to the task.
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
        self._verify_array(data, True, False)
        
        auto_start = (self._auto_start if self._auto_start is not 
                      AUTO_START_UNSET else True)

        return _write_analog_f_64(
            self._handle, data, 1, auto_start, timeout)


class AnalogUnscaledWriter(ChannelWriterBase):
    """
    Writes unscaled samples to one or more analog output channels in
    an NI-DAQmx task.
    """

    def write_int16(self, data, timeout=10.0):
        """
        Writes one or more unscaled 16-bit integer samples to one or
        more analog output channels in a task.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            data (numpy.ndarray): Contains a 2D NumPy array of unscaled
                16-bit integer samples to write to the task.

                Each row corresponds to a channel in the task. Each
                column corresponds to a sample to write to each channel.
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
            successfully wrote to each channel in the task.
        """
        self._verify_array(data, True, True)
        
        auto_start = (self._auto_start if self._auto_start is not 
                      AUTO_START_UNSET else False)

        return _write_binary_i_16(
            self._handle, data, data.shape[1], auto_start, timeout)

    def write_int32(self, data, timeout=10.0):
        """
        Writes one or more unscaled 32-bit integer samples to one or
        more analog output channels in a task.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            data (numpy.ndarray): Contains a 2D NumPy array of unscaled
                32-bit integer samples to write to the task.

                Each row corresponds to a channel in the task. Each
                column corresponds to a sample to write to each channel.
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
            successfully wrote to each channel in the task.
        """
        self._verify_array(data, True, True)
        
        auto_start = (self._auto_start if self._auto_start is not 
                      AUTO_START_UNSET else False)

        return _write_binary_i_32(
            self._handle, data, data.shape[1], auto_start, timeout)

    def write_uint16(self, data, timeout=10.0):
        """
        Writes one or more unscaled 16-bit unsigned integer samples to
        one or more analog output channels in a task.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            data (numpy.ndarray): Contains a 2D NumPy array of unscaled
                16-bit unsigned integer samples to write to the task.

                Each row corresponds to a channel in the task. Each
                column corresponds to a sample to write to each channel.
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
            successfully wrote to each channel in the task.
        """
        self._verify_array(data, True, True)
        
        auto_start = (self._auto_start if self._auto_start is not 
                      AUTO_START_UNSET else False)

        return _write_binary_u_16(
            self._handle, data, data.shape[1], auto_start, timeout)

    def write_uint32(self, data, timeout=10.0):
        """
        Writes one or more unscaled 32-bit unsigned integer samples to
        one or more analog output channels in a task.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            data (numpy.ndarray): Contains a 2D NumPy array of unscaled
                32-bit unsigned integer samples to write to the task.

                Each row corresponds to a channel in the task. Each
                column corresponds to a sample to write to each channel.
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
            successfully wrote to each channel in the task.
        """
        self._verify_array(data, True, True)
        
        auto_start = (self._auto_start if self._auto_start is not 
                      AUTO_START_UNSET else False)

        return _write_binary_u_32(
            self._handle, data, data.shape[1], auto_start, timeout)


class CounterWriter(ChannelWriterBase):
    """
    Writes samples to a counter output channel in an NI-DAQmx task.
    """

    def write_many_sample_pulse_frequency(
            self, frequencies, duty_cycles, timeout=10.0):
        """
        Writes one or more pulse samples in terms of frequency to a
        single counter output channel in a task.

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
        """
        self._verify_array(frequencies, False, True)
        self._verify_array(duty_cycles, False, True)
        
        auto_start = (self._auto_start if self._auto_start is not 
                      AUTO_START_UNSET else False)

        return _write_ctr_freq(
            self._handle, frequencies, duty_cycles, frequencies.shape[0],
            auto_start, timeout)

    def write_many_sample_pulse_ticks(
            self, high_ticks, low_ticks, timeout=10.0):
        """
        Writes one or more pulse samples in terms of ticks to a single
        counter output channel in a task.

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
        """
        self._verify_array(high_ticks, False, True)
        self._verify_array(low_ticks, False, True)
        
        auto_start = (self._auto_start if self._auto_start is not 
                      AUTO_START_UNSET else False)

        return _write_ctr_ticks(
            self._handle, high_ticks, low_ticks, high_ticks.shape[0],
            auto_start, timeout)

    def write_many_sample_pulse_time(
            self, high_times, low_times, timeout=10.0):
        """
        Writes one or more pulse samples in terms of time to a single
        counter output channel in a task.

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
        """
        self._verify_array(high_times, False, True)
        self._verify_array(low_times, False, True)
        
        auto_start = (self._auto_start if self._auto_start is not 
                      AUTO_START_UNSET else False)

        return _write_ctr_time(
            self._handle, high_times, low_times, high_times.shape[0],
            auto_start, timeout)

    def write_one_sample_pulse_frequency(
            self, frequency, duty_cycle, timeout=10):
        """
        Writes a new pulse frequency and duty cycle to a single counter
        output channel in a task.

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
        auto_start = (self._auto_start if self._auto_start is not 
                      AUTO_START_UNSET else True)
        
        return _write_ctr_freq_scalar(
            self._handle, frequency, duty_cycle, auto_start, timeout)

    def write_one_sample_pulse_ticks(
            self, high_ticks, low_ticks, timeout=10):
        """
        Writes a new pulse high tick count and low tick count to a
        single counter output channel in a task.

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
        """
        auto_start = (self._auto_start if self._auto_start is not 
                      AUTO_START_UNSET else True)
        
        return _write_ctr_ticks_scalar(
            self._handle, high_ticks, low_ticks, auto_start, timeout)

    def write_one_sample_pulse_time(
            self, high_time, low_time, timeout=10):
        """
        Writes a new pulse high time and low time to a single counter
        output channel in a task.

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
        auto_start = (self._auto_start if self._auto_start is not 
                      AUTO_START_UNSET else True)
        
        return _write_ctr_time_scalar(
            self._handle, high_time, low_time, auto_start, timeout)


class DigitalSingleChannelWriter(ChannelWriterBase):
    """
    Writes samples to a single digital output channel in an NI-DAQmx
    task.
    """

    def write_many_sample_port_byte(self, data, timeout=10.0):
        """
        Writes one or more 8-bit unsigned integer samples to a single
        digital output channel in a task.

        Use this method for devices with up to 8 lines per port.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            data (numpy.ndarray): Contains a 1D NumPy array of 8-bit
                unsigned integer samples to write to the task. Each
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
        """
        self._verify_array(data, False, True)
        
        auto_start = (self._auto_start if self._auto_start is not 
                      AUTO_START_UNSET else False)

        return _write_digital_u_8(
            self._handle, data, data.shape[0], auto_start, timeout)

    def write_many_sample_port_uint16(self, data, timeout=10.0):
        """
        Writes one or more 16-bit unsigned integer samples to a single
        digital output channel in a task.

        Use this method for devices with up to 16 lines per port.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            data (numpy.ndarray): Contains a 1D NumPy array of 16-bit
                unsigned integer samples to write to the task. Each
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
        """
        self._verify_array(data, False, True)
        
        auto_start = (self._auto_start if self._auto_start is not 
                      AUTO_START_UNSET else False)

        return _write_digital_u_16(
            self._handle, data, data.shape[0], auto_start, timeout)

    def write_many_sample_port_uint32(self, data, timeout=10.0):
        """
        Writes one or more 32-bit unsigned integer samples to a single
        digital output channel in a task.

        Use this method for devices with up to 32 lines per port.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            data (numpy.ndarray): Contains a 1D NumPy array of 32-bit
                unsigned integer samples to write to the task. Each
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
        """
        self._verify_array(data, False, True)
        
        auto_start = (self._auto_start if self._auto_start is not 
                      AUTO_START_UNSET else False)

        return _write_digital_u_32(
            self._handle, data, data.shape[0], auto_start, timeout)

    def write_one_sample_multi_line(self, data, timeout=10):
        """
        Writes a single boolean sample to a single digital output
        channel in a task. The channel can contain multiple digital
        lines.

        Args:
            data (numpy.ndarray): Contains a 1D NumPy array of boolean
                samples to write to the task. Each element of the array
                corresponds to a line in the channel.
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
        self._verify_array_digital_lines(data, False, True)
        
        auto_start = (self._auto_start if self._auto_start is not 
                      AUTO_START_UNSET else True)

        return _write_digital_lines(
            self._handle, data, 1, auto_start, timeout)

    def write_one_sample_one_line(self, data, timeout=10):
        """
        Writes a single boolean sample to a single digital output
        channel in a task. The channel can contain only one digital
        line.

        Args:
            data (int): Specifies the boolean sample to write to the
                task.
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
        auto_start = (self._auto_start if self._auto_start is not 
                      AUTO_START_UNSET else True)
        
        numpy_array = numpy.asarray([data], dtype=numpy.bool)

        return _write_digital_lines(
            self._handle, numpy_array, 1, auto_start, timeout)

    def write_one_sample_port_byte(self, data, timeout=10):
        """
        Writes a single 8-bit unsigned integer sample to a single
        digital output channel in a task.

        Use this method for devices with up to 8 lines per port.

        Args:
            data (int): Specifies the 8-bit unsigned integer sample to
                write to the task.
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
        auto_start = (self._auto_start if self._auto_start is not 
                      AUTO_START_UNSET else True)
        
        numpy_array = numpy.asarray([data], dtype=numpy.uint8)

        return _write_digital_u_8(
            self._handle, numpy_array, 1, auto_start, timeout)

    def write_one_sample_port_uint16(self, data, timeout=10):
        """
        Writes a single 16-bit unsigned integer sample to a single
        digital output channel in a task.

        Use this method for devices with up to 16 lines per port.

        Args:
            data (int): Specifies the 16-bit unsigned integer sample to
                write to the task.
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
        auto_start = (self._auto_start if self._auto_start is not 
                      AUTO_START_UNSET else True)
        
        numpy_array = numpy.asarray([data], dtype=numpy.uint16)

        return _write_digital_u_16(
            self._handle, numpy_array, 1, auto_start, timeout)

    def write_one_sample_port_uint32(self, data, timeout=10):
        """
        Writes a single 32-bit unsigned integer sample to a single
        digital output channel in a task.

        Use this method for devices with up to 32 lines per port.

        Args:
            data (int): Specifies the 32-bit unsigned integer sample to
                write to the task.
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
        auto_start = (self._auto_start if self._auto_start is not 
                      AUTO_START_UNSET else True)
        
        return _write_digital_scalar_u_32(
            self._handle, data, auto_start, timeout)


class DigitalMultiChannelWriter(ChannelWriterBase):
    """
    Writes samples to one or more digital output channels in an NI-DAQmx
    task.
    """

    def write_many_sample_port_byte(self, data, timeout=10.0):
        """
        Writes one or more 8-bit unsigned integer samples to one or more
        digital output channels in a task.

        Use this method for devices with up to 8 lines per port.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            data (numpy.ndarray): Contains a 2D NumPy array of 8-bit
                unsigned integer samples to write to the task.

                Each row corresponds to a channel in the task. Each
                column corresponds to a sample to write to each channel.
                The order of the channels in the array corresponds to
                the order in which you add the channels to the task.
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
            successfully wrote to each channel in the task.
        """
        self._verify_array(data, True, True)
        
        auto_start = (self._auto_start if self._auto_start is not 
                      AUTO_START_UNSET else False)

        return _write_digital_u_8(
            self._handle, data, data.shape[1], auto_start, timeout)

    def write_many_sample_port_uint16(self, data, timeout=10.0):
        """
        Writes one or more 16-bit unsigned integer samples to one or
        more digital output channels in a task.

        Use this method for devices with up to 16 lines per port.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            data (numpy.ndarray): Contains a 2D NumPy array of 16-bit
                unsigned integer samples to write to the task.

                Each row corresponds to a channel in the task. Each
                column corresponds to a sample to write to each channel.
                The order of the channels in the array corresponds to
                the order in which you add the channels to the task.
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
            successfully wrote to each channel in the task.
        """
        self._verify_array(data, True, True)
        
        auto_start = (self._auto_start if self._auto_start is not 
                      AUTO_START_UNSET else False)

        return _write_digital_u_16(
            self._handle, data, data.shape[1], auto_start, timeout)

    def write_many_sample_port_uint32(self, data, timeout=10.0):
        """
        Writes one or more 32-bit unsigned integer samples to one or
        more digital output channels in a task.

        Use this method for devices with up to 32 lines per port.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            data (numpy.ndarray): Contains a 2D NumPy array of 32-bit
                unsigned integer samples to write to the task.

                Each row corresponds to a channel in the task. Each
                column corresponds to a sample to write to each channel.
                The order of the channels in the array corresponds to
                the order in which you add the channels to the task.
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
            successfully wrote to each channel in the task.
        """
        self._verify_array(data, True, True)
        
        auto_start = (self._auto_start if self._auto_start is not 
                      AUTO_START_UNSET else False)

        return _write_digital_u_32(
            self._handle, data, data.shape[1], auto_start, timeout)

    def write_one_sample_multi_line(self, data, timeout=10):
        """
        Writes a single boolean sample to one or more digital output
        channels in a task. The channel can contain multiple digital
        lines.

        Args:
            data (numpy.ndarray): Contains a 2D NumPy array of boolean
                samples to write to the task.

                Each row corresponds to a channel in the task. Each
                column corresponds to a line from each channel. The
                order of the channels in the array corresponds to the
                order in which you add the channels to the task.
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
        self._verify_array_digital_lines(data, True, True)
        
        auto_start = (self._auto_start if self._auto_start is not 
                      AUTO_START_UNSET else True)

        return _write_digital_lines(
            self._handle, data, 1, auto_start, timeout)

    def write_one_sample_one_line(self, data, timeout=10):
        """
        Writes a single boolean sample to one or more digital output
        channels in a task. The channel can contain only one digital
        line.

        Args:
            data (numpy.ndarray): Contains a 1D NumPy array of boolean
                samples to write to the task.

                Each element in the array corresponds to a channel in
                the task. The order of the channels in the array
                corresponds to the order in which you add the channels
                to the task.
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
        self._verify_array_digital_lines(data, True, False)
        
        auto_start = (self._auto_start if self._auto_start is not 
                      AUTO_START_UNSET else True)

        return _write_digital_lines(
            self._handle, data, 1, auto_start, timeout)

    def write_one_sample_port_byte(self, data, timeout=10):
        """
        Writes a single 8-bit unsigned integer sample to one or more
        digital output channels in a task.

        Use this method for devices with up to 8 lines per port.

        Args:
            data (numpy.ndarray): Contains a 1D NumPy array of 8-bit
                unsigned integer samples to write to the task.

                Each element in the array corresponds to a channel in
                the task. The order of the channels in the array
                corresponds to the order in which you add the channels
                to the task.
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
        self._verify_array(data, True, False)
        
        auto_start = (self._auto_start if self._auto_start is not 
                      AUTO_START_UNSET else True)

        return _write_digital_u_8(
            self._handle, data, 1, auto_start, timeout)

    def write_one_sample_port_uint16(self, data, timeout=10):
        """
        Writes a single 16-bit unsigned integer sample to one or more
        digital output channels in a task.

        Use this method for devices with up to 16 lines per port.

        Args:
            data (numpy.ndarray): Contains a 1D NumPy array of 16-bit
                unsigned integer samples to write to the task.

                Each element in the array corresponds to a channel in
                the task. The order of the channels in the array
                corresponds to the order in which you add the channels
                to the task.
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
        self._verify_array(data, True, False)
        
        auto_start = (self._auto_start if self._auto_start is not 
                      AUTO_START_UNSET else True)

        return _write_digital_u_16(
            self._handle, data, 1, auto_start, timeout)

    def write_one_sample_port_uint32(self, data, timeout=10):
        """
        Writes a single 32-bit unsigned integer sample to one or more
        digital output channels in a task.

        Use this method for devices with up to 32 lines per port.

        Args:
            data (numpy.ndarray): Contains a 1D NumPy array of 32-bit
                unsigned integer samples to write to the task.

                Each element in the array corresponds to a channel in
                the task. The order of the channels in the array
                corresponds to the order in which you add the channels
                to the task.
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
        self._verify_array(data, True, False)
        
        auto_start = (self._auto_start if self._auto_start is not 
                      AUTO_START_UNSET else True)

        return _write_digital_u_32(
            self._handle, data, 1, auto_start, timeout)
