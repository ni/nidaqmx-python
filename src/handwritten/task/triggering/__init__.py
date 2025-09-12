"""NI-DAQmx task triggering classes."""

from nidaqmx.task.triggering._arm_start_trigger import ArmStartTrigger
from nidaqmx.task.triggering._handshake_trigger import HandshakeTrigger
from nidaqmx.task.triggering._pause_trigger import PauseTrigger
from nidaqmx.task.triggering._reference_trigger import ReferenceTrigger
from nidaqmx.task.triggering._start_trigger import StartTrigger
from nidaqmx.task.triggering._triggers import Triggers

__all__ = [
    "Triggers",
    "ArmStartTrigger",
    "HandshakeTrigger",
    "PauseTrigger",
    "ReferenceTrigger",
    "StartTrigger",
]
