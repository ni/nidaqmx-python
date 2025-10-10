from nidaqmx import DaqError
from nidaqmx.error_codes import DAQmxErrors


class UnsetAutoStartSentinel:
    """Sentinel class for unset auto_start parameter."""

    def __init__(self):  # noqa: D107 - Missing docstring in __init__ (auto-generated noqa)
        raise RuntimeError(
            "Cannot instantiate UnsetAutoStartSentinel. Use AUTO_START_UNSET instead."
        )


AUTO_START_UNSET = object.__new__(UnsetAutoStartSentinel)


class ChannelWriterBase:
    """Defines base class for all NI-DAQmx stream writers."""

    def __init__(self, task_out_stream, auto_start=AUTO_START_UNSET):
        """Initialize a new ChannelWriterBase.

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
        self._interpreter = task_out_stream._task._interpreter

        self._verify_array_shape = True
        self._auto_start = auto_start

    @property
    def auto_start(self):
        """bool: Specifies whether the write method automatically starts the task, if needed.

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
        """bool: Specifies whether to verify the shape of NumPy arrays.

        Defaults to True when this object is instantiated.

        Setting this property to True may marginally adversely
        impact the performance of read methods.
        """
        return self._verify_array_shape

    @verify_array_shape.setter
    def verify_array_shape(self, val):
        self._verify_array_shape = val

    def _verify_array(self, data, is_many_chan, is_many_samp):
        """Verifies the shape of a NumPy array.

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

        number_of_channels = self._out_stream.num_chans

        expected_num_dimensions = None
        if is_many_chan:
            if is_many_samp:
                expected_num_dimensions = 2
            else:
                expected_num_dimensions = 1

            if data.shape[0] != number_of_channels:
                self._task._raise_invalid_write_num_chans_error(number_of_channels, data.shape[0])
        else:
            if is_many_samp:
                expected_num_dimensions = 1

        if expected_num_dimensions is not None:
            self._raise_error_if_invalid_write_dimensions(expected_num_dimensions, len(data.shape))

    def _verify_array_digital_lines(self, data, is_many_chan, is_many_line):
        """Verify the shape of a NumPy array of digital lines.

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

        number_of_channels = self._out_stream.num_chans
        number_of_lines = self._out_stream.do_num_booleans_per_chan

        expected_num_dimensions = None
        if is_many_chan:
            if data.shape[0] != number_of_channels:
                self._task._raise_invalid_write_num_chans_error(number_of_channels, data.shape[0])

            if is_many_line:
                expected_num_dimensions = 2
                if data.shape[1] != number_of_lines:
                    self._task._raise_invalid_num_lines_error(number_of_lines, data.shape[1])
            else:
                expected_num_dimensions = 1
        else:
            if is_many_line:
                expected_num_dimensions = 1
                if data.shape[0] != number_of_lines:
                    self._task._raise_invalid_num_lines_error(number_of_lines, data.shape[0])

        if expected_num_dimensions is not None:
            self._raise_error_if_invalid_write_dimensions(expected_num_dimensions, len(data.shape))

    def _raise_error_if_invalid_write_dimensions(
        self, num_dimensions_expected, num_dimensions_in_data
    ):
        if num_dimensions_expected != num_dimensions_in_data:
            raise DaqError(
                "Write cannot be performed because the NumPy array passed "
                "into this function is not shaped correctly. "
                "You must pass in a NumPy array of the correct number of "
                "dimensions based on the write method you use.\n\n"
                "No. of dimensions of NumPy Array provided: {}\n"
                "No. of dimensions of NumPy Array required: {}".format(
                    num_dimensions_in_data, num_dimensions_expected
                ),
                DAQmxErrors.UNKNOWN,
                task_name=self._task.name,
            )
