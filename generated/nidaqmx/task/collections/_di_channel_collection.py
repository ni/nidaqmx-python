# Do not edit this file; it was automatically generated.

from nidaqmx.errors import DaqFunctionNotSupportedError
from nidaqmx.task.channels._di_channel import DIChannel
from nidaqmx.task.collections._channel_collection import ChannelCollection
from nidaqmx.utils import unflatten_channel_string
from nidaqmx.constants import (
    LineGrouping)


class DIChannelCollection(ChannelCollection):
    """
    Contains the collection of digital input channels for a DAQmx Task.
    """
    def __init__(self, task_handle, interpreter):
        """
        Do not construct this object directly; instead, construct a nidaqmx.Task and use the task.di_channels property.
        """
        super().__init__(task_handle, interpreter)

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
            nidaqmx.task.channels.DIChannel: 
            
            Specifies the newly created DIChannel object.
        """
        # Attempt to retrieve the last created channel name. This is only supported on DAQmx 24Q3+ with the library
        # interpreter.
        virtual_channel_name = None
        try:
            virtual_channel_name = self._interpreter.internal_get_last_created_chan()
        except (NotImplementedError, DaqFunctionNotSupportedError):
            pass

        # Fallback implementation is sometimes incorrect.
        if virtual_channel_name is None:
            unflattened_lines = unflatten_channel_string(lines)
            num_lines = len(unflattened_lines)
            
            if line_grouping == LineGrouping.CHAN_FOR_ALL_LINES:
                if name_to_assign_to_lines:
                    virtual_channel_name = name_to_assign_to_lines
                elif num_lines == 1:
                    virtual_channel_name = lines
                else:
                    virtual_channel_name = unflattened_lines[0] + '...'
            else:
                if name_to_assign_to_lines:
                    if num_lines > 1:
                        virtual_channel_name = '{}0:{}'.format(
                            name_to_assign_to_lines, num_lines-1)
                    else:
                        virtual_channel_name = name_to_assign_to_lines
                else:
                    virtual_channel_name = lines

        return DIChannel(self._handle, virtual_channel_name, self._interpreter)

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
            nidaqmx.task.channels.DIChannel:

            Indicates the newly created channel object.
        """

        self._interpreter.create_di_chan(
            self._handle, lines, name_to_assign_to_lines, line_grouping.value)

        return self._create_chan(lines, line_grouping, name_to_assign_to_lines)

