import collections
import typing

# region Task Counter IO namedtuples

CtrFreq = collections.namedtuple(
    'CtrFreq', ['freq', 'duty_cycle'])

CtrTick = collections.namedtuple(
    'CtrTick', ['high_tick', 'low_tick'])

CtrTime = collections.namedtuple(
    'CtrTime', ['high_time', 'low_time'])

# endregion

# region Power IO namedtuples

PowerMeasurement = collections.namedtuple(
    'PowerMeasurement', ['voltage', 'current'])

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

# region ID Pin namedtuples

class IDPinContents(typing.NamedTuple):
    """IDPinContents represent the contents of the memory connected to the ID pin."""

    data: list[int]
    """The binary data stored on the memory connected to the ID pin."""

    format_code: int
    """The format code of the binary data."""

# endregion
