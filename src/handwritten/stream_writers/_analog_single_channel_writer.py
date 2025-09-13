from __future__ import annotations

from typing import Any

from nitypes.waveform import AnalogWaveform

from nidaqmx._feature_toggles import WAVEFORM_SUPPORT, requires_feature
from nidaqmx.constants import FillMode
from nidaqmx.stream_writers._channel_writer_base import (
    AUTO_START_UNSET,
    ChannelWriterBase,
)


class AnalogSingleChannelWriter(ChannelWriterBase):
    """Writes samples to an analog output channel in an NI-DAQmx task."""

    def write_many_sample(self, data, timeout=10.0):
        """Writes one or more floating-point samples to a single analog output channel in a task.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            data (numpy.ndarray): Contains a 1D NumPy array of
                floating-point samples to write to the task. Each
                element of the array corresponds to a sample to write.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.

        Returns:
            int:

            Specifies the actual number of samples this method
            successfully wrote.
        """
        self._verify_array(data, False, True)

        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else False

        return self._interpreter.write_analog_f64(
            self._handle, data.shape[0], auto_start, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

    def write_one_sample(self, data, timeout=10):
        """Writes a single floating-point sample to a single analog output channel in a task.

        Args:
            data (float): Specifies the floating-point sample to write
                to the task.
            auto_start (Optional[bool]): Specifies if this method
                automatically starts the task if you did not explicitly
                start it with the DAQmx Start Task method.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.
        """
        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else True

        return self._interpreter.write_analog_scalar_f64(self._handle, auto_start, timeout, data)

    @requires_feature(WAVEFORM_SUPPORT)
    def write_waveform(self, waveform: AnalogWaveform[Any], timeout: float = 10.0) -> int:
        """Writes a waveform to a single analog output channel in a task.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            waveform (AnalogWaveform[Any]): Specifies the
                waveform to write to the task.
            timeout (Optional[float]): Specifies the amount of time in
                seconds to wait for the method to write all samples.
                NI-DAQmx performs a timeout check only if the method
                must wait before it writes data. This method returns an
                error if the time elapses. The default timeout is 10
                seconds. If you set timeout to
                nidaqmx.constants.WAIT_INFINITELY, the method waits
                indefinitely. If you set timeout to 0, the method tries
                once to write the submitted samples. If the method could
                not write all the submitted samples, it returns an error
                and the number of samples successfully written.

        Returns:
            int: Specifies the actual number of samples this method
            successfully wrote.
        """
        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else False

        return self._interpreter.write_analog_waveform(self._handle, waveform, auto_start, timeout)
