import typing

import nidaqmx.constants

# region Task Counter IO named tuples

class CtrFreq(typing.NamedTuple):
    freq: float
    duty_cycle: float

class CtrTick(typing.NamedTuple):
    high_tick: int
    low_tick: int

class CtrTime(typing.NamedTuple):
    high_time: float
    low_time: float

# endregion

# region Power IO named tuples

class PowerMeasurement(typing.NamedTuple):
    voltage: float
    current: float

# endregion

# region Watchdog named tuples

class AOExpirationState(typing.NamedTuple):
    physical_channel: str
    expiration_state: float
    output_type: nidaqmx.constants.WatchdogAOExpirState

class COExpirationState(typing.NamedTuple):
    physical_channel: str
    expiration_state: nidaqmx.constants.WatchdogCOExpirState

class DOExpirationState(typing.NamedTuple):
    physical_channel: str
    expiration_state: bool

# endregion

# region Power Up States named tuples

class AOPowerUpState(typing.NamedTuple):
    physical_channel: str
    power_up_state: float
    channel_type: nidaqmx.constants.AOPowerUpOutputBehavior

class DOPowerUpState(typing.NamedTuple):
    physical_channel: str
    power_up_state: nidaqmx.constants.PowerUpStates

class DOResistorPowerUpState(typing.NamedTuple):
    physical_channel: str
    power_up_state: nidaqmx.constants.ResistorState

# endregion

# region System named tuples

class CDAQSyncConnection(typing.NamedTuple):
    output_port: str
    input_port: str

# endregion

