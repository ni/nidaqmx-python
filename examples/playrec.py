"""Simultaneous read and write with NI USB-4431 or similar device."""

import numpy as np

import nidaqmx as ni
from nidaqmx.constants import WAIT_INFINITELY


def query_devices():
    """Queries all the device information connected to the local system."""
    local = ni.system.System.local()
    for device in local.devices:
        print(f"Device Name: {device.name}, Product Type: {device.product_type}")
        print("Input channels:", [chan.name for chan in device.ai_physical_chans])
        print("Output channels:", [chan.name for chan in device.ao_physical_chans])


def playrec(data, samplerate, input_mapping, output_mapping):
    """Simultaneous playback and recording though NI device.

    Parameters:
    -----------
    data: array_like, shape (nsamples, len(output_mapping))
      Data to be send to output channels.
    samplerate: int
      Samplerate
    input_mapping: list of str
      Input device channels
    output_mapping: list of str
      Output device channels

    Returns
    -------
    ndarray, shape (nsamples, len(input_mapping))
      Recorded data

    """
    devices = ni.system.System.local().devices
    data = np.asarray(data).T
    nsamples = data.shape[1]

    with ni.Task() as read_task, ni.Task() as write_task:
        for i, o in enumerate(output_mapping):
            aochan = write_task.ao_channels.add_ao_voltage_chan(
                o,
                min_val=devices[o].ao_voltage_rngs[0],
                max_val=devices[o].ao_voltage_rngs[1],
            )
            min_data, max_data = np.min(data[i]), np.max(data[i])
            if ((max_data > aochan.ao_max) | (min_data < aochan.ao_min)).any():
                raise ValueError(
                    f"Data range ({min_data:.2f}, {max_data:.2f}) exceeds output range of "
                    f"{o} ({aochan.ao_min:.2f}, {aochan.ao_max:.2f})."
                )
        for i in input_mapping:
            read_task.ai_channels.add_ai_voltage_chan(i)

        for task in (read_task, write_task):
            task.timing.cfg_samp_clk_timing(
                rate=samplerate, source="OnboardClock", samps_per_chan=nsamples
            )

        # trigger write_task as soon as read_task starts
        write_task.triggers.start_trigger.cfg_dig_edge_start_trig(
            read_task.triggers.start_trigger.term
        )
        # squeeze as Task.write expects 1d array for 1 channel
        write_task.write(data.squeeze(), auto_start=False)
        # write_task doesn't start at read_task's start_trigger without this
        write_task.start()
        # do not time out for long inputs
        indata = read_task.read(nsamples, timeout=WAIT_INFINITELY)

    return np.asarray(indata).T


if __name__ == "__main__":
    query_devices()
    # Prints in this example:
    #   Device Name: Dev2, Product Type: USB-4431
    #   Input channels: ['Dev2/ai0', 'Dev2/ai1', 'Dev2/ai2', 'Dev2/ai3']
    #   Output channels: ['Dev2/ao0']

    # excite through one output and record at three inputs
    outdata = np.random.normal(size=(5000, 1)) * 0.01
    indata = playrec(
        outdata,
        samplerate=96000,
        input_mapping=["Dev2/ai0", "Dev2/ai1", "Dev2/ai2"],
        output_mapping=["Dev2/ao0"],
    )
