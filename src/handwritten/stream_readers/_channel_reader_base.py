from __future__ import annotations

from nidaqmx import DaqError
from nidaqmx.error_codes import DAQmxErrors


class ChannelReaderBase:
    """Defines base class for all NI-DAQmx stream readers."""

    def __init__(self, task_in_stream):
        """Initialize a new ChannelReaderBase.

        Args:
            task_in_stream: Specifies the input stream associated with
                an NI-DAQmx task from which to read samples.
        """
        self._in_stream = task_in_stream
        self._task = task_in_stream._task
        self._handle = task_in_stream._task._handle
        self._interpreter = task_in_stream._task._interpreter

        self._verify_array_shape = True

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

    def _verify_array(self, data, number_of_samples_per_channel, is_many_chan, is_many_samp):
        """Verify the shape of a NumPy array.

        Verifies that the shape of the specified NumPy array can be used
        to read multiple samples from the current task which contains
        one or more channels, if the "verify_array_shape" property is
        set to True.

        Args:
            data (numpy.ndarray): Specifies the NumPy array to verify.
            number_of_samples_per_channel (int): Specifies the number of
                samples per channel requested.
            is_many_chan (bool): Specifies if the read method is a many
                channel version.
            is_many_samp (bool): Specifies if the read method is a many
                samples version.
        """
        if not self._verify_array_shape:
            return

        number_of_channels = self._in_stream.num_chans

        array_shape: tuple[int, ...] | None = None
        if is_many_chan:
            if is_many_samp:
                array_shape = (number_of_channels, number_of_samples_per_channel)
            else:
                array_shape = (number_of_channels,)
        else:
            if is_many_samp:
                array_shape = (number_of_samples_per_channel,)

        if array_shape is not None and data.shape != array_shape:
            raise DaqError(
                "Read cannot be performed because the NumPy array passed into "
                "this function is not shaped correctly. You must pass in a "
                "NumPy array of the correct shape based on the number of "
                "channels in task and the number of samples per channel "
                "requested.\n\n"
                "Shape of NumPy Array provided: {}\n"
                "Shape of NumPy Array required: {}".format(data.shape, array_shape),
                DAQmxErrors.UNKNOWN,
                task_name=self._task.name,
            )

    def _verify_array_digital_lines(self, data, is_many_chan, is_many_line):
        """Verify the shape of a NumPy array of digital lines.

        Verifies that the shape of the specified NumPy array can be used
        to read samples from the current task which contains one or more
        channels that have one or more digital lines per channel, if the
        "verify_array_shape" property is set to True.

        Args:
            data (numpy.ndarray): Specifies the NumPy array to verify.
            is_many_chan (bool): Specifies if the read method is a
                many channel version.
            is_many_line (bool): Specifies if the read method is a
                many line version.
        """
        if not self._verify_array_shape:
            return

        number_of_channels = self._in_stream.num_chans
        number_of_lines = self._in_stream.di_num_booleans_per_chan

        array_shape: tuple[int, ...] | None = None
        if is_many_chan:
            if is_many_line:
                array_shape = (number_of_channels, number_of_lines)
            else:
                array_shape = (number_of_channels,)
        else:
            if is_many_line:
                array_shape = (number_of_lines,)

        if array_shape is not None and data.shape != array_shape:
            raise DaqError(
                "Read cannot be performed because the NumPy array passed into "
                "this function is not shaped correctly. You must pass in a "
                "NumPy array of the correct shape based on the number of "
                "channels in task and the number of digital lines per "
                "channel.\n\n"
                "Shape of NumPy Array provided: {}\n"
                "Shape of NumPy Array required: {}".format(data.shape, array_shape),
                DAQmxErrors.UNKNOWN,
                task_name=self._task.name,
            )
