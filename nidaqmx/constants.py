from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from enum import Enum

# Constants
AUTO = -1
CFG_DEFAULT = -1
DEFAULT = -1
READ_ALL_AVAILABLE = -1
WAIT_INFINITELY = -1.0


# Enums
class ACExcitWireMode(Enum):
    FOUR_WIRE = 4  #: 4-wire.
    FIVE_WIRE = 5  #: 5-wire.
    SIX_WIRE = 6  #: 6-wire.


class ADCTimingMode(Enum):
    AUTOMATIC = 16097  #: Uses the most appropriate supported timing mode based on the Sample Clock Rate.
    HIGH_RESOLUTION = 10195  #: Increases resolution and noise rejection while decreasing conversion rate.
    HIGH_SPEED = 14712  #: Increases conversion rate while decreasing resolution.
    BEST_50_HZ_REJECTION = 14713  #: Improves 50 Hz noise rejection while decreasing noise rejection at other frequencies.
    BEST_60_HZ_REJECTION = 14714  #: Improves 60 Hz noise rejection while decreasing noise rejection at other frequencies.
    CUSTOM = 10137  #: Use **ai_adc_custom_timing_mode** to specify a custom value controlling the tradeoff between speed and resolution.


class AOIdleOutputBehavior(Enum):
    ZERO_VOLTS = 12526  #: Generate 0 V.
    HIGH_IMPEDANCE = 12527  #: Set the channel to high-impedance, effectively disconnecting the analog output circuitry from the I/O connector.
    MAINTAIN_EXISTING_VALUE = 12528  #: Continue generating the current value.


class AOPowerUpOutputBehavior(Enum):
    VOLTAGE = 10322  #: Voltage output.
    CURRENT = 10134  #: Current output.
    HIGH_IMPEDANCE = 12527  #: High-impedance state.


class AccelChargeSensitivityUnits(Enum):
    PICO_COULOMBS_PER_G = 16099  #: PicoCoulombs per g.
    PICO_COULOMBS_PER_METERS_PER_SECOND_SQUARED = 16100  #: PicoCoulombs per m/s^2.
    PICO_COULOMBS_PER_INCHES_PER_SECOND_SQUARED = 16101  #: PicoCoulombs per in/s^2.


class AccelSensitivityUnits(Enum):
    M_VOLTS_PER_G = 12509  #: mVolts/g.
    VOLTS_PER_G = 12510  #: Volts/g.


class AccelUnits(Enum):
    G = 10186  #: 1 g is approximately equal to 9.81 m/s/s.
    METERS_PER_SECOND_SQUARED = 12470  #: Meters per second per second.
    INCHES_PER_SECOND_SQUARED = 12471  #: Inches per second per second.
    FROM_CUSTOM_SCALE = 10065  #: Units a custom scale specifies. If you select this value, you must specify a custom scale name.


class AcquisitionType(Enum):
    FINITE = 10178  #: Acquire or generate a finite number of samples.
    CONTINUOUS = 10123  #: Acquire or generate samples until you stop the task.
    HW_TIMED_SINGLE_POINT = 12522  #: Acquire or generate samples continuously using hardware timing without a buffer. Hardware timed single point sample mode is supported only for the sample clock and change detection timing types.


class Action(Enum):
    COMMIT = 0  #: Commit
    CANCEL = 1  #: Cancel


class ActiveLevel(Enum):
    ABOVE = 10093  #: Pause the measurement or generation while the signal is above the threshold.
    BELOW = 10107  #: Pause the measurement or generation while the signal is below the threshold.


class ActiveOrInactiveEdgeSelection(Enum):
    ACTIVE = 14617  #: Active edges.
    INACTIVE = 14618  #: Inactive edges.


class AngleUnits(Enum):
    DEGREES = 10146  #: Degrees.
    RADIANS = 10273  #: Radians.
    TICKS = 10304  #: Ticks.
    FROM_CUSTOM_SCALE = 10065  #: Units a custom scale specifies. If you select this value, you must specify a custom scale name.


class AngularVelocityUnits(Enum):
    RPM = 16080  #: Revolutions per minute.
    RADIANS_PER_SECOND = 16081  #: Radians per second.
    DEGREES_PER_SECOND = 16082  #: Degrees per second.
    FROM_CUSTOM_SCALE = 10065  #: Units a custom scale specifies. If you select this value, you must specify a custom scale name.


class AutoZeroType(Enum):
    NONE = 10230  #: Do not perform an autozero.
    ONCE = 10244  #: Perform an auto zero at the beginning of the acquisition. This auto zero task might not run if you have used DAQmx Control Task previously in your task.
    EVERY_SAMPLE = 10164  #: Perform an auto zero at every sample of the acquisition.


class BreakMode(Enum):
    NO_ACTION = 10227  #: When advancing to the next entry in the scan list, leave all previous connections intact.
    BREAK_BEFORE_MAKE = 10110  #: When advancing to the next entry in the scan list, disconnect all previous connections before making any new connections.


class BridgeConfiguration(Enum):
    FULL_BRIDGE = 10182  #: Sensor is a full bridge. If you set **ai_excit_use_for_scaling** to True, NI-DAQmx divides the measurement by the excitation value. Many sensors scale data to native units using scaling of volts per excitation.
    HALF_BRIDGE = 10187  #: Sensor is a half bridge. If you set **ai_excit_use_for_scaling** to True, NI-DAQmx divides the measurement by the excitation value. Many sensors scale data to native units using scaling of volts per excitation.
    QUARTER_BRIDGE = 10270  #: Sensor is a quarter bridge. If you set **ai_excit_use_for_scaling** to True, NI-DAQmx divides the measurement by the excitation value. Many sensors scale data to native units using scaling of volts per excitation.
    NO_BRIDGE = 10228  #: Sensor is not a Wheatstone bridge.


class BridgeElectricalUnits(Enum):
    VOLTS_PER_VOLT = 15896  #: Volts per volt.
    M_VOLTS_PER_VOLT = 15897  #: Millivolts per volt.


class BridgePhysicalUnits(Enum):
    NEWTONS = 15875  #: Newtons.
    POUNDS = 15876  #: Pounds.
    KILOGRAM_FORCE = 15877  #: kilograms-force.
    PASCALS = 10081  #: Pascals.
    BAR = 15880  #: Bar.
    POUNDS_PER_SQ_INCH = 15879  #: Pounds per square inch.
    NEWTON_METERS = 15881  #: Newton metres.
    INCH_OUNCES = 15882  #: Ounce-inches.
    INCH_POUNDS = 15883  #: Pound-inches.
    FOOT_POUNDS = 15884  #: Pound-feet.


class BridgeShuntCalSource(Enum):
    BUILT_IN = 10200  #: Use the internal shunt.
    USER_PROVIDED = 10167  #: Use an external shunt.


class BridgeUnits(Enum):
    VOLTS_PER_VOLTS = 15896  #: Volts per volt.
    M_VOLTS_PER_VOLT = 15897  #: Millivolts per volt.
    FROM_CUSTOM_SCALE = 10065  #: Units a custom scale specifies. If you select this value, you must specify a custom scale name.
    FROM_TEDS = 12516  #: Units defined by TEDS information associated with the channel.


class BusType(Enum):
    PCI = 12582  #: PCI.
    PCIE = 13612  #: PCI Express.
    PXI = 12583  #: PXI.
    PXIE = 14706  #: PXI Express.
    SCXI = 12584  #: SCXI.
    SCC = 14707  #: SCC.
    PC_CARD = 12585  #: PC Card/PCMCIA.
    USB = 12586  #: USB.
    UNKNOWN = 12588  #: Unknown bus type.
    COMPACT_DAQ = 14637  #: CompactDAQ.
    TCPIP = 14828  #: TCP/IP.
    SWITCH_BLOCK = 15870  #: SwitchBlock.


class CJCSource(Enum):
    BUILT_IN = 10200  #: Use a cold-junction compensation channel built into the terminal block.
    CONSTANT_USER_VALUE = 10116  #: You must specify the cold-junction temperature.
    SCANNABLE_CHANNEL = 10113  #: Use a channel for cold-junction compensation.


class CalibrationMode2(Enum):
    VOLTAGE = 10322  #: Voltage
    CHARGE = 16105  #: Charge


class CalibrationTerminalConfig(Enum):
    DIFF = 10106  #: Differential
    PSEUDO_DIFF = 12529  #: Pseudodifferential


class ChannelType(Enum):
    ANALOG_INPUT = 10100  #: Analog input channel.
    ANALOG_OUTPUT = 10102  #: Analog output channel.
    DIGITAL_INPUT = 10151  #: Digital input channel.
    DIGITAL_OUTPUT = 10153  #: Digital output channel.
    COUNTER_INPUT = 10131  #: Counter input channel.
    COUNTER_OUTPUT = 10132  #: Counter output channel.


class ChargeUnits(Enum):
    COULOMBS = 16102  #: Coulombs.
    PICO_COULOMBS = 16103  #: PicoCoulombs.
    FROM_CUSTOM_SCALE = 10065  #: Units a custom scale specifies. If you select this value, you must specify a custom scale name.


class ConstrainedGenMode(Enum):
    UNCONSTRAINED = 14708  #: Counter has no restrictions on pulse generation.
    FIXED_HIGH_FREQ = 14709  #: Pulse frequency must be above 7.63 Hz and cannot change while the task runs. In this mode, the duty cycle has 8 bits of resolution.
    FIXED_LOW_FREQ = 14710  #: Pulse frequency must be below 366.21 Hz and cannot change while the task runs. In this mode, the duty cycle has 16 bits of resolution.
    FIXED_50_PERCENT_DUTY_CYCLE = 14711  #: Pulse duty cycle must be 50 percent. The frequency can change while the task runs.


class CountDirection(Enum):
    COUNT_UP = 10128  #: Increment counter.
    COUNT_DOWN = 10124  #: Decrement counter.
    EXTERNAL_SOURCE = 10326  #: The state of a digital line controls the count direction. Each counter has a default count direction terminal.


class CounterFrequencyMethod(Enum):
    LOW_FREQUENCY_1_COUNTER = 10105  #: Use one counter that uses a constant timebase to measure the input signal.
    HIGH_FREQUENCY_2_COUNTERS = 10157  #: Use two counters, one of which counts pulses of the signal to measure during the specified measurement time.
    LARGE_RANGE_2_COUNTERS = 10205  #: Use one counter to divide the frequency of the input signal to create a lower-frequency signal that the second counter can more easily measure.
    DYNAMIC_AVERAGING = 16065  #: Uses one counter and automatically configures the counter settings based on the range of frequencies to be measured. During the acquisition, the counter dynamically adjusts the number of periods that are averaged to balance measurement accuracy and latency.


class Coupling(Enum):
    AC = 10045  #: Remove the DC offset from the signal.
    DC = 10050  #: Allow NI-DAQmx to measure all of the signal.
    GND = 10066  #: Remove the signal from the measurement and measure only ground.


class CurrentShuntResistorLocation(Enum):
    LET_DRIVER_CHOOSE = -1  #: 
    INTERNAL = 10200  #: Use the built-in shunt resistor of the device.
    EXTERNAL = 10167  #: Use a shunt resistor external to the device. You must specify the value of the shunt resistor by using **ai_current_shunt_resistance**.


class CurrentUnits(Enum):
    AMPS = 10342  #: Amperes.
    FROM_CUSTOM_SCALE = 10065  #: Units a custom scale specifies. If you select this value, you must specify a custom scale name.
    FROM_TEDS = 12516  #: Units defined by TEDS information associated with the channel.


class DataJustification(Enum):
    RIGHT = 10279  #: Samples occupy the lower bits of the integer.
    LEFT = 10209  #: Samples occupy the higher bits of the integer.


class DataTransferActiveTransferMode(Enum):
    DMA = 10054  #: Direct Memory Access. Data transfers take place independently from the application.
    INTERRUPT = 10204  #: Data transfers take place independently from the application. Using interrupts increases CPU usage because the CPU must service interrupt requests. Typically, you should use interrupts if the device is out of DMA channels.
    POLLED = 10264  #: Data transfers take place when you call DAQmx Read or DAQmx Write.
    USB_BULK = 12590  #: Data transfers take place independently from the application using a USB bulk pipe.


class DeassertCondition(Enum):
    ON_BOARD_MEMORY_MORE_THAN_HALF_FULL = 10237  #: Deassert the signal when more than half of the onboard memory of the device fills.
    ON_BOARD_MEMORY_FULL = 10236  #: Deassert the signal when the onboard memory fills.
    ONBOARD_MEMORY_CUSTOM_THRESHOLD = 12577  #: Deassert the signal when the amount of space available in the onboard memory is below the value specified with **rdy_for_xfer_event_deassert_cond_custom_threshold**.


class DigitalDriveType(Enum):
    ACTIVE_DRIVE = 12573  #: Drive the output pin to approximately 0 V for logic low and +3.3 V or +5 V, depending on the device, for logic high.
    OPEN_COLLECTOR = 12574  #: Drive the output pin to 0 V for logic low. For logic high, the output driver assumes a high-impedance state and does not drive a voltage.


class DigitalPatternCondition(Enum):
    PATTERN_MATCHES = 10254  #: Trigger when the physical channels match the specified pattern.
    PATTERN_DOES_NOT_MATCH = 10253  #: Trigger when the physical channels do not match the specified pattern.


class DigitalWidthUnits(Enum):
    SAMPLE_CLOCK_PERIODS = 10286  #: Complete periods of the Sample Clock.
    SECONDS = 10364  #: Seconds.
    TICKS = 10304  #: Timebase ticks.


class EddyCurrentProxProbeSensitivityUnits(Enum):
    MIL = 14836  #: mVolts/mil.
    IL = 14837  #: Volts/mil.
    MILLIMETER = 14838  #: mVolts/mMeter.
    ILLIMETER = 14839  #: Volts/mMeter.
    MICRON = 14840  #: mVolts/micron.


class Edge(Enum):
    RISING = 10280  #: Rising edge(s).
    FALLING = 10171  #: Falling edge(s).


class EncoderType(Enum):
    X_1 = 10090  #: If signal A leads signal B, count the rising edges of signal A. If signal B leads signal A, count the falling edges of signal A.
    X_2 = 10091  #: Count the rising and falling edges of signal A.
    X_4 = 10092  #: Count the rising and falling edges of signal A and signal B.
    TWO_PULSE_COUNTING = 10313  #: Two pulse counting.


class EncoderZIndexPhase(Enum):
    AHIGH_BHIGH = 10040  #: Reset the measurement when signal A and signal B are high.
    AHIGH_BLOW = 10041  #: Reset the measurement when signal A is high and signal B is low.
    ALOW_BHIGH = 10042  #: Reset the measurement when signal A is low and signal B high.
    ALOW_BLOW = 10043  #: Reset the measurement when signal A and signal B are low.


class EveryNSamplesEventType(Enum):
    ACQUIRED_INTO_BUFFER = 1  #: Acquired Into Buffer
    TRANSFERRED_FROM_BUFFER = 2  #: Transferred From Buffer


class ExcitationDCorAC(Enum):
    USE_DC = 10050  #: DC excitation.
    USE_AC = 10045  #: AC excitation.


class ExcitationIdleOutputBehavior(Enum):
    ZERO_VOLTS_OR_AMPERES = 12526  #: Drive excitation output to zero.
    MAINTAIN_EXISTING_VALUE = 12528  #: Continue generating the current value.


class ExcitationSource(Enum):
    INTERNAL = 10200  #: Use the built-in excitation source of the device. If you select this value, you must specify the amount of excitation.
    EXTERNAL = 10167  #: Use an excitation source other than the built-in excitation source of the device. If you select this value, you must specify the amount of excitation.
    NONE = 10230  #: Supply no excitation to the channel.


class ExcitationVoltageOrCurrent(Enum):
    USE_VOLTAGE = 10322  #: Voltage excitation.
    USE_CURRENT = 10134  #: Current excitation.


class ExportAction(Enum):
    PULSE = 10265  #: Send a pulse to the terminal.
    TOGGLE = 10307  #: Toggle the state of the terminal from low to high or from high to low.
    LEVEL = 10210  #: The exported Sample Clock goes high at the beginning of the sample and goes low when the last AI Convert begins.
    INTERLOCKED = 12549  #: Handshake Event deasserts after the Handshake Trigger asserts, plus the amount of time specified with **hshk_event_interlocked_deassert_delay**.


class FillMode(Enum):
    GROUP_BY_CHANNEL = 0  #: Group by Channel
    GROUP_BY_SCAN_NUMBER = 1  #: Group by Scan Number


class FilterResponse(Enum):
    CONSTANT_GROUP_DELAY = 16075  #: Constant group delay filter response.
    BUTTERWORTH = 16076  #: Butterworth filter response.
    ELLIPTICAL = 16077  #: Elliptical filter response.
    HARDWARE_DEFINED = 10191  #: Use the hardware-defined filter response.


class FilterType(Enum):
    LOWPASS = 16071  #: Lowpass filter.
    HIGHPASS = 16072  #: Highpass filter.
    BANDPASS = 16073  #: Bandpass filter.
    NOTCH = 16074  #: Notch filter.
    CUSTOM = 10137  #: Custom filter.


class ForceIEPESensorSensitivityUnits(Enum):
    M_VOLTS_PER_POUND = 15892  #: Millivolts per pound.
    M_VOLTS_PER_NEWTON = 15891  #: Millivolts per newton.


class ForceUnits(Enum):
    NEWTONS = 15875  #: Newtons.
    POUNDS = 15876  #: Pounds.
    KILOGRAM_FORCE = 15877  #: Kilograms-force.
    FROM_CUSTOM_SCALE = 10065  #: Units a custom scale specifies. If you select this value, you must specify a custom scale name.


class FrequencyUnits(Enum):
    HZ = 10373  #: Hertz.
    TICKS = 10304  #: Timebase ticks.
    FROM_CUSTOM_SCALE = 10065  #: Units a custom scale specifies. If you select this value, you must specify a custom scale name.


class FuncGenType(Enum):
    SINE = 14751  #: Sine wave.
    TRIANGLE = 14752  #: Triangle wave.
    SQUARE = 14753  #: Square wave.
    SAWTOOTH = 14754  #: Sawtooth wave.


class GpsSignalType(Enum):
    IRIGB = 10070  #: Use the IRIG-B synchronization method. The GPS receiver sends one synchronization pulse per second, as well as information about the number of days, hours, minutes, and seconds that elapsed since the beginning of the current year.
    PPS = 10080  #: Use the PPS synchronization method. The GPS receiver sends one synchronization pulse per second, but does not send any timing information. The timestamp measurement returns the number of seconds that elapsed since the device powered up unless you set **ci_timestamp_initial_seconds**.
    NONE = 10230  #: Do not synchronize the counter to a GPS receiver. The timestamp measurement returns the number of seconds that elapsed since the device powered up unless you set  **ci_timestamp_initial_seconds**.


class HandshakeStartCondition(Enum):
    IMMEDIATE = 10198  #: Device is waiting for space in the FIFO (for acquisition) or waiting for samples (for generation).
    WAIT_FOR_HANDSHAKE_TRIGGER_ASSERT = 12550  #: Device is waiting for the Handshake Trigger to assert.
    WAIT_FOR_HANDSHAKE_TRIGGER_DEASSERT = 12551  #: Device is waiting for the Handshake Trigger to deassert.


class Impedance1(Enum):
    FIFTY_OHMS = 50  #: 50 Ohms.
    SEVENTY_FIVE_OHMS = 75  #: 75 Ohms.
    ONE_M_OHM = 1000000  #: 1 M Ohm.
    TEN_G_OHMS = 10000000000  #: 10 G Ohm.


class InputCalSource(Enum):
    LOOPBACK_0 = 0  #: Loopback 0 degree shift
    LOOPBACK_180 = 1  #: Loopback 180 degree shift
    GROUND = 2  #: Ground


class InputDataTransferCondition(Enum):
    ON_BOARD_MEMORY_MORE_THAN_HALF_FULL = 10237  #: Transfer data from the device when more than half of the onboard memory of the device fills.
    ON_BOARD_MEMORY_NOT_EMPTY = 10241  #: Transfer data from the device when there is data in the onboard memory.
    ONBOARD_MEMORY_CUSTOM_THRESHOLD = 12577  #: Transfer data from the device when the number of samples specified with **ai_data_xfer_custom_threshold** are in the device FIFO.
    WHEN_ACQUISITION_COMPLETE = 12546  #: Transfer data when the acquisition is complete.


class LVDTSensitivityUnits(Enum):
    M_VOLTS_PER_VOLT_PER_MILLIMETER = 12506  #: mVolts/Volt/mMeter.
    M_VOLTS_PER_VOLT_PER_MILLI_INCH = 12505  #: mVolts/Volt/0.001 Inch.


class Language(Enum):
    RAW = -1  #: 
    ENG = 0  #: 
    FRA = 1  #: 
    DEU = 2  #: 
    JPN = 3  #: 
    KOR = 4  #: 
    CHS = 5  #: 


class LengthUnits(Enum):
    METERS = 10219  #: Meters.
    INCHES = 10379  #: Inches.
    TICKS = 10304  #: Ticks.
    FROM_CUSTOM_SCALE = 10065  #: Units a custom scale specifies. If you select this value, you must specify a custom scale name.


class Level(Enum):
    HIGH = 10192  #: Logic high.
    LOW = 10214  #: Logic low.
    NO_CHANGE = 10160  #: Do not change the state of the lines. On some devices, you can select this value only for entire ports.
    TRISTATE = 10310  #: High-impedance state. You can select this state only on devices with bidirectional lines.  You cannot select this state for dedicated digital output lines. On some devices, you can select this value only for entire ports.


class LineGrouping(Enum):
    CHAN_PER_LINE = 0  #: One Channel For Each Line
    CHAN_FOR_ALL_LINES = 1  #: One Channel For All Lines


class LoggingMode(Enum):
    OFF = 10231  #: Disable logging for the task.
    LOG = 15844  #: Enable logging for the task. You cannot read data using DAQmx Read when using this mode. If you require access to the data, read from the TDMS file.
    LOG_AND_READ = 15842  #: Enable both logging and reading data for the task. You must use DAQmx Read to read samples for NI-DAQmx to stream them to disk.


class LoggingOperation(Enum):
    OPEN = 10437  #: Open an existing TDMS file, and append data to that file. If the file does not exist, NI-DAQmx returns an error.
    OPEN_OR_CREATE = 15846  #: Open an existing TDMS file, and append data to that file. If the file does not exist, NI-DAQmx creates a new TDMS file.
    CREATE_OR_REPLACE = 15847  #: Create a new TDMS file, or replace an existing TDMS file.
    CREATE = 15848  #: Create a new TDMS file. If the file already exists, NI-DAQmx returns an error.


class LogicFamily(Enum):
    TWO_POINT_FIVE_V = 14620  #: Compatible with 2.5 V CMOS signals.
    THREE_POINT_THREE_V = 14621  #: Compatible with LVTTL signals.
    FIVE_V = 14619  #: Compatible with TTL and 5 V CMOS signals.


class LogicLvlBehavior(Enum):
    PULL_UP = 16064  #: High logic.
    NONE = 10230  #: Supply no excitation to the channel.


class MIOAIConvertTimebaseSource(Enum):
    SAMPLE_TIMEBASE = 10284  #: Use the same source as Sample Clock timebase.
    EIGHT_M_HZ_TIMEBASE = 16023  #: Use the onboard 8 MHz timebase.
    ONE_HUNDRED_M_HZ_TIMEBASE = 15857  #: Use the onboard 100 MHz timebase.
    MASTER_TIMEBASE = 10282  #: Use the same source as the Master Timebase.
    TWENTY_M_HZ_TIMEBASE = 12537  #: Use the onboard 20 MHz timebase.
    EIGHTY_M_HZ_TIMEBASE = 14636  #: Use the onboard 80 MHz timebase.


class ModulationType(Enum):
    AM = 14756  #: Amplitude modulation.
    FM = 14757  #: Frequency modulation.
    NONE = 10230  #: No modulation.


class OutputDataTransferCondition(Enum):
    ON_BOARD_MEMORY_EMPTY = 10235  #: Transfer data to the device only when there is no data in the onboard memory of the device.
    ON_BOARD_MEMORY_HALF_FULL_OR_LESS = 10239  #: Transfer data to the device any time the onboard memory is less than half full.
    ON_BOARD_MEMORY_LESS_THAN_FULL = 10242  #: Transfer data to the device any time the onboard memory of the device is not full.


class OverflowBehavior(Enum):
    TOP_TASK_AND_ERROR = 15862  #: Stop task and return an error.
    GNORE_OVERRUNS = 15863  #: NI-DAQmx ignores Sample Clock overruns, and the task continues to run.


class OverwriteMode(Enum):
    OVERWRITE_UNREAD_SAMPLES = 10252  #: When an acquisition encounters unread data in the buffer, the acquisition continues and overwrites the unread samples with new ones. You can read the new samples by setting **relative_to** to **ReadRelativeTo.MOST_RECENT_SAMPLE** and setting **offset** to the appropriate number of samples.
    DO_NOT_OVERWRITE_UNREAD_SAMPLES = 10159  #: The acquisition stops when it encounters a sample in the buffer that you have not read.


class PathCapability(Enum):
    PATH_AVAILABLE = 10431  #: 
    PATH_ALREADY_EXISTS = 10432  #: 
    PATH_UNSUPPORTED = 10433  #: 
    CHANNEL_IN_USE = 10434  #: 
    CHANNEL_SOURCE_CONFLICT = 10435  #: 
    CHANNEL_RESERVED_FOR_ROUTING = 10436  #: 


class Polarity(Enum):
    ACTIVE_HIGH = 10095  #: High state is the active state.
    ACTIVE_LOW = 10096  #: Low state is the active state.


class PowerUpChannelType(Enum):
    CHANNEL_VOLTAGE = 0  #: Voltage Channel
    CHANNEL_CURRENT = 1  #: Current Channel
    CHANNEL_HIGH_IMPEDANCE = 2  #: High-Impedance Channel


class PowerUpStates(Enum):
    HIGH = 10192  #: Logic high.
    LOW = 10214  #: Logic low.
    TRISTATE = 10310  #: High-impedance state. You can select this state only on devices with bidirectional lines.  You cannot select this state for dedicated digital output lines. On some devices, you can select this value only for entire ports.


class PressureUnits(Enum):
    PASCALS = 10081  #: Pascals.
    POUNDS_PER_SQ_INCH = 15879  #: Pounds per square inch.
    BAR = 15880  #: Bar.
    FROM_CUSTOM_SCALE = 10065  #: Units a custom scale specifies. If you select this value, you must specify a custom scale name.


class ProductCategory(Enum):
    M_SERIES_DAQ = 14643  #: M Series DAQ.
    X_SERIES_DAQ = 15858  #: X Series DAQ.
    E_SERIES_DAQ = 14642  #: E Series DAQ.
    S_SERIES_DAQ = 14644  #: S Series DAQ.
    B_SERIES_DAQ = 14662  #: B Series DAQ.
    SC_SERIES_DAQ = 14645  #: SC Series DAQ.
    USBDAQ = 14646  #: USB DAQ.
    AO_SERIES = 14647  #: AO Series.
    DIGITAL_IO = 14648  #: Digital I/O.
    TIO_SERIES = 14661  #: TIO Series.
    DSA = 14649  #: Dynamic Signal Acquisition.
    SWITCHES = 14650  #: Switches.
    COMPACT_DAQ_CHASSIS = 14658  #: CompactDAQ chassis.
    C_SERIES_MODULE = 14659  #: C Series I/O module.
    SCXI_MODULE = 14660  #: SCXI module.
    SCC_CONNECTOR_BLOCK = 14704  #: SCC Connector Block.
    SCC_MODULE = 14705  #: SCC Module.
    NIELVIS = 14755  #: NI ELVIS.
    NETWORK_DAQ = 14829  #: Network DAQ.
    SC_EXPRESS = 15886  #: SC Express.
    UNKNOWN = 12588  #: Unknown category.


class RTDType(Enum):
    PT_3750 = 12481  #: Pt3750.
    PT_3851 = 10071  #: Pt3851.
    PT_3911 = 12482  #: Pt3911.
    PT_3916 = 10069  #: Pt3916.
    PT_3920 = 10053  #: Pt3920.
    PT_3928 = 12483  #: Pt3928.
    CUSTOM = 10137  #: You must use **ai_rtd_a**, **ai_rtd_b**, and **ai_rtd_c** to supply the coefficients for the Callendar-Van Dusen equation.


class RVDTSensitivityUnits(Enum):
    M_VPER_VPER_DEGREE = 12507  #: mVolts/Volt/Degree.
    M_VPER_VPER_RADIAN = 12508  #: mVolts/Volt/Radian.


class RawDataCompressionType(Enum):
    NONE = 10230  #: Do not compress samples.
    LOSSLESS_PACKING = 12555  #: Remove unused bits from samples. No resolution is lost.
    LOSSY_LSB_REMOVAL = 12556  #: Remove unused bits from samples. Then, if necessary, remove bits from samples until the samples are the size specified with **ai_lossy_lsb_removal_compressed_samp_size**. This compression type limits resolution to the specified sample size.


class ReadRelativeTo(Enum):
    FIRST_SAMPLE = 10424  #: Start reading samples relative to the first sample acquired.
    CURRENT_READ_POSITION = 10425  #: Start reading samples relative to the last sample returned by the previous read. For the first read operation, this position is the first sample acquired or the first pretrigger sample if you configured a reference trigger for the task.
    REFERENCE_TRIGGER = 10426  #: Start reading samples relative to the first sample after the reference trigger occurred.
    FIRST_PRETRIGGER_SAMPLE = 10427  #: Start reading samples relative to the first pretrigger sample. You specify the number of pretrigger samples to acquire when you configure a reference trigger.
    MOST_RECENT_SAMPLE = 10428  #: Start reading samples relative to the next sample acquired. For example, use this value and set **offset** to -1 to read the last sample acquired.


class RegenerationMode(Enum):
    ALLOW_REGENERATION = 10097  #: Allow NI-DAQmx to regenerate samples that the device previously generated. When you choose this value, the write marker returns to the beginning of the buffer after the device generates all samples currently in the buffer.
    DONT_ALLOW_REGENERATION = 10158  #: Do not allow NI-DAQmx to regenerate samples the device previously generated. When you choose this value, NI-DAQmx waits for you to write more samples to the buffer or until the timeout expires.


class RelayPosition(Enum):
    OPEN = 10437  #: 
    CLOSED = 10438  #: 


class ResistanceConfiguration(Enum):
    TWO_WIRE = 2  #: 2-wire mode.
    THREE_WIRE = 3  #: 3-wire mode.
    FOUR_WIRE = 4  #: 4-wire mode.


class ResistanceUnits(Enum):
    OHMS = 10384  #: Ohms.
    FROM_CUSTOM_SCALE = 10065  #: Units a custom scale specifies. If you select this value, you must specify a custom scale name.
    FROM_TEDS = 12516  #: Units defined by TEDS information associated with the channel.


class ResistorState(Enum):
    PULL_UP = 15950  #: pull up state for pull up/pull down resistors
    PULL_DOWN = 15951  #: pull down state for pull up pull down resistors


class ResolutionType(Enum):
    BITS = 10109  #: Bits.


class SCXI1124Range(Enum):
    ZERO_TO_ONE_V = 14629  #: 
    ZERO_TO_FIVE_V = 14630  #: 
    ZERO_TO_TEN_V = 14631  #: 
    NEG_1_TO_1_V = 14632  #: 
    NEG_5_TO_5_V = 14633  #: 
    NEG_10_TO_10_V = 14634  #: 
    ZERO_TO_TWENTY_M_A = 14635  #: 


class SampClkOverrunBehavior(Enum):
    REPEAT_LAST_SAMPLE = 16062  #: Repeat the last sample.
    RETURN_SENTINEL_VALUE = 16063  #: Return the sentinel value.


class SampleInputDataWhen(Enum):
    HANDSHAKE_TRIGGER_ASSERTS = 12552  #: Latch data when the Handshake Trigger asserts.
    HANDSHAKE_TRIGGER_DEASSERTS = 12553  #: Latch data when the Handshake Trigger deasserts.


class SampleTimingType(Enum):
    SAMPLE_CLOCK = 10388  #: Acquire or generate samples on the specified edge of the sample clock.
    BURST_HANDSHAKE = 12548  #: Determine sample timing using burst handshaking between the device and a peripheral device.
    HANDSHAKE = 10389  #: Determine sample timing by using digital handshaking between the device and a peripheral device.
    IMPLICIT = 10451  #: Configure only the duration of the task.
    ON_DEMAND = 10390  #: Acquire or generate a sample on each read or write operation. This timing type is also referred to as static or software-timed.
    CHANGE_DETECTION = 12504  #: Acquire samples when a change occurs in the state of one or more digital input lines. The lines must be contained within a digital input channel.
    PIPELINED_SAMPLE_CLOCK = 14668  #: Device acquires or generates samples on each sample clock edge, but does not respond to certain triggers until a few sample clock edges later. Pipelining allows higher data transfer rates at the cost of increased trigger response latency.  Refer to the device documentation for information about which triggers pipelining affects. This timing type allows handshaking with some devices using the Pause trigger, the Ready for Transfer event, or the Data Active event. Refer to the device documentation for more information.


class ScaleType(Enum):
    LINEAR = 10447  #: Scale values by using the equation y=mx+b, where x is a prescaled value and y is a scaled value.
    MAP_RANGES = 10448  #: Scale values proportionally from a range of pre-scaled values to a range of scaled values.
    POLYNOMIAL = 10449  #: Scale values by using an Nth order polynomial equation.
    TABLE = 10450  #: Map a list of pre-scaled values to a list of corresponding scaled values, with all other values scaled proportionally.
    NONE = 10230  #: Do not scale electrical values to physical units.
    TWO_POINT_LINEAR = 15898  #: You provide two pairs of electrical values and their corresponding physical values. NI-DAQmx uses those values to calculate the slope and y-intercept of a linear equation and uses that equation to scale electrical values to physical values.


class ScanRepeatMode(Enum):
    FINITE = 10172  #: The task advances through the scan list one time only. NI-DAQmx ignores any Advance Triggers after completing the scan list.
    CONTINUOUS = 10117  #: The task returns to the beginning of the scan list when it reaches the end of the scan list.


class Sense(Enum):
    LOCAL = 16095  #: Local.
    REMOTE = 16096  #: Remote.


class ShuntCalSelect(Enum):
    A = 12513  #: Switch A.
    B = 12514  #: Switch B.
    AAND_B = 12515  #: Switches A and B.


class ShuntElementLocation(Enum):
    R_1 = 12465  #: 
    R_2 = 12466  #: 
    R_3 = 12467  #: 
    R_4 = 14813  #: 
    NONE = 10230  #: 


class ShuntResistorSelect(Enum):
    A = 12513  #: A
    B = 12514  #: B


class Signal(Enum):
    AI_CONVERT_CLOCK = 12484  #: 
    TEN_M_HZ_REF_CLOCK = 12536  #: 
    TWENTY_M_HZ_TIMEBASE_CLOCK = 12486  #: 
    SAMPLE_CLOCK = 12487  #: Timed Loop executes on each active edge of the Sample Clock.
    ADVANCE_TRIGGER = 12488  #: 
    REFERENCE_TRIGGER = 12490  #: 
    START_TRIGGER = 12491  #: 
    ADV_CMPLT_EVENT = 12492  #: 
    AI_HOLD_CMPLT_EVENT = 12493  #: 
    COUNTER_OUTPUT_EVENT = 12494  #: Timed Loop executes each time the Counter Output Event occurs.
    CHANGE_DETECTION_EVENT = 12511  #: Timed Loop executes each time the Change Detection Event occurs.
    WATCHDOG_TIMER_EXPIRED_EVENT = 12512  #: 
    SAMPLE_COMPLETE = 12530  #: Timed Loop executes each time the Sample Complete Event occurs.


class SignalModifiers(Enum):
    DO_NOT_INVERT_POLARITY = 0  #: Do not invert polarity
    INVERT_POLARITY = 1  #: Invert polarity


class Slope(Enum):
    RISING = 10280  #: Trigger on the rising slope of the signal.
    FALLING = 10171  #: Trigger on the falling slope of the signal.


class SoftwareTrigger(Enum):
    ADVANCE_TRIGGER = 12488  #: Place holder enum to make editting internal enum easier.


class SoundPressureUnits(Enum):
    PA = 10081  #: Pascals.
    FROM_CUSTOM_SCALE = 10065  #: Units a custom scale specifies. If you select this value, you must specify a custom scale name.


class SourceSelection(Enum):
    INTERNAL = 10200  #: Internal to the device.
    EXTERNAL = 10167  #: External to the device.


class StrainGageBridgeType(Enum):
    FULL_BRIDGE_I = 10183  #: Four active gages with two pairs subjected to equal and opposite strains.
    FULL_BRIDGE_II = 10184  #: Four active gages with two aligned with maximum principal strain and two Poisson gages in adjacent arms.
    FULL_BRIDGE_III = 10185  #: Four active gages with two aligned with maximum principal strain and two Poisson gages in opposite arms.
    HALF_BRIDGE_I = 10188  #: Two active gages with one aligned with maximum principal strain and one Poisson gage.
    HALF_BRIDGE_II = 10189  #: Two active gages with equal and opposite strains.
    QUARTER_BRIDGE_I = 10271  #: Single active gage.
    QUARTER_BRIDGE_II = 10272  #: Single active gage and one dummy gage.


class StrainGageRosetteMeasurementType(Enum):
    PRINCIPAL_STRAIN_1 = 15971  #: The maximum tensile strain coplanar to the surface of the material under stress.
    PRINCIPAL_STRAIN_2 = 15972  #: The minimum tensile strain coplanar to the surface of the material under stress.
    PRINCIPAL_STRAIN_ANGLE = 15973  #: The angle at which the principal strains of the rosette occur.
    CARTESIAN_STRAIN_X = 15974  #: The tensile strain coplanar to the surface of the material under stress in the X coordinate direction.
    CARTESIAN_STRAIN_Y = 15975  #: The tensile strain coplanar to the surface of the material under stress in the Y coordinate direction.
    CARTESIAN_SHEAR_STRAIN_XY = 15976  #: The tensile strain coplanar to the surface of the material under stress in the XY coordinate direction.
    MAX_SHEAR_STRAIN = 15977  #: The maximum strain coplanar to the cross section of the material under stress.
    MAX_SHEAR_STRAIN_ANGLE = 15978  #: The angle at which the maximum shear strain of the rosette occurs.


class StrainGageRosetteType(Enum):
    RECTANGULAR = 15968  #: A rectangular rosette consists of three strain gages, each separated by a 45 degree angle.
    DELTA = 15969  #: A delta rosette consists of three strain gages, each separated by a 60 degree angle.
    TEE = 15970  #: A tee rosette consists of two gages oriented at 90 degrees with respect to each other.


class StrainUnits(Enum):
    STRAIN = 10299  #: Strain.
    FROM_CUSTOM_SCALE = 10065  #: Units a custom scale specifies. If you select this value, you must specify a custom scale name.


class SwitchChannelUsage(Enum):
    SOURCE_CHANNEL = 10439  #: You can use the channel only as an input for a signal.
    LOAD_CHANNEL = 10440  #: You can use the channel only as the output for a signal passing through the switch.
    RESERVED_FOR_ROUTING_CHANNEL = 10441  #: You can use the channel only to complete routes within a switch.


class SyncType(Enum):
    NONE = 10230  #: Disables trigger skew correction.
    MASTER = 15888  #: Device is the source for shared clocks and triggers.
    SLAVE = 15889  #: Device uses clocks and triggers from the master device.


class TEDSUnits(Enum):
    FROM_CUSTOM_SCALE = 10065  #: Units a custom scale specifies. If you select this value, you must specify a custom scale name.
    FROM_TEDS = 12516  #: Units defined by TEDS information associated with the channel.


class TaskMode(Enum):
    TASK_START = 0  #: Start
    TASK_STOP = 1  #: Stop
    TASK_VERIFY = 2  #: Verify
    TASK_COMMIT = 3  #: Commit
    TASK_RESERVE = 4  #: Reserve
    TASK_UNRESERVE = 5  #: Unreserve
    TASK_ABORT = 6  #: Abort


class TaskStringFormat(Enum):
    INI = 0  #: 
    TAB_DELIMITED = 1  #: 
    JSON = 2  #: 


class TemperatureUnits(Enum):
    DEG_C = 10143  #: Degrees Celsius.
    DEG_F = 10144  #: Degrees Fahrenheit.
    K = 10325  #: Kelvins.
    DEG_R = 10145  #: Degrees Rankine.
    FROM_CUSTOM_SCALE = 10065  #: Units a custom scale specifies. If you select this value, you must specify a custom scale name.


class TerminalConfiguration(Enum):
    DEFAULT = -1  #: Default.
    RSE = 10083  #: Referenced Single-Ended.
    NRSE = 10078  #: Non-Referenced Single-Ended.
    DIFFERENTIAL = 10106  #: Differential.
    PSEUDODIFFERENTIAL = 12529  #: Pseudodifferential.


class ThermocoupleType(Enum):
    J = 10072  #: J-type thermocouple.
    K = 10073  #: K-type thermocouple.
    N = 10077  #: N-type thermocouple.
    R = 10082  #: R-type thermocouple.
    S = 10085  #: S-type thermocouple.
    T = 10086  #: T-type thermocouple.
    B = 10047  #: B-type thermocouple.
    E = 10055  #: E-type thermocouple.


class TimeUnits(Enum):
    SECONDS = 10364  #: Seconds.
    TICKS = 10304  #: Timebase ticks.
    FROM_CUSTOM_SCALE = 10065  #: Units a custom scale specifies. If you select this value, you must specify a custom scale name.


class TorqueUnits(Enum):
    NEWTON_METERS = 15881  #: Newton meters.
    FOOT_POUNDS = 15884  #: Pound-feet.
    INCH_POUNDS = 15883  #: Pound-inches.
    INCH_OUNCES = 15882  #: Ounce-inches.
    FROM_CUSTOM_SCALE = 10065  #: Units a custom scale specifies. If you select this value, you must specify a custom scale name.


class TriggerType(Enum):
    NONE = 10230  #: Disable reference triggering for the task.
    ANALOG_LEVEL = 10101  #: Pause the measurement or generation while an analog signal is above or below a level.
    ANALOG_WINDOW = 10103  #: Trigger when an analog signal enters or leaves a range of values.
    DIGITAL_EDGE = 10150  #: Trigger on a rising or falling edge of a digital pulse.
    DIGITAL_LEVEL = 10152  #: Pause the measurement or generation while a digital signal is at either a high or low state.
    DIGITAL_PATTERN = 10398  #: Pause the measurement or generation while digital physical channels either match or do not match a digital pattern.
    SOFTWARE = 10292  #: Advance to the next entry in a scan list when you call DAQmx Send Software Trigger.
    ANALOG_EDGE = 10099  #: Trigger when an analog signal crosses a threshold.
    INTERLOCKED = 12549  #: Use the Handshake Trigger as a control signal for asynchronous handshaking, such as 8255 handshaking.


class TriggerUsage(Enum):
    ADVANCE = 12488  #: Advance trigger.
    PAUSE = 12489  #: Pause trigger.
    REFERENCE = 12490  #: Reference trigger.
    START = 12491  #: Start trigger.
    HANDSHAKE = 10389  #: Handshake trigger.
    ARM_START = 14641  #: Arm Start trigger.


class UnderflowBehavior(Enum):
    HALT_OUTPUT_AND_ERROR = 14615  #: Stop generating samples and return an error.
    AUSE_UNTIL_DATA_AVAILABLE = 14616  #: Pause the task until samples are available in the FIFO.


class UnitsPreScaled(Enum):
    VOLTS = 10348  #: Volts.
    AMPS = 10342  #: Amperes.
    DEG_F = 10144  #: Degrees Fahrenheit.
    DEG_C = 10143  #: Degrees Celsius.
    DEG_R = 10145  #: Degrees Rankine.
    K = 10325  #: Kelvins.
    STRAIN = 10299  #: Strain.
    OHMS = 10384  #: Ohms.
    HERTZ = 10373  #: Hertz.
    SECONDS = 10364  #: Seconds.
    METERS = 10219  #: Meters.
    INCHES = 10379  #: Inches.
    DEGREES = 10146  #: Degrees.
    RADIANS = 10273  #: Radians.
    TICKS = 10304  #: Ticks.
    RPM = 16080  #: Revolutions per minute.
    RADIANS_PER_SECOND = 16081  #: Radians per second.
    DEGREES_PER_SECOND = 16082  #: Degrees per second.
    G = 10186  #: 1 g is approximately equal to 9.81 m/s/s.
    METERS_PER_SECOND_SQUARED = 12470  #: Meters per second per second.
    INCHES_PER_SECOND_SQUARED = 12471  #: Inches per second per second.
    METERS_PER_SECOND = 15959  #: Meters per second.
    INCHES_PER_SECOND = 15960  #: Inches per second.
    PA = 10081  #: Pascals.
    NEWTONS = 15875  #: Newtons.
    POUNDS = 15876  #: Pounds.
    KILOGRAM_FORCE = 15877  #: Kilograms-force.
    BAR = 15880  #: Bar.
    POUNDS_PER_SQ_INCH = 15879  #: Pounds per square inch.
    NEWTON_METERS = 15881  #: Newton meters.
    INCH_OUNCES = 15882  #: Ounce-inches.
    INCH_POUNDS = 15883  #: Pound-inches.
    FOOT_POUNDS = 15884  #: Pound-feet.
    VOLTS_PER_VOLT = 15896  #: Volts per volt.
    M_VOLTS_PER_VOLT = 15897  #: Millivolts per volt.
    COULOMBS = 16102  #: Coulombs.
    PICO_COULOMBS = 16103  #: PicoCoulombs.
    FROM_TEDS = 12516  #: Units defined by TEDS information associated with the channel.


class UsageTypeAI(Enum):
    VOLTAGE = 10322  #: Voltage measurement.
    VOLTAGE_ACRMS = 10350  #: Voltage RMS measurement.
    VOLTAGE_CUSTOM_WITH_EXCITATION = 10323  #: Voltage measurement with an excitation source. You can use this measurement type for custom sensors that require excitation, but you must use a custom scale to scale the measured voltage.
    CURRENT = 10134  #: Current measurement.
    CURRENT_ACRMS = 10351  #: Current RMS measurement.
    FREQUENCY_VOLTAGE = 10181  #: Frequency measurement using a frequency to voltage converter.
    RESISTANCE = 10278  #: Resistance measurement.
    TEMPERATURE_THERMOCOUPLE = 10303  #: Temperature measurement using a thermocouple.
    TEMPERATURE_THERMISTOR = 10302  #: Temperature measurement using a thermistor.
    TEMPERATURE_BUILT_IN_SENSOR = 10311  #: Temperature measurement using a built-in sensor on a terminal block or device. On SCXI modules, for example, this could be the CJC sensor.
    TEMPERATURE_RTD = 10301  #: Temperature measurement using an RTD.
    POSITION_LINEAR_LVDT = 10352  #: Position measurement using an LVDT.
    POSITION_ANGULAR_RVDT = 10353  #: Position measurement using an RVDT.
    POSITION_EDDY_CURRENT_PROX_PROBE = 14835  #: Position measurement using an eddy current proximity probe.
    SOUND_PRESSURE_MICROPHONE = 10354  #: Sound pressure measurement using a microphone.
    STRAIN_STRAIN_GAGE = 10300  #: Strain measurement.
    ROSETTE_STRAIN_GAGE = 15980  #: Strain measurement using a rosette strain gage.
    ACCELERATION_ACCELEROMETER_CURRENT_INPUT = 10356  #: Acceleration measurement using an accelerometer.
    ACCELERATION_CHARGE = 16104  #: Acceleration measurement using a charge-based sensor.
    ACCELERATION_4_WIRE_DC_VOLTAGE = 16106  #: Acceleration measurement using a 4 wire DC voltage based sensor.
    VELOCITY_IEPE_SENSOR = 15966  #: Velocity measurement using an IEPE Sensor.
    FORCE_IEPE_SENSOR = 15895  #: Force measurement using an IEPE Sensor.
    FORCE_BRIDGE = 15899  #: Force measurement using a bridge-based sensor.
    BRIDGE = 15908  #: Measure voltage ratios from a Wheatstone bridge.
    TORQUE_BRIDGE = 15905  #: Torque measurement using a bridge-based sensor.
    PRESSURE_BRIDGE = 15902  #: Pressure measurement using a bridge-based sensor.
    TEDS = 12531  #: Measurement type defined by TEDS.
    CHARGE = 16105  #: Charge measurement.


class UsageTypeAO(Enum):
    VOLTAGE = 10322  #: Voltage generation.
    CURRENT = 10134  #: Current generation.
    FUNCTION_GENERATION = 14750  #: Function generation.


class UsageTypeCI(Enum):
    FREQUENCY = 10179  #: Measure the frequency of a digital signal.
    PERIOD = 10256  #: Measure the period of a digital signal.
    PULSE_WIDTH_DIGITAL = 10359  #: Measure the width of a pulse of a digital signal.
    PULSE_WIDTH_DIGITAL_TWO_EDGE_SEPARATION = 10267  #: Measure time between edges of two digital signals.
    PULSE_WIDTH_DIGITAL_SEMI_PERIOD = 10289  #: Measure the time between state transitions of a digital signal.
    PULSE_FREQ = 15864  #: Pulse measurement, returning the result as frequency and duty cycle.
    PULSE_TIME = 15865  #: Pulse measurement, returning the result as high time and low time.
    PULSE_TICKS = 15866  #: Pulse measurement, returning the result as high ticks and low ticks.
    COUNT_EDGES = 10125  #: Count edges of a digital signal.
    POSITION_ANGULAR_ENCODER = 10360  #: Angular position measurement using an angular encoder.
    POSITION_LINEAR_ENCODER = 10361  #: Linear position measurement using a linear encoder.
    TIME_GPS = 10362  #: Timestamp measurement, synchronizing the counter to a GPS receiver.
    DUTY_CYCLE = 16070  #: Measure the duty cycle of a digital signal.
    VELOCITY_ANGULAR_ENCODER = 16078  #: Angular velocity measurement using an angular encoder.
    VELOCITY_LINEAR_ENCODER = 16079  #: Linear velocity measurement using a linear encoder.


class UsageTypeCO(Enum):
    PULSE_TIME = 10269  #: Generate pulses defined by the time the pulse is at a low state and the time the pulse is at a high state.
    PULSE_FREQUENCY = 10119  #: Generate digital pulses defined by frequency and duty cycle.
    PULSE_TICKS = 10268  #: Generate digital pulses defined by the number of timebase ticks that the pulse is at a low state and the number of timebase ticks that the pulse is at a high state.


class VelocityIEPESensorSensitivityUnits(Enum):
    M_VOLTS_PER_MILLIMETER_PER_SECOND = 15963  #: Millivolts per millimeter per second.
    M_VOLTS_PER_INCH_PER_SECOND = 15964  #: Millivolts per inch per second.


class VelocityUnits(Enum):
    METERS_PER_SECOND = 15959  #: Meters per second.
    INCHES_PER_SECOND = 15960  #: Inches per second.
    FROM_CUSTOM_SCALE = 10065  #: Units a custom scale specifies. If you select this value, you must specify a custom scale name.


class VoltageUnits(Enum):
    VOLTS = 10348  #: Volts.
    FROM_CUSTOM_SCALE = 10065  #: Units a custom scale specifies. If you select this value, you must specify a custom scale name.
    FROM_TEDS = 12516  #: Units defined by TEDS information associated with the channel.


class WDTTaskAction(Enum):
    RESET_TIMER = 0  #: Reset Timer
    CLEAR_EXPIRATION = 1  #: Clear Expiration


class WaitMode(Enum):
    WAIT_FOR_INTERRUPT = 12523  #: Check for available samples when the system receives an interrupt service request. This mode is the most CPU efficient, but results in lower possible sampling rates.
    POLL = 12524  #: Repeatedly check for available samples as fast as possible. This mode allows for the highest sampling rates at the expense of CPU efficiency.
    YIELD = 12525  #: Repeatedly check for available samples, but yield control to other threads after each check. This mode offers a balance between sampling rate and CPU efficiency.
    SLEEP = 12547  #: Check for available samples once per the amount of time specified in **sleep_time**.


class WatchdogAOExpirState(Enum):
    VOLTAGE = 10322  #: Voltage output.
    CURRENT = 10134  #: Current output.
    NO_CHANGE = 10160  #: Expiration does not affect the port. Do not change the state of any lines in the port, and do not lock the port.


class WatchdogCOExpirState(Enum):
    LOW = 10214  #: Low logic.
    HIGH = 10192  #: High logic.
    NO_CHANGE = 10160  #: Expiration does not affect the state of the counter output. The channels retain their states at the time of the watchdog timer expiration, and no further counter generation runs.


class WaveformAttributes(Enum):
    SAMPLES_ONLY = 10287  #: Return only samples.
    SAMPLES_AND_TIMING = 10140  #: Return the samples and timing information.
    SAMPLES_TIMING_AND_ATTRIBUTES = 10141  #: Return the samples, timing information, and other attributes, such as the name of the channel.


class WindowTriggerCondition1(Enum):
    ENTERING_WINDOW = 10163  #: Trigger when the signal enters the window.
    LEAVING_WINDOW = 10208  #: Trigger when the signal leaves the window.


class WindowTriggerCondition2(Enum):
    INSIDE_WINDOW = 10199  #: Pause the measurement or generation while the trigger is inside the window.
    OUTSIDE_WINDOW = 10251  #: Pause the measurement or generation while the signal is outside the window.


class WriteBasicTEDSOptions(Enum):
    WRITE_TO_EEPROM = 12538  #: blah
    WRITE_TO_PROM = 12539  #: blah
    DO_NOT_WRITE = 12540  #: blah


class WriteRelativeTo(Enum):
    FIRST_SAMPLE = 10424  #: Write samples relative to the first sample.
    CURRENT_WRITE_POSITION = 10430  #: Write samples relative to the current position in the buffer.


class _Callback(Enum):
    SYNCHRONOUS_EVENT_CALLBACKS = 1  #: Synchronous callbacks


class _CouplingTypes(Enum):
    AC = 1  #: Device supports AC coupling
    DC = 2  #: Device supports DC coupling
    GND = 4  #: Device supports ground coupling
    HF_REJECT = 8  #: Device supports High Frequency Reject coupling
    LF_REJECT = 16  #: Device supports Low Frequency Reject coupling
    NOISE_REJECT = 32  #: Device supports Noise Reject coupling


class _Save(Enum):
    OVERWRITE = 1  #: 
    ALLOW_INTERACTIVE_EDITING = 2  #: 
    ALLOW_INTERACTIVE_DELETION = 4  #: 


class _TermCfg(Enum):
    RSE = 1  #: RSE terminal configuration
    NRSE = 2  #: NRSE terminal configuration
    DIFFERENTIAL = 4  #: Differential terminal configuration
    PSEUDODIFFERENTIAL = 8  #: Pseudodifferential terminal configuration


class _TriggerUsageTypes(Enum):
    ADVANCE = 1  #: Device supports advance triggers
    PAUSE = 2  #: Device supports pause triggers
    REFERENCE = 4  #: Device supports reference triggers
    START = 8  #: Device supports start triggers
    HANDSHAKE = 16  #: Device supports handshake triggers
    ARM_START = 32  #: Device supports arm start triggers
