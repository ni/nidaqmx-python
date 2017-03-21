from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import collections

# region Task Counter IO namedtuples

CtrFreq = collections.namedtuple(
    'CtrFreq', ['freq', 'duty_cycle'])

CtrTick = collections.namedtuple(
    'CtrTick', ['high_tick', 'low_tick'])

CtrTime = collections.namedtuple(
    'CtrTime', ['high_time', 'low_time'])

# endregion

# region Watchdog namedtuples

AOExpirationState = collections.namedtuple(
    'AOExpirationState',
    ['physical_channel', 'expiration_state', 'output_type'])

COExpirationState = collections.namedtuple(
    'COExpirationState', ['physical_channel', 'expiration_state'])

DOExpirationState = collections.namedtuple(
    'DOExpirationState', ['physical_channel', 'expiration_state'])

# endregion

# region Power Up States namedtuples

AOPowerUpState = collections.namedtuple(
    'AOPowerUpState', ['physical_channel', 'power_up_state', 'channel_type'])

DOPowerUpState = collections.namedtuple(
    'DOPowerUpState', ['physical_channel', 'power_up_state'])

DOResistorPowerUpState = collections.namedtuple(
    'DOResistorPowerUpState', ['physical_channel', 'power_up_state'])

# endregion

# region System namedtuples

CDAQSyncConnection = collections.namedtuple(
    'CDAQSyncConnection', ['output_port', 'input_port'])

# endregion

