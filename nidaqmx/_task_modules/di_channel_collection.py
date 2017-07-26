from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import ctypes
import numpy

from nidaqmx._lib import lib_importer, ctypes_byte_str
from nidaqmx.errors import check_for_error
from nidaqmx._task_modules.channels.di_channel import DIChannel
from nidaqmx._task_modules.channel_collection import ChannelCollection
from nidaqmx.utils import unflatten_channel_string
from nidaqmx.constants import (
    LineGrouping)


class DIChannelCollection(ChannelCollection):
    """
    Contains the collection of digital input channels for a DAQmx Task.
    """
    def __init__(self, task_handle):
        super(DIChannelCollection, self).__init__(task_handle)

    def _create_chan(self, lines, line_grouping, name_to_assign_to_lines=''):
        """
        Creates and returns a DIChannel object.

        Args:
            lines (str): Specifies the names of the lines to use to 
                create virtual channels.
            line_grouping (Optional[nidaqmx.constants.LineGrouping]):
                Specifies how to group digital lines into one or more
                virtual channels.
            name_to_assign_to_lines (Optional[str]): Specifies a name to 
                assign to the virtual channel this method creates.
        Returns:
            nidaqmx._task_modules.channels.di_channel.DIChannel: 
            
            Specifies the newly created DIChannel object.
        """
        unflattened_lines = unflatten_channel_string(lines)
        num_lines = len(unflattened_lines)
        
        if line_grouping == LineGrouping.CHAN_FOR_ALL_LINES:
            if name_to_assign_to_lines or num_lines == 1:
                name = lines
            else:
                name = unflattened_lines[0] + '...'
        else:
            if name_to_assign_to_lines:
                if num_lines > 1:
                    name = '{0}0:{1}'.format(
                        name_to_assign_to_lines, num_lines-1)
                else:
                    name = name_to_assign_to_lines
            else:
                name = lines

        return DIChannel(self._handle, name)

    def add_di_chan(
            self, lines, name_to_assign_to_lines="",
            line_grouping=LineGrouping.CHAN_FOR_ALL_LINES):
        """
        Creates channel(s) to measure digital signals. You can group
        digital lines into one digital channel or separate them into
        multiple digital channels. If you specify one or more entire
        ports in the **lines** input by using port physical channel
        names, you cannot separate the ports into multiple channels. To
        separate ports into multiple channels, use this function
        multiple times with a different port each time.

        Args:
            lines (str): Specifies the names of the digital lines or
                ports to use to create virtual channels. The DAQmx
                physical channel constant lists all lines and ports for
                devices installed in the system.
            name_to_assign_to_lines (Optional[str]): Specifies a name to
                assign to the virtual channel this function creates. If
                you do not specify a value for this input, NI-DAQmx uses
                the physical channel name as the virtual channel name.
            line_grouping (Optional[nidaqmx.constants.LineGrouping]): 
                Specifies how to group digital lines into one or more
                virtual channels. If you specify one or more entire
                ports with the **lines** input, you must set this input
                to **one channel for all lines**.
        Returns:
            nidaqmx._task_modules.channels.di_channel.DIChannel:
            
            Indicates the newly created channel object.
        """
        cfunc = lib_importer.windll.DAQmxCreateDIChan
        if cfunc.argtypes is None:
            with cfunc.arglock:
                if cfunc.argtypes is None:
                    cfunc.argtypes = [
                        lib_importer.task_handle, ctypes_byte_str,
                        ctypes_byte_str, ctypes.c_int]

        error_code = cfunc(
            self._handle, lines, name_to_assign_to_lines, line_grouping.value)
        check_for_error(error_code)

        return self._create_chan(lines, line_grouping, name_to_assign_to_lines)

