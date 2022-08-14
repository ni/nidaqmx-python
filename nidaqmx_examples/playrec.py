"""Simultaneous read and write with NI USB-4431 or similar device."""

import numpy as np
import nidaqmx as ni
from nidaqmx.constants import WAIT_INFINITELY


def query_devices():
  local = ni.system.System.local()
  driver = local.driver_version

  print(f'DAQmx {0}.{1}.{2}'.format(
    driver.major_version, driver.minor_version, driver.update_version))

  for device in local.devices:
    print('Device Name: {0}, Product Category: {1}, Product Type: {2}'.format(
      device.name, device.product_category, device.product_type))


def playrec(
  data, samplerate=96000, input_mapping=['Dev2/ai0', 'Dev2/ai1', 'Dev2/ai2'],
  output_mapping=['Dev2/ao0']
):
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
  max_out_range = 3.5 # output range of USB-4431
  max_in_range = 10   # input range of USB-4431
  max_outdata = np.max(np.abs(outdata))
  if max_outdata > max_out_range:
    raise ValueError(
      f"outdata amplitude ({max_outdata:.2f}) larger than allowed range"
      f"(+-{max_out_range:.2f}).")

  outdata = np.asarray(outdata).T
  nsamples = outdata.shape[1]

  with ni.Task() as read_task, ni.Task() as write_task:
    for o in output_mapping:
      aochan = write_task.ao_channels.add_ao_voltage_chan(o)
      aochan.ao_max = max_out_range
      aochan.ao_min = -max_out_range
    for i in input_mapping:
      aichan = read_task.ai_channels.add_ai_voltage_chan(i)
      aichan.ai_min = -max_in_range
      aichan.ai_max = max_in_range

    for task in (read_task, write_task):
      task.timing.cfg_samp_clk_timing(rate=samplerate, source='OnboardClock',
                                      samps_per_chan=nsamples)

    # trigger write_task as soon as read_task starts
    write_task.triggers.start_trigger.cfg_dig_edge_start_trig(
            read_task.triggers.start_trigger.term)
    write_task.write(outdata, auto_start=False)
    write_task.start()  # write_task doesn't start at read_task's start_trigger
                        # without this
    indata = read_task.read(nsamples, timeout=WAIT_INFINITELY) # do not time out
                                                               # for long inputs

  return np.asarray(indata).T


if __name__ == '__main__':
  # excite through one output and record at three inputs
  outdata = np.random.normal(size=(1000, 1))*0.01
  indata = playrec(outdata)
