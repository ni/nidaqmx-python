from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import re

from nidaqmx.errors import DaqError

# Method logic adapted from
# //Measurements/Infrastructure/dmxf/trunk/2.5/source/nimuck/parseUtilities.cpp

_invalid_range_syntax_message = (
    "Syntax for a range of objects in the input string is invalid.\n\n"
    "For ranges of objects, specify a number immediately before and after "
    "every colon (':') in the input string. Or, if a name is specified after "
    "the colon, it must be identical to the name specified immediately before "
    "the colon. Colons are not allowed within the names of the individual "
    "objects.")


def flatten_channel_string(channel_names):
    """
    Converts a list of channel names to a comma-delimited list of names.

    You can use this method to convert a list of physical or virtual channel
    names to a single string prior to using the DAQmx Create Channel methods or
    instantiating a DAQmx Task object.

    Args:
        channel_names (List[str]): The list of physical or virtual channel
            names.
    Returns:
        str:
        
        The resulting comma-delimited list of physical or virtual channel
        names.
    """
    unflattened_channel_names = []
    for channel_name in channel_names:
        unflattened_channel_names.extend(unflatten_channel_string(channel_name))

    # Go through the channel names and flatten them.
    flattened_channel_list = []
    previous = {
        'base_name': '',
        'start_index': -1,
        'end_index': -1
        }
    for channel_name in unflattened_channel_names:
        m = re.search('(.*[^0-9])?([0-9]+)$', channel_name)
        if not m:
            # If the channel name doesn't end in a valid number, just use the
            # channel name as-is.
            flattened_channel_list.append(
                _channel_info_to_flattened_name(previous))
            previous = {
                'base_name': channel_name,
                'start_index': -1,
                'end_index': -1
                }
        else:
            # If the channel name ends in a valid number, we may need to flatten
            # this channel with subsequent channels in the x:y format.
            current_base_name = m.group(1)
            current_index = int(m.group(2))

            if current_base_name == previous['base_name'] and (
                (current_index == previous['end_index'] + 1 and
                 previous['end_index'] >= previous['start_index']) or
                (current_index == previous['end_index'] - 1 and
                 previous['end_index'] <= previous['start_index'])):
                # If the current channel name has the same base name as the
                # previous and it's end index differs by 1, change the end
                # index value. It gets flattened later.
                previous['end_index'] = current_index
            else:
                # If the current channel name has the same base name as the
                # previous or it's end index differs by more than 1, it doesn't
                # get flattened with the previous channel.
                flattened_channel_list.append(
                    _channel_info_to_flattened_name(previous))
                previous = {
                    'base_name': current_base_name,
                    'start_index': current_index,
                    'end_index': current_index
                    }

    # Convert the final channel dictionary to a flattened string
    flattened_channel_list.append(
        _channel_info_to_flattened_name(previous))

    # Remove empty strings in list, convert to comma-delimited string, then trim
    # whitespace.
    return ','.join([_f for _f in flattened_channel_list if _f]).strip()

    
def _channel_info_to_flattened_name(channel_info):
    """
    Simple method to generate a flattened channel name.
    """
    if channel_info['start_index'] == -1:
        return channel_info['base_name']
    elif channel_info['start_index'] == channel_info['end_index']:
        return '{0}{1}'.format(channel_info['base_name'],
                               channel_info['start_index'])
    else:
        return '{0}{1}:{2}'.format(channel_info['base_name'],
                                   channel_info['start_index'],
                                   channel_info['end_index'])

                                   
def unflatten_channel_string(channel_names):
    """
    Converts a comma-delimited list of channel names to a list of names.

    You can use this method to convert a comma-delimited list or range of
    physical or virtual channels into a list of physical or virtual channel
    names.

    Args:
        channel_names (str): The list or range of physical or virtual channels.
        
    Returns:
        List[str]: 
        
        The list of physical or virtual channel names. Each element of the 
        list contains a single channel.
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

            num_before = int(m_before.group(2))
            num_after = int(m_after.group(2))
            num_max = max([num_before, num_after])
            num_min = min([num_before, num_after])
            number_of_channels = (num_max - num_min) + 1

            if number_of_channels >= 15000:
                raise DaqError(_invalid_range_syntax_message,
                                       error_code=-200498)

            colon_expanded_channel = []
            for i in range(number_of_channels):
                colon_expanded_channel.append(
                    '{0}{1}'.format(m_before.group(1), num_min + i))

            if num_after < num_before:
                colon_expanded_channel.reverse()

            channel_list_to_return.extend(colon_expanded_channel)

    return channel_list_to_return
