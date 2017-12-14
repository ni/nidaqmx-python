from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import ctypes
import numpy

from nidaqmx._lib import lib_importer, ctypes_byte_str, c_bool32
from nidaqmx._task_modules.read_functions import _read_raw
from nidaqmx.errors import check_for_error, is_string_buffer_too_small
from nidaqmx._task_modules.channels.channel import Channel
from nidaqmx.utils import unflatten_channel_string
from nidaqmx.constants import (
    AcquisitionType, LoggingMode, LoggingOperation, OverwriteMode,
    READ_ALL_AVAILABLE, ReadRelativeTo, WaitMode)


class InStream(object):
    """
    Exposes an input data stream on a DAQmx task.

    The input data stream be used to control reading behavior and can be
    used in conjunction with reader classes to read samples from an
    NI-DAQmx task.
    """
    def __init__(self, task):
        self._task = task
        self._handle = task._handle
        self._timeout = 10.0

        super(InStream, self).__init__()

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self._handle == other._handle and
                    self._timeout == other._timeout)
        return False

    def __hash__(self):
        return hash((self._handle.value, self._timeout))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return 'InStream(task={0})'.format(self._task.name)

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

    @property
    def accessory_insertion_or_removal_detected(self):
        """
        bool: Indicates if any device(s) in the task detected the
            insertion or removal of an accessory since the task started.
            Reading this property clears the accessory change status for
            all channels in the task. You must read this property before
            you read **devs_with_inserted_or_removed_accessories**.
            Otherwise, you will receive an error.
        """
        val = c_bool32()

        cfunc = (lib_importer.windll.
                 DAQmxGetReadAccessoryInsertionOrRemovalDetected)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def auto_start(self):
        """
        bool: Specifies if DAQmx Read automatically starts the task  if
            you did not start the task explicitly by using DAQmx Start.
            The default value is True. When  DAQmx Read starts a finite
            acquisition task, it also stops the task after reading the
            last sample.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetReadAutoStart
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @auto_start.setter
    def auto_start(self, val):
        cfunc = lib_importer.windll.DAQmxSetReadAutoStart
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, c_bool32]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @auto_start.deleter
    def auto_start(self):
        cfunc = lib_importer.windll.DAQmxResetReadAutoStart
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def avail_samp_per_chan(self):
        """
        int: Indicates the number of samples available to read per
            channel. This value is the same for all channels in the
            task.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetReadAvailSampPerChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle,
                        ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def change_detect_overflowed(self):
        """
        bool: Indicates if samples were missed because change detection
            events occurred faster than the device could handle them.
            Some devices detect overflows differently than others.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetReadChangeDetectHasOverflowed
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def channels_to_read(self):
        """
        :class:`nidaqmx._task_modules.channels.channel.Channel`:
            Specifies a subset of channels in the task from which to
            read.
        """
        cfunc = lib_importer.windll.DAQmxGetReadChannelsToRead
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return Channel._factory(self._handle, val.value.decode('ascii'))

    @channels_to_read.setter
    def channels_to_read(self, val):
        val = val.name
        cfunc = lib_importer.windll.DAQmxSetReadChannelsToRead
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @channels_to_read.deleter
    def channels_to_read(self):
        cfunc = lib_importer.windll.DAQmxResetReadChannelsToRead
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def common_mode_range_error_chans(self):
        """
        List[str]: Indicates a list of names of any virtual channels in
            the task for which the device(s) detected a common mode
            range violation. You must read
            **common_mode_range_error_chans_exist** before you read this
            property. Otherwise, you will receive an error.
        """
        cfunc = lib_importer.windll.DAQmxGetReadCommonModeRangeErrorChans
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 2048
        val = ctypes.create_string_buffer(temp_size)

        error_code = cfunc(
            self._handle, val, temp_size)
        check_for_error(error_code)

        return unflatten_channel_string(val.value.decode('ascii'))

    @property
    def common_mode_range_error_chans_exist(self):
        """
        bool: Indicates if the device(s) detected a common mode range
            violation for any virtual channel in the task. Common mode
            range violation occurs when the voltage of either the
            positive terminal or negative terminal to ground are out of
            range. Reading this property clears the common mode range
            violation status for all channels in the task. You must read
            this property before you read
            **common_mode_range_error_chans**. Otherwise, you will
            receive an error.
        """
        val = c_bool32()

        cfunc = (lib_importer.windll.
                 DAQmxGetReadCommonModeRangeErrorChansExist)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def curr_read_pos(self):
        """
        long: Indicates in samples per channel the current position in
            the buffer.
        """
        val = ctypes.c_ulonglong()

        cfunc = lib_importer.windll.DAQmxGetReadCurrReadPos
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle,
                        ctypes.POINTER(ctypes.c_ulonglong)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def devs_with_inserted_or_removed_accessories(self):
        """
        List[str]: Indicates the names of any devices that detected the
            insertion or removal of an accessory since the task started.
            You must read **accessory_insertion_or_removal_detected**
            before you read this property. Otherwise, you will receive
            an error.
        """
        cfunc = (lib_importer.windll.
                 DAQmxGetReadDevsWithInsertedOrRemovedAccessories)
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return unflatten_channel_string(val.value.decode('ascii'))

    @property
    def di_num_booleans_per_chan(self):
        """
        int: Indicates the number of booleans per channel that NI-DAQmx
            returns in a sample for line-based reads. If a channel has
            fewer lines than this number, the extra booleans are False.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetReadDigitalLinesBytesPerChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle,
                        ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def excit_fault_chans(self):
        """
        List[str]: Indicates a list of names of any virtual channels in
            the task for which the device(s) detected an excitation
            fault condition. You must read **excit_fault_chans_exist**
            before you read this property. Otherwise, you will receive
            an error.
        """
        cfunc = lib_importer.windll.DAQmxGetReadExcitFaultChans
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return unflatten_channel_string(val.value.decode('ascii'))

    @property
    def excit_fault_chans_exist(self):
        """
        bool: Indicates if the device(s) detected an excitation fault
            condition for any virtual channel in the task. Reading this
            property clears the excitation fault status for all channels
            in the task. You must read this property before you read
            **excit_fault_chans**. Otherwise, you will receive an error.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetReadExcitFaultChansExist
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def input_buf_size(self):
        """
        int: Specifies the number of samples the input buffer can hold
            for each channel in the task. Zero indicates to allocate no
            buffer. Use a buffer size of 0 to perform a hardware-timed
            operation without using a buffer. Setting this property
            overrides the automatic input buffer allocation that NI-
            DAQmx performs.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetBufInputBufSize
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle,
                        ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @input_buf_size.setter
    def input_buf_size(self, val):
        cfunc = lib_importer.windll.DAQmxSetBufInputBufSize
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_uint]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @input_buf_size.deleter
    def input_buf_size(self):
        cfunc = lib_importer.windll.DAQmxResetBufInputBufSize
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def input_onbrd_buf_size(self):
        """
        int: Indicates in samples per channel the size of the onboard
            input buffer of the device.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetBufInputOnbrdBufSize
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle,
                        ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def logging_file_path(self):
        """
        str: Specifies the path to the TDMS file to which you want to
            log data.  If the file path is changed while the task is
            running, this takes effect on the next sample interval (if
            Logging.SampsPerFile has been set) or when DAQmx Start New
            File is called. New file paths can be specified by ending
            with "\" or "/". Files created after specifying a new file
            path retain the same name and numbering sequence.
        """
        cfunc = lib_importer.windll.DAQmxGetLoggingFilePath
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.value.decode('ascii')

    @logging_file_path.setter
    def logging_file_path(self, val):
        cfunc = lib_importer.windll.DAQmxSetLoggingFilePath
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @logging_file_path.deleter
    def logging_file_path(self):
        cfunc = lib_importer.windll.DAQmxResetLoggingFilePath
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def logging_file_preallocation_size(self):
        """
        long: Specifies a size in samples to be used to pre-allocate
            space on disk.  Pre-allocation can improve file I/O
            performance, especially in situations where multiple files
            are being written to disk.  For finite tasks, the default
            behavior is to pre-allocate the file based on the number of
            samples you configure the task to acquire.
        """
        val = ctypes.c_ulonglong()

        cfunc = lib_importer.windll.DAQmxGetLoggingFilePreallocationSize
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle,
                        ctypes.POINTER(ctypes.c_ulonglong)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @logging_file_preallocation_size.setter
    def logging_file_preallocation_size(self, val):
        cfunc = lib_importer.windll.DAQmxSetLoggingFilePreallocationSize
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_ulonglong]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @logging_file_preallocation_size.deleter
    def logging_file_preallocation_size(self):
        cfunc = lib_importer.windll.DAQmxResetLoggingFilePreallocationSize
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def logging_file_write_size(self):
        """
        int: Specifies the size, in samples, in which data will be
            written to disk.  The size must be evenly divisible by the
            volume sector size, in bytes.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetLoggingFileWriteSize
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle,
                        ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @logging_file_write_size.setter
    def logging_file_write_size(self, val):
        cfunc = lib_importer.windll.DAQmxSetLoggingFileWriteSize
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_uint]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @logging_file_write_size.deleter
    def logging_file_write_size(self):
        cfunc = lib_importer.windll.DAQmxResetLoggingFileWriteSize
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def logging_mode(self):
        """
        :class:`nidaqmx.constants.LoggingMode`: Specifies whether to
            enable logging and whether to allow reading data while
            logging. Log mode allows for the best performance. However,
            you cannot read data while logging if you specify this mode.
            If you want to read data while logging, specify Log and Read
            mode.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetLoggingMode
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return LoggingMode(val.value)

    @logging_mode.setter
    def logging_mode(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetLoggingMode
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @logging_mode.deleter
    def logging_mode(self):
        cfunc = lib_importer.windll.DAQmxResetLoggingMode
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def logging_pause(self):
        """
        bool: Specifies whether logging is paused while a task is
            executing. If **logging_mode** is set to Log and Read mode,
            this value is taken into consideration on the next call to
            DAQmx Read, where data is written to disk. If
            **logging_mode** is set to Log Only mode, this value is
            taken into consideration the next time that data is written
            to disk. A new TDMS group is written when logging is resumed
            from a paused state.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetLoggingPause
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @logging_pause.setter
    def logging_pause(self, val):
        cfunc = lib_importer.windll.DAQmxSetLoggingPause
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, c_bool32]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @logging_pause.deleter
    def logging_pause(self):
        cfunc = lib_importer.windll.DAQmxResetLoggingPause
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def logging_samps_per_file(self):
        """
        long: Specifies how many samples to write to each file. When the
            file reaches the number of samples specified, a new file is
            created with the naming convention of <filename>_####.tdms,
            where #### starts at 0001 and increments automatically with
            each new file. For example, if the file specified is
            C:\data.tdms, the next file name used is C:\data_0001.tdms.
            To disable file spanning behavior, set this attribute to 0.
            If **logging_file_path** is changed while this attribute is
            set, the new file path takes effect on the next file
            created.
        """
        val = ctypes.c_ulonglong()

        cfunc = lib_importer.windll.DAQmxGetLoggingSampsPerFile
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle,
                        ctypes.POINTER(ctypes.c_ulonglong)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @logging_samps_per_file.setter
    def logging_samps_per_file(self, val):
        cfunc = lib_importer.windll.DAQmxSetLoggingSampsPerFile
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_ulonglong]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @logging_samps_per_file.deleter
    def logging_samps_per_file(self):
        cfunc = lib_importer.windll.DAQmxResetLoggingSampsPerFile
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def logging_tdms_group_name(self):
        """
        str: Specifies the name of the group to create within the TDMS
            file for data from this task. If you append data to an
            existing file and the specified group already exists, NI-
            DAQmx appends a number symbol and a number to the group
            name, incrementing that number until finding a group name
            that does not exist. For example, if you specify a group
            name of Voltage Task, and that group already exists, NI-
            DAQmx assigns the group name Voltage Task #1, then Voltage
            Task #2.
        """
        cfunc = lib_importer.windll.DAQmxGetLoggingTDMSGroupName
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return val.value.decode('ascii')

    @logging_tdms_group_name.setter
    def logging_tdms_group_name(self, val):
        cfunc = lib_importer.windll.DAQmxSetLoggingTDMSGroupName
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @logging_tdms_group_name.deleter
    def logging_tdms_group_name(self):
        cfunc = lib_importer.windll.DAQmxResetLoggingTDMSGroupName
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def logging_tdms_operation(self):
        """
        :class:`nidaqmx.constants.LoggingOperation`: Specifies how to
            open the TDMS file.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetLoggingTDMSOperation
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return LoggingOperation(val.value)

    @logging_tdms_operation.setter
    def logging_tdms_operation(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetLoggingTDMSOperation
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @logging_tdms_operation.deleter
    def logging_tdms_operation(self):
        cfunc = lib_importer.windll.DAQmxResetLoggingTDMSOperation
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def num_chans(self):
        """
        int: Indicates the number of channels that DAQmx Read reads from
            the task. This value is the number of channels in the task
            or the number of channels you specify with
            **channels_to_read**.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetReadNumChans
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle,
                        ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def offset(self):
        """
        int: Specifies an offset in samples per channel at which to
            begin a read operation. This offset is relative to the
            location you specify with **relative_to**.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetReadOffset
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @offset.setter
    def offset(self, val):
        cfunc = lib_importer.windll.DAQmxSetReadOffset
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @offset.deleter
    def offset(self):
        cfunc = lib_importer.windll.DAQmxResetReadOffset
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def open_chans(self):
        """
        List[str]: Indicates a list of names of any open virtual
            channels. You must read **open_chans_exist** before you read
            this property. Otherwise you will receive an error.
        """
        cfunc = lib_importer.windll.DAQmxGetReadOpenChans
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return unflatten_channel_string(val.value.decode('ascii'))

    @property
    def open_chans_details(self):
        """
        List[str]: Indicates a list of details of any open virtual
            channels. You must read **open_chans_exist** before you read
            this property. Otherwise you will receive an error.
        """
        cfunc = lib_importer.windll.DAQmxGetReadOpenChansDetails
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return unflatten_channel_string(val.value.decode('ascii'))

    @property
    def open_chans_exist(self):
        """
        bool: Indicates if the device or devices detected an open
            channel condition in any virtual channel in the task.
            Reading this property clears the open channel status for all
            channels in this task. You must read this property before
            you read **open_chans**. Otherwise, you will receive an
            error.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetReadOpenChansExist
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def open_current_loop_chans(self):
        """
        List[str]: Indicates a list of names of any virtual channels in
            the task for which the device(s) detected an open current
            loop. You must read **open_current_loop_chans_exist** before
            you read this property. Otherwise, you will receive an
            error.
        """
        cfunc = lib_importer.windll.DAQmxGetReadOpenCurrentLoopChans
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return unflatten_channel_string(val.value.decode('ascii'))

    @property
    def open_current_loop_chans_exist(self):
        """
        bool: Indicates if the device(s) detected an open current loop
            for any virtual channel in the task. Reading this property
            clears the open current loop status for all channels in the
            task. You must read this property before you read
            **open_current_loop_chans**. Otherwise, you will receive an
            error.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetReadOpenCurrentLoopChansExist
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def open_thrmcpl_chans(self):
        """
        List[str]: Indicates a list of names of any virtual channels in
            the task for which the device(s) detected an open
            thermcouple. You must read **open_thrmcpl_chans_exist**
            before you read this property. Otherwise, you will receive
            an error.
        """
        cfunc = lib_importer.windll.DAQmxGetReadOpenThrmcplChans
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return unflatten_channel_string(val.value.decode('ascii'))

    @property
    def open_thrmcpl_chans_exist(self):
        """
        bool: Indicates if the device(s) detected an open thermocouple
            connected to any virtual channel in the task. Reading this
            property clears the open thermocouple status for all
            channels in the task. You must read this property before you
            read **open_thrmcpl_chans**. Otherwise, you will receive an
            error.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetReadOpenThrmcplChansExist
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def over_write(self):
        """
        :class:`nidaqmx.constants.OverwriteMode`: Specifies whether to
            overwrite samples in the buffer that you have not yet read.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetReadOverWrite
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return OverwriteMode(val.value)

    @over_write.setter
    def over_write(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetReadOverWrite
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @over_write.deleter
    def over_write(self):
        cfunc = lib_importer.windll.DAQmxResetReadOverWrite
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def overcurrent_chans(self):
        """
        List[str]: Indicates a list of names of any virtual channels in
            the task for which the device(s) detected an overcurrent
            condition. You must read **overcurrent_chans_exist** before
            you read this property. Otherwise, you will receive an
            error. On some devices, you must restart the task for all
            overcurrent channels to recover.
        """
        cfunc = lib_importer.windll.DAQmxGetReadOvercurrentChans
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return unflatten_channel_string(val.value.decode('ascii'))

    @property
    def overcurrent_chans_exist(self):
        """
        bool: Indicates if the device(s) detected an overcurrent
            condition for any virtual channel in the task. Reading this
            property clears the overcurrent status for all channels in
            the task. You must read this property before you read
            **overcurrent_chans**. Otherwise, you will receive an error.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetReadOvercurrentChansExist
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def overloaded_chans(self):
        """
        List[str]: Indicates a list of names of any overloaded virtual
            channels in the task. You must read
            **overloaded_chans_exist** before you read this property.
            Otherwise, you will receive an error.
        """
        cfunc = lib_importer.windll.DAQmxGetReadOverloadedChans
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return unflatten_channel_string(val.value.decode('ascii'))

    @property
    def overloaded_chans_exist(self):
        """
        bool: Indicates if the device(s) detected an overload in any
            virtual channel in the task. Reading this property clears
            the overload status for all channels in the task. You must
            read this property before you read **overloaded_chans**.
            Otherwise, you will receive an error.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetReadOverloadedChansExist
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def overtemperature_chans(self):
        """
        List[str]: Indicates a list of names of any overtemperature
            virtual channels. You must read
            **overtemperature_chans_exist** before you read this
            property. Otherwise, you will receive an error.
        """
        cfunc = lib_importer.windll.DAQmxGetReadOvertemperatureChans
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_char_p,
                        ctypes.c_uint]

        temp_size = 0
        while True:
            val = ctypes.create_string_buffer(temp_size)

            size_or_code = cfunc(
                self._handle, val, temp_size)

            if is_string_buffer_too_small(size_or_code):
                # Buffer size must have changed between calls; check again.
                temp_size = 0
            elif size_or_code > 0 and temp_size == 0:
                # Buffer size obtained, use to retrieve data.
                temp_size = size_or_code
            else:
                break

        check_for_error(size_or_code)

        return unflatten_channel_string(val.value.decode('ascii'))

    @property
    def overtemperature_chans_exist(self):
        """
        bool: Indicates if the device(s) detected an overtemperature
            condition in any virtual channel in the task. Reading this
            property clears the overtemperature status for all channels
            in the task. You must read this property before you read
            **overtemperature_chans**. Otherwise, you will receive an
            error.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetReadOvertemperatureChansExist
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def raw_data_width(self):
        """
        int: Indicates in bytes the size of a raw sample from the task.
        """
        val = ctypes.c_uint()

        cfunc = lib_importer.windll.DAQmxGetReadRawDataWidth
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle,
                        ctypes.POINTER(ctypes.c_uint)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def read_all_avail_samp(self):
        """
        bool: Specifies whether subsequent read operations read all
            samples currently available in the buffer or wait for the
            buffer to become full before reading. NI-DAQmx uses this
            setting for finite acquisitions and only when the number of
            samples to read is -1. For continuous acquisitions when the
            number of samples to read is -1, a read operation always
            reads all samples currently available in the buffer.
        """
        val = c_bool32()

        cfunc = lib_importer.windll.DAQmxGetReadReadAllAvailSamp
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(c_bool32)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @read_all_avail_samp.setter
    def read_all_avail_samp(self, val):
        cfunc = lib_importer.windll.DAQmxSetReadReadAllAvailSamp
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, c_bool32]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @read_all_avail_samp.deleter
    def read_all_avail_samp(self):
        cfunc = lib_importer.windll.DAQmxResetReadReadAllAvailSamp
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def relative_to(self):
        """
        :class:`nidaqmx.constants.ReadRelativeTo`: Specifies the point
            in the buffer at which to begin a read operation. If you
            also specify an offset with **offset**, the read operation
            begins at that offset relative to the point you select with
            this property. The default value is
            **ReadRelativeTo.CURRENT_READ_POSITION** unless you
            configure a Reference Trigger for the task. If you configure
            a Reference Trigger, the default value is
            **ReadRelativeTo.FIRST_PRETRIGGER_SAMPLE**.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetReadRelativeTo
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return ReadRelativeTo(val.value)

    @relative_to.setter
    def relative_to(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetReadRelativeTo
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @relative_to.deleter
    def relative_to(self):
        cfunc = lib_importer.windll.DAQmxResetReadRelativeTo
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def sleep_time(self):
        """
        float: Specifies in seconds the amount of time to sleep after
            checking for available samples if **wait_mode** is
            **WaitMode.SLEEP**.
        """
        val = ctypes.c_double()

        cfunc = lib_importer.windll.DAQmxGetReadSleepTime
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle,
                        ctypes.POINTER(ctypes.c_double)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @sleep_time.setter
    def sleep_time(self, val):
        cfunc = lib_importer.windll.DAQmxSetReadSleepTime
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_double]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @sleep_time.deleter
    def sleep_time(self):
        cfunc = lib_importer.windll.DAQmxResetReadSleepTime
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

    @property
    def total_samp_per_chan_acquired(self):
        """
        long: Indicates the total number of samples acquired by each
            channel. NI-DAQmx returns a single value because this value
            is the same for all channels. For retriggered acquisitions,
            this value is the cumulative number of samples across all
            retriggered acquisitions.
        """
        val = ctypes.c_ulonglong()

        cfunc = lib_importer.windll.DAQmxGetReadTotalSampPerChanAcquired
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle,
                        ctypes.POINTER(ctypes.c_ulonglong)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return val.value

    @property
    def wait_mode(self):
        """
        :class:`nidaqmx.constants.WaitMode`: Specifies how DAQmx Read
            waits for samples to become available.
        """
        val = ctypes.c_int()

        cfunc = lib_importer.windll.DAQmxGetReadWaitMode
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.POINTER(ctypes.c_int)]

        error_code = cfunc(
            self._handle, ctypes.byref(val))
        check_for_error(error_code)

        return WaitMode(val.value)

    @wait_mode.setter
    def wait_mode(self, val):
        val = val.value
        cfunc = lib_importer.windll.DAQmxSetReadWaitMode
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes.c_int]

        error_code = cfunc(
            self._handle, val)
        check_for_error(error_code)

    @wait_mode.deleter
    def wait_mode(self):
        cfunc = lib_importer.windll.DAQmxResetReadWaitMode
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle]

        error_code = cfunc(
            self._handle)
        check_for_error(error_code)

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
        cfunc = lib_importer.windll.DAQmxConfigureLogging
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes.c_int, ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, file_path, logging_mode.value, group_name,
            operation.value)
        check_for_error(error_code)

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

        samples_read, number_of_bytes_per_sample = _read_raw(
            self._handle, numpy_array, num_samps_per_chan,
            self.timeout)

        if samples_read != number_of_samples:
            return numpy_array[:samples_read]
        return numpy_array

    def readall(self):
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

    def readinto(self, numpy_array):
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
                number_of_channels * channels_to_read.ai_raw_samp_size / 8))

        samples_read, _ = _read_raw(
            self._handle, numpy_array, number_of_samples_per_channel,
            self.timeout)

        return samples_read

    def start_new_file(self, file_path):
        """
        Starts a new TDMS file the next time data is written to disk.

        Args:
            file_path (str): Specifies the path to the TDMS file to
                which you want to log data.
        """
        cfunc = lib_importer.windll.DAQmxStartNewFile
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str]

        error_code = cfunc(
            self._handle, file_path)
        check_for_error(error_code)
