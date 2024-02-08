<%
    from codegen.utilities.attribute_helpers import get_attributes, get_enums_used
    from codegen.utilities.text_wrappers import wrap
    attributes = get_attributes(data, "InStream")
    enums_used = get_enums_used(attributes)
%>\
# Do not edit this file; it was automatically generated.

import numpy
import deprecation

from nidaqmx._task_modules.channels.channel import Channel
from nidaqmx.utils import unflatten_channel_string
from nidaqmx.constants import (
    ${', '.join([c for c in enums_used]) | wrap(4, 4)})


class InStream:
    """
    Exposes an input data stream on a DAQmx task.

    The input data stream be used to control reading behavior and can be
    used in conjunction with reader classes to read samples from an
    NI-DAQmx task.
    """
    def __init__(self, task, interpreter):
        self._task = task
        self._handle = task._handle
        self._interpreter = interpreter
        self._timeout = 10.0

        super().__init__()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self._handle == other._handle and
                    self._timeout == other._timeout)
        return False

    def __hash__(self):
        return self._interpreter.hash_task_handle(self._handle) ^ hash(self._timeout)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return f'InStream(task={self._task.name})'

    @property
    def timeout(self):
        """
        float: Specifies the amount of time in seconds to wait for
            samples to become available. If the time elapses, the read
            method returns an error and any samples read before the
            timeout elapsed. The default timeout is 10 seconds. If you
            set timeout to nidaqmx.WAIT_INFINITELY, the read method
            waits indefinitely. If you set timeout to 0, the read method
            tries once to read the requested samples and returns an error
            if it is unable to.
        """
        return self._timeout

    @timeout.setter
    def timeout(self, val):
        self._timeout = val

    @timeout.deleter
    def timeout(self):
        self._timeout = 10.0

<%namespace name="property_template" file="/property_template.py.mako"/>\
%for attribute in attributes:
${property_template.script_property(attribute)}\
%endfor
\
    def _calculate_num_samps_per_chan(self, num_samps_per_chan):
        if num_samps_per_chan == -1:
            acq_type = self._task.timing.samp_quant_samp_mode

            if (acq_type == AcquisitionType.FINITE and
                    not self.read_all_avail_samp):
                return self._task.timing.samp_quant_samp_per_chan
            else:
                return self.avail_samp_per_chan
        else:
            return num_samps_per_chan

    def configure_logging(
            self, file_path, logging_mode=LoggingMode.LOG_AND_READ,
            group_name="", operation=LoggingOperation.OPEN_OR_CREATE):
        """
        Configures TDMS file logging for the task.

        Args:
            file_path (str): Specifies the path to the TDMS file to
                which you want to log data.
            logging_mode (Optional[nidaqmx.constants.LoggingMode]):
                Specifies whether to enable logging and whether to allow
                reading data while logging. "log" mode allows for the
                best performance. However, you cannot read data while
                logging if you specify this mode. If you want to read
                data while logging, specify "LOG_AND_READ" mode.
            group_name (Optional[str]): Specifies the name of the group
                to create within the TDMS file for data from this task.
                If you append data to an existing file and the specified
                group already exists, NI-DAQmx appends a number symbol
                and a number to the group name, incrementing that number
                until finding a group name that does not exist. For
                example, if you specify a group name of Voltage Task,
                and that group already exists, NI-DAQmx assigns the
                group name Voltage Task #1, then Voltage Task #2. If you
                do not specify a group name, NI-DAQmx uses the name of
                the task.
            operation (Optional[nidaqmx.constants.LoggingOperation]):
                Specifies how to open the TDMS file.
        """

        self._interpreter.configure_logging(
            self._handle, file_path, logging_mode.value, group_name, operation.value)

    def read(self, number_of_samples_per_channel=READ_ALL_AVAILABLE):
        """
        Reads raw samples from the task or virtual channels you specify.

        Raw samples constitute the internal representation of samples in a
        device, read directly from the device or buffer without scaling or
        reordering. The native format of a device can be an 8-, 16-, or
        32-bit integer, signed or unsigned.

        NI-DAQmx does not separate raw data into channels. It returns data
        in an interleaved or non-interleaved 1D array, depending on the
        raw ordering of the device. Refer to your device documentation for
        more information.

        This method determines a NumPy array of appropriate size and data
        type to create and return based on your device specifications.

        Use the "timeout" property on the stream to specify the amount of
        time in seconds to wait for samples to become available. If the
        time elapses, the method returns an error and any samples read
        before the timeout elapsed. The default timeout is 10 seconds.
        If you set timeout to nidaqmx.WAIT_INFINITELY, the method waits
        indefinitely. If you set timeout to 0, the method tries once to
        read the requested samples and returns an error if it is unable
        to.

        Args:
            number_of_samples_per_channel (int): Specifies the number of
                samples to read.

                If you set this input to nidaqmx.READ_ALL_AVAILABLE,
                NI-DAQmx determines how many samples to read based on if
                the task acquires samples continuously or acquires a
                finite number of samples.

                If the task acquires samples continuously and you set
                this input to nidaqmx.READ_ALL_AVAILABLE, this method
                reads all the samples currently available in the buffer.

                If the task acquires a finite number of samples and you
                set this input to nidaqmx.READ_ALL_AVAILABLE, the method
                waits for the task to acquire all requested samples,
                then reads those samples. If you set the
                "read_all_avail_samp" property to TRUE, the method reads
                the samples currently available in the buffer and does
                not wait for the task to acquire all requested samples.
        Returns:
            numpy.ndarray:

            The samples requested in the form of a 1D NumPy array. This
            method determines a NumPy array of appropriate size and data
            type to create and return based on your device specifications.
        """
        channels_to_read = self.channels_to_read
        number_of_channels = len(channels_to_read.channel_names)

        samp_size_in_bits = channels_to_read.ai_raw_samp_size
        has_negative_range = channels_to_read.ai_rng_low < 0

        if samp_size_in_bits == 32:
            if has_negative_range:
                dtype = numpy.int32
            else:
                dtype = numpy.uint32
        elif samp_size_in_bits == 16:
            if has_negative_range:
                dtype = numpy.int16
            else:
                dtype = numpy.uint16
        else:
            if has_negative_range:
                dtype = numpy.int8
            else:
                dtype = numpy.uint8

        num_samps_per_chan = self._calculate_num_samps_per_chan(
            number_of_samples_per_channel)

        number_of_samples = number_of_channels * num_samps_per_chan

        numpy_array = numpy.zeros(number_of_samples, dtype=dtype)

        _, samples_read, _ = self._interpreter.read_raw(
            self._handle, num_samps_per_chan,
            self.timeout, numpy_array)

        if number_of_channels * samples_read != number_of_samples:
            return numpy_array[:number_of_channels * samples_read]
        return numpy_array

    def read_all(self):
        """
        Reads all available raw samples from the task or virtual channels
        you specify.

        NI-DAQmx determines how many samples to read based on if the task
        acquires samples continuously or acquires a finite number of
        samples.

        If the task acquires samples continuously, this method reads all
        the samples currently available in the buffer.

        If the task acquires a finite number of samples, the method
        waits for the task to acquire all requested samples, then reads
        those samples. If you set the "read_all_avail_samp" property to
        TRUE, the method reads the samples currently available in the
        buffer and does not wait for the task to acquire all requested
        samples.

        Raw samples constitute the internal representation of samples in a
        device, read directly from the device or buffer without scaling or
        reordering. The native format of a device can be an 8-, 16-, or
        32-bit integer, signed or unsigned.

        NI-DAQmx does not separate raw data into channels. It returns data
        in an interleaved or non-interleaved 1D array, depending on the
        raw ordering of the device. Refer to your device documentation for
        more information.

        This method determines a NumPy array of appropriate size and data
        type to create and return based on your device specifications.

        Use the "timeout" property on the stream to specify the amount of
        time in seconds to wait for samples to become available. If the
        time elapses, the method returns an error and any samples read
        before the timeout elapsed. The default timeout is 10 seconds.
        If you set timeout to nidaqmx.WAIT_INFINITELY, the method waits
        indefinitely. If you set timeout to 0, the method tries once to
        read the requested samples and returns an error if it is unable
        to.

        Returns:
            numpy.ndarray:

            The samples requested in the form of a 1D NumPy array. This
            method determines a NumPy array of appropriate size and data
            type to create and return based on your device specifications.
        """
        return self.read(number_of_samples_per_channel=READ_ALL_AVAILABLE)

    def read_into(self, numpy_array):
        """
        Reads raw samples from the task or virtual channels you specify
        into numpy_array.

        The object numpy_array should be a pre-allocated, writable 1D
        numpy array.

        The number of samples per channel to read is determined using
        the following equation:

        number_of_samples_per_channel = math.floor(
            numpy_array_size_in_bytes / (
                number_of_channels_to_read * raw_sample_size_in_bytes))

        Raw samples constitute the internal representation of samples in a
        device, read directly from the device or buffer without scaling or
        reordering. The native format of a device can be an 8-, 16-, or
        32-bit integer, signed or unsigned.

        If you use a different integer size than the native format of the
        device, one integer can contain multiple samples or one sample can
        stretch across multiple integers. For example, if you use 32-bit
        integers, but the device uses 8-bit samples, one integer contains
        up to four samples. If you use 8-bit integers, but the device uses
        16-bit samples, a sample might require two integers. This behavior
        varies from device to device. Refer to your device documentation
        for more information.

        NI-DAQmx does not separate raw data into channels. It returns data
        in an interleaved or non-interleaved 1D array, depending on the
        raw ordering of the device. Refer to your device documentation for
        more information.

        Use the "timeout" property on the stream to specify the amount of
        time in seconds to wait for samples to become available. If the
        time elapses, the method returns an error and any samples read
        before the timeout elapsed. The default timeout is 10 seconds.
        If you set timeout to -1, the method waits indefinitely. If you
        set timeout to 0, the method tries once to read the requested
        samples and returns an error if it is unable to.

        Args:
            numpy_array: Specifies the 1D NumPy array object into which
                the samples requested are read.
        Returns:
            int: Indicates the total number of samples read.
        """
        channels_to_read = self.channels_to_read
        number_of_channels = len(channels_to_read.channel_names)

        number_of_samples_per_channel, _ = divmod(
            numpy_array.nbytes, (
                number_of_channels * channels_to_read.ai_raw_samp_size // 8))

        _, samples_read, _ = self._interpreter.read_raw(
            self._handle, number_of_samples_per_channel,
            self.timeout, numpy_array)

        return samples_read

    def start_new_file(self, file_path):
        """
        Starts a new TDMS file the next time data is written to disk.

        Args:
            file_path (str): Specifies the path to the TDMS file to
                which you want to log data.
        """

        self._interpreter.start_new_file(self._handle, file_path)

<%namespace name="deprecated_template" file="/property_deprecated_template.py.mako"/>\
${deprecated_template.script_deprecated_property(attributes)}\
