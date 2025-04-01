from __future__ import annotations

import re
from dataclasses import dataclass
from typing import List, Optional

from nidaqmx.errors import DaqError
from nidaqmx.grpc_session_options import GrpcSessionOptions
from nidaqmx._base_interpreter import BaseInterpreter


# Method logic adapted from
# //Measurements/Infrastructure/dmxf/trunk/2.5/source/nimuck/parseUtilities.cpp

_invalid_range_syntax_message = (
    "Syntax for a range of objects in the input string is invalid.\n\n"
    "For ranges of objects, specify a number immediately before and after "
    "every colon (':') in the input string. Or, if a name is specified after "
    "the colon, it must be identical to the name specified immediately before "
    "the colon. Colons are not allowed within the names of the individual "
    "objects.")


@dataclass
class _ChannelInfo:
    base_name: str = ""
    start_index: int = -1
    start_index_str: str = ""
    end_index: int = -1
    end_index_str: str = ""

    def to_flattened_name(self) -> str:
        """Convert the channel info to a flattened channel name."""
        if self.start_index == -1:
            return self.base_name
        elif self.start_index == self.end_index:
            return f"{self.base_name}{self.start_index_str}"
        else:
            return f"{self.base_name}{self.start_index_str}:{self.end_index_str}"


def flatten_channel_string(channel_names: list[str]) -> str:
    """
    Converts a list of channel names to a comma-delimited list of names.

    You can use this method to convert a list of physical or virtual channel
    names to a single string prior to using the DAQmx Create Channel methods or
    instantiating a DAQmx Task object.

    Note: For simplicity, this implementation is not fully compatible with the
    NI-DAQmx driver implementation, which is generally more permissive. For
    example, the driver is more graceful with whitespace padding. It was deemed
    valuable to implement this natively in Python, so it can be leveraged in
    workflows that don't have the driver installed. If we have specific examples
    where this approximation is a problem, we can revisit this in the future.

    Args:
        channel_names: The list of physical or virtual channel names.
    Returns:
        The resulting comma-delimited list of physical or virtual channel names.
    """
    unflattened_channel_names = []
    for channel_name in channel_names:
        unflattened_channel_names.extend(unflatten_channel_string(channel_name))

    # Go through the channel names and flatten them.
    flattened_channel_list = []
    previous = _ChannelInfo()
    for channel_name in unflattened_channel_names:
        m = re.search('(.*[^0-9])?([0-9]+)$', channel_name)
        if not m:
            # If the channel name doesn't end in a valid number, just use the
            # channel name as-is.
            flattened_channel_list.append(previous.to_flattened_name())
            previous = _ChannelInfo(channel_name)
        else:
            # If the channel name ends in a valid number, we may need to flatten
            # this channel with subsequent channels in the x:y format.
            current_base_name = m.group(1)
            current_index_str = m.group(2)
            current_index = int(current_index_str)

            if current_base_name == previous.base_name and (
                (current_index == previous.end_index + 1 and
                 previous.end_index >= previous.start_index) or
                (current_index == previous.end_index - 1 and
                 previous.end_index <= previous.start_index)):
                # If the current channel name has the same base name as the
                # previous and it's end index differs by 1, change the end
                # index value. It gets flattened later.
                previous.end_index = current_index
                previous.end_index_str = current_index_str
            else:
                # If the current channel name has the same base name as the
                # previous or it's end index differs by more than 1, it doesn't
                # get flattened with the previous channel.
                flattened_channel_list.append(previous.to_flattened_name())
                previous = _ChannelInfo(
                    current_base_name, 
                    current_index, 
                    current_index_str, 
                    current_index, 
                    current_index_str
                )

    # Convert the final channel dictionary to a flattened string
    flattened_channel_list.append(previous.to_flattened_name())

    # Remove empty strings in list, convert to comma-delimited string, then trim
    # whitespace.
    return ','.join([_f for _f in flattened_channel_list if _f]).strip()

                                   
def unflatten_channel_string(channel_names: str) -> list[str]:
    """
    Converts a comma-delimited list of channel names to a list of names.

    You can use this method to convert a comma-delimited list or range of
    physical or virtual channels into a list of physical or virtual channel
    names.

    Note: For simplicity, this implementation is not fully compatible with the
    NI-DAQmx driver implementation, which is generally more permissive. For
    example, the driver is more graceful with whitespace padding. It was deemed
    valuable to implement this natively in Python, so it can be leveraged in
    workflows that don't have the driver installed. If we have specific examples
    where this approximation is a problem, we can revisit this in the future.

    Args:
        channel_names: The list or range of physical or virtual channels.
        
    Returns:
        The list of physical or virtual channel names. 
        
        Each element of the list contains a single channel.
    """
    channel_list_to_return = []
    channel_list = [c for c in channel_names.strip().split(',') if c]

    for channel in channel_list:
        channel = channel.strip()
        colon_index = channel.find(':')

        if colon_index == -1:
            channel_list_to_return.append(channel)
        else:
            before = channel[:colon_index]
            after = channel[colon_index+1:]

            m_before = re.match('(.*?)([0-9]+)$', before)
            m_after = re.match('(.*?)([0-9]+)$', after)

            if not m_before or not m_after:
                raise DaqError(_invalid_range_syntax_message,
                                       error_code=-200498)

            if m_after.group(1) and (
                m_before.group(1).lower() != m_after.group(1).lower()):
                raise DaqError(_invalid_range_syntax_message,
                               error_code=-200498)

            num_before_str = m_before.group(2)
            num_before = int(num_before_str)
            num_after_str = m_after.group(2)
            num_after = int(num_after_str)

            num_min_width = 0
            # If there are any leading 0s in the first number, we want to ensure
            # match that width. This is established precedence in the DAQmx
            # algorithm.
            if num_before > 0 and len(num_before_str.lstrip('0')) < len(num_before_str):
                num_min_width = len(num_before_str)

            num_max = max([num_before, num_after])
            num_min = min([num_before, num_after])
            number_of_channels = (num_max - num_min) + 1

            if number_of_channels >= 15000:
                raise DaqError(_invalid_range_syntax_message,
                                       error_code=-200498)

            colon_expanded_channel = []
            for i in range(number_of_channels):
                current_number = num_min + i
                if num_min_width > 0:
                    # Using fstrings to create format strings. Braces for days!
                    zero_padded_format_specifier = f"{{:0{num_min_width}d}}"
                    current_number_str = zero_padded_format_specifier.format(current_number)
                else:
                    current_number_str = str(current_number)
                colon_expanded_channel.append(f"{m_before.group(1)}{current_number_str}")

            if num_after < num_before:
                colon_expanded_channel.reverse()

            channel_list_to_return.extend(colon_expanded_channel)

    return channel_list_to_return


def _select_interpreter(
    grpc_options: GrpcSessionOptions | None = None,
    interpreter: BaseInterpreter | None = None
) -> BaseInterpreter:
    if interpreter:
        return interpreter
    else:
        if grpc_options:
            from nidaqmx._grpc_interpreter import GrpcStubInterpreter
            return GrpcStubInterpreter(grpc_options)
        else:
            from nidaqmx._library_interpreter import LibraryInterpreter
            return LibraryInterpreter()
