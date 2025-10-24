from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from nitypes.waveform import DigitalWaveform

from nidaqmx._feature_toggles import WAVEFORM_SUPPORT, requires_feature
from nidaqmx.constants import FillMode
from nidaqmx.stream_writers._channel_writer_base import (
    AUTO_START_UNSET,
    ChannelWriterBase,
)


class DigitalMultiChannelWriter(ChannelWriterBase):
    """Writes samples to one or more digital output channels in an NI-DAQmx task."""

    def write_many_sample_port_byte(self, data, timeout=10.0):
        """Writes 8-bit unsigned integer samples to one or more digital output channels in a task.

        Use this method for devices with up to 8 lines per port.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            data (numpy.ndarray): Contains a 2D NumPy array of 8-bit
                unsigned integer samples to write to the task.

                Each row corresponds to a channel in the task. Each
                column corresponds to a sample to write to each channel.
                The order of the channels in the array corresponds to
                the order in which you add the channels to the task.
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
            successfully wrote to each channel in the task.
        """
        self._verify_array(data, True, True)

        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else False

        return self._interpreter.write_digital_u8(
            self._handle, data.shape[1], auto_start, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

    def write_many_sample_port_uint16(self, data, timeout=10.0):
        """Writes 16-bit unsigned integer samples to one or more digital output channels in a task.

        Use this method for devices with up to 16 lines per port.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            data (numpy.ndarray): Contains a 2D NumPy array of 16-bit
                unsigned integer samples to write to the task.

                Each row corresponds to a channel in the task. Each
                column corresponds to a sample to write to each channel.
                The order of the channels in the array corresponds to
                the order in which you add the channels to the task.
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
            successfully wrote to each channel in the task.
        """
        self._verify_array(data, True, True)

        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else False

        return self._interpreter.write_digital_u16(
            self._handle, data.shape[1], auto_start, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

    def write_many_sample_port_uint32(self, data, timeout=10.0):
        """Writes 32-bit unsigned integer samples to one or more digital output channels in a task.

        Use this method for devices with up to 32 lines per port.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            data (numpy.ndarray): Contains a 2D NumPy array of 32-bit
                unsigned integer samples to write to the task.

                Each row corresponds to a channel in the task. Each
                column corresponds to a sample to write to each channel.
                The order of the channels in the array corresponds to
                the order in which you add the channels to the task.
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
            successfully wrote to each channel in the task.
        """
        self._verify_array(data, True, True)

        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else False

        return self._interpreter.write_digital_u32(
            self._handle, data.shape[1], auto_start, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

    def write_one_sample_multi_line(self, data, timeout=10):
        """Writes a single boolean sample to one or more digital output channels in a task.

        The channel can contain multiple digital lines.

        Args:
            data (numpy.ndarray): Contains a 2D NumPy array of boolean
                samples to write to the task.

                Each row corresponds to a channel in the task. Each
                column corresponds to a line from each channel. The
                order of the channels in the array corresponds to the
                order in which you add the channels to the task.
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
        self._verify_array_digital_lines(data, True, True)

        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else True

        return self._interpreter.write_digital_lines(
            self._handle, 1, auto_start, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

    def write_one_sample_one_line(self, data, timeout=10):
        """Writes a single boolean sample to one or more digital output channels in a task.

        The channel can contain only one digital line.

        Args:
            data (numpy.ndarray): Contains a 1D NumPy array of boolean
                samples to write to the task.

                Each element in the array corresponds to a channel in
                the task. The order of the channels in the array
                corresponds to the order in which you add the channels
                to the task.
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
        self._verify_array_digital_lines(data, True, False)

        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else True

        return self._interpreter.write_digital_lines(
            self._handle, 1, auto_start, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

    def write_one_sample_port_byte(self, data, timeout=10):
        """Writes a single 8-bit unsigned integer sample to one or more digital output channels.

        Use this method for devices with up to 8 lines per port.

        Args:
            data (numpy.ndarray): Contains a 1D NumPy array of 8-bit
                unsigned integer samples to write to the task.

                Each element in the array corresponds to a channel in
                the task. The order of the channels in the array
                corresponds to the order in which you add the channels
                to the task.
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
        self._verify_array(data, True, False)

        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else True

        return self._interpreter.write_digital_u8(
            self._handle, 1, auto_start, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

    def write_one_sample_port_uint16(self, data, timeout=10):
        """Writes a single 16-bit unsigned integer sample to one or more digital output channels.

        Use this method for devices with up to 16 lines per port.

        Args:
            data (numpy.ndarray): Contains a 1D NumPy array of 16-bit
                unsigned integer samples to write to the task.

                Each element in the array corresponds to a channel in
                the task. The order of the channels in the array
                corresponds to the order in which you add the channels
                to the task.
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
        self._verify_array(data, True, False)

        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else True

        return self._interpreter.write_digital_u16(
            self._handle, 1, auto_start, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

    def write_one_sample_port_uint32(self, data, timeout=10):
        """Writes a single 32-bit unsigned integer sample to one or more digital output channels.

        Use this method for devices with up to 32 lines per port.

        Args:
            data (numpy.ndarray): Contains a 1D NumPy array of 32-bit
                unsigned integer samples to write to the task.

                Each element in the array corresponds to a channel in
                the task. The order of the channels in the array
                corresponds to the order in which you add the channels
                to the task.
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
        self._verify_array(data, True, False)

        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else True

        return self._interpreter.write_digital_u32(
            self._handle, 1, auto_start, timeout, FillMode.GROUP_BY_CHANNEL.value, data
        )

    @requires_feature(WAVEFORM_SUPPORT)
    def write_waveforms(
        self, waveforms: Sequence[DigitalWaveform[Any]], timeout: float = 10.0
    ) -> int:
        """Writes waveforms to one or more digital output channels in a task.

        If the task uses on-demand timing, this method returns only
        after the device generates all samples. On-demand is the default
        timing type if you do not use the timing property on the task to
        configure a sample timing type. If the task uses any timing type
        other than on-demand, this method returns immediately and does
        not wait for the device to generate all samples. Your
        application must determine if the task is done to ensure that
        the device generated all samples.

        Args:
            waveforms (Sequence[DigitalWaveform[Any]]): Specifies the
                waveforms to write to the task.
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
            int: Specifies the actual number of samples per channel this method
            successfully wrote.
        """
        auto_start = self._auto_start if self._auto_start is not AUTO_START_UNSET else False

        return self._interpreter.write_digital_waveforms(
            self._handle, waveforms, auto_start, timeout
        )
