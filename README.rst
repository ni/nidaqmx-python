+------------+-----------------------------------------------------------+
| **Info**   | NI-DAQmx API for Python                                   | 
+------------+-----------------------------------------------------------+
| **Author** | National Instruments                                      |
+------------+-----------------------------------------------------------+

.. contents:: Table of Contents
   :depth: 1
   :backlinks: none

About
=====

The **nidaqmx** package allows you to develop instrumentation, acquisition, and 
control applications with NI data acquisition (DAQ) devices in Python. NI
created and supports this package.

Documentation
-------------

You can find the latest API documentation for the **nidaqmx** package on
`Read the Docs <http://nidaqmx-python.readthedocs.io/en/stable>`_.

Refer to the
`NI-DAQmx User Manual <https://www.ni.com/docs/en-US/bundle/ni-daqmx/>`_ for
an overview of NI-DAQmx, key concepts, and measurement fundamentals. The
NI-DAQmx Help also installs locally with the full version of NI-DAQmx. Refer to
`this Knowledge Base (KB) <http://digital.ni.com/express.nsf/bycode/exagg4>`_
for more information.

Implementation
--------------

The package is implemented in Python as an object-oriented wrapper around the
NI-DAQmx C API using the
`ctypes <https://docs.python.org/3/library/ctypes.html>`_ Python library.

Supported NI-DAQmx Driver Versions
----------------------------------

**nidaqmx** supports all versions of NI-DAQmx. Some functions in the **nidaqmx**
package may be unavailable with earlier versions of the NI-DAQmx driver. Refer
to the Installation section for details on how to install the latest version of
the NI-DAQmx driver.

Operating System Support
------------------------

**nidaqmx** supports Windows and Linux operating systems where the NI-DAQmx
driver is supported. Refer to
`NI Hardware and Operating System Compatibility <https://www.ni.com/r/hw-support>`_
for which versions of the driver support your hardware on a given operating
system.

Python Version Support
----------------------

**nidaqmx** supports CPython 3.9+ and PyPy3.

Installation
============

You can use `pip <http://pypi.python.org/pypi/pip>`_ to download **nidaqmx** from
`PyPI <https://pypi.org/project/nidaqmx/>`_ and install it::

  $ python -m pip install nidaqmx

Automatic Driver Installation
-----------------------------

Running **nidaqmx** requires NI-DAQmx to be installed. The **nidaqmx** module
ships with a command-line interface (CLI) to streamline the installation
experience. You can install the NI-DAQmx driver using the following command::

  $ python -m nidaqmx installdriver

On Windows, this command will download and launch an online streaming installer
from ni.com. On Linux, this will download the repository registration package
for your Linux distribution and install the driver using your package manager.

Manual Driver Installation
--------------------------

Visit `ni.com/downloads <http://www.ni.com/downloads/>`_ to download the latest
version of NI-DAQmx. None of the recommended **Additional items** are required
for **nidaqmx** to function, and they can be removed to minimize installation
size. It is recommended you continue to install the **NI Certificates** package
to allow your Operating System to trust NI built binaries, improving your
software and hardware installation experience.

Getting Started
===============
In order to use the **nidaqmx** package, you must have at least one DAQ
(`Data Acquisition <https://www.ni.com/en/shop/data-acquisition.html>`_) device
installed on your system. Both physical and simulated devices are supported. The
examples below use an X Series DAQ device (e.g.: PXIe-6363, PCIe-6363, or
USB-6363). You can use **NI MAX** or **NI Hardware Configuration Utility** to
verify and configure your devices.

Finding and configuring device name in **NI MAX**:

.. image:: https://raw.githubusercontent.com/ni/nidaqmx-python/ca9b8554e351a45172a3490a4716a52d8af6e95e/max_device_name.png
  :alt: NI MAX Device Name
  :align: center
  :width: 800px

Finding and configuring device name in **NI Hardware Configuration Utility**:

.. image:: https://raw.githubusercontent.com/ni/nidaqmx-python/ca9b8554e351a45172a3490a4716a52d8af6e95e/hwcu_device_name.png
  :alt: NI HWCU Device Name
  :align: center
  :width: 800px

Python Examples
===============

You can find a variety of examples in the GitHub repository in the
`nidaqmx-python examples <https://github.com/ni/nidaqmx-python/tree/master/examples>`_
directory. For best results, use the examples corresponding to the version of
**nidaqmx** that you are using. For example, if you are using version 1.0.0,
check out the
`examples directory in the 1.0.0 tag <https://github.com/ni/nidaqmx-python/tree/1.0.0/examples>`_.
Newer examples may demonstrate features that are not available in older versions
of **nidaqmx**.

Key Concepts in NI-DAQmx
=========================

Tasks
-----
A task is a collection of one or more virtual channels with timing, triggering, and other properties.
Refer to `NI-DAQmx Task <https://www.ni.com/docs/en-US/bundle/ni-daqmx/page/tasksnidaqmx.html>`_ for more information.

Example code to create a task:

.. code-block:: python

  >>> import nidaqmx
  >>> with nidaqmx.Task() as task:
  ...     pass

Virtual Channels
----------------
Virtual channels, or sometimes referred to generically as channels, are software entities that encapsulate the physical channel
along with other channel specific information (e.g.: range, terminal configuration, and custom scaling) that formats the data.
A physical channel is a terminal or pin at which you can measure or generate an analog or digital signal. A single physical channel
can include more than one terminal, as in the case of a differential analog input channel or a digital port of eight lines.
Every physical channel on a device has a unique name (for instance, cDAQ1Mod4/ai0, Dev2/ao5, and Dev6/ctr3) that follows the
NI-DAQmx physical channel naming convention.
Refer to `NI-DAQmx Channel <https://www.ni.com/docs/en-US/bundle/ni-daqmx/page/chans.html>`_ for more information.

Example code that adds an analog input channel to a task, configures the range, and reads data:

.. code-block:: python

  >>> import nidaqmx
  >>> with nidaqmx.Task() as task:
  ...     task.ai_channels.add_ai_voltage_chan("Dev1/ai0", min_val=-10.0, max_val=10.0)
  ...     task.read()
  ...
  AIChannel(name=Dev1/ai0)
  -0.14954069643238624

Example code that adds multiple analog input channels to a task, configures their range, and reads data:

.. code-block:: python

  >>> import nidaqmx
  >>> with nidaqmx.Task() as task:
  ...     task.ai_channels.add_ai_voltage_chan("Dev1/ai0", min_val=-5.0, max_val=5.0)
  ...     task.ai_channels.add_ai_voltage_chan("Dev1/ai1", min_val=-10.0, max_val=10.0)
  ...     task.read()
  ...
  AIChannel(name=Dev1/ai0)
  AIChannel(name=Dev1/ai1)
  [-0.07477034821619312, 0.8642841883602405]

Timing
------
You can use software timing or hardware timing to control when a signal is acquired or generated.
With hardware timing, a digital signal, such as a clock on your device, controls the rate of acquisition or generation.
With software timing, the rate at which the samples are acquired or generated is determined by the software and operating system
instead of by the measurement device. A hardware clock can run much faster than a software loop.
A hardware clock is also more accurate than a software loop.
Refer to `Timing, Hardware Versus Software <https://www.ni.com/docs/en-US/bundle/ni-daqmx/page/hardwresoftwretiming.html>`_ for more information.

Example code to acquire finite amount of data using hardware timing:

.. code-block:: python

  >>> import nidaqmx
  >>> from nidaqmx.constants import AcquisitionType, READ_ALL_AVAILABLE
  >>> with nidaqmx.Task() as task:
  ...     task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
  ...     task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=10)
  ...     data = task.read(READ_ALL_AVAILABLE)
  ...     print("Acquired data: [" + ", ".join(f"{value:f}" for value in data) + "]")
  ...
  AIChannel(name=Dev1/ai0)
  Acquired data: [-0.149693, 2.869503, 4.520249, 4.704886, 2.875912, -0.006104, -2.895596, -4.493698, -4.515671, -2.776574]

TDMS Logging
------------
Technical Data Management Streaming (TDMS) is a binary file format that allows for high-speed data logging.
When you enable TDMS data logging, NI-DAQmx can stream data directly from the device buffer to the hard disk.
Refer to `TDMS Logging <https://www.ni.com/docs/en-US/bundle/ni-daqmx/page/datalogging.html>`_ for more information.

Example code to acquire finite amount of data and log it to a TDMS file:

.. code-block:: python

  >>> import nidaqmx
  >>> from nidaqmx.constants import AcquisitionType, LoggingMode, LoggingOperation, READ_ALL_AVAILABLE
  >>> with nidaqmx.Task() as task:
  ...     task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
  ...     task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=10)
  ...     task.in_stream.configure_logging("TestData.tdms", LoggingMode.LOG_AND_READ, operation=LoggingOperation.CREATE_OR_REPLACE)
  ...     data = task.read(READ_ALL_AVAILABLE)
  ...     print("Acquired data: [" + ", ".join(f"{value:f}" for value in data) + "]")
  ...
  AIChannel(name=Dev1/ai0)
  Acquired data: [-0.149693, 2.869503, 4.520249, 4.704886, 2.875912, -0.006104, -2.895596, -4.493698, -4.515671, -2.776574]

To read the TDMS file, you can use the **npTDMS** third-party module.
Refer to `npTDMS <https://pypi.org/project/npTDMS/>`_ for detailed usage.

Example code to read the TDMS file created from example above and display the data:

.. code-block:: python

  >>> from nptdms import TdmsFile
  >>> with TdmsFile.read("TestData.tdms") as tdms_file:
  ...   for group in tdms_file.groups():
  ...     for channel in group.channels():
  ...       data = channel[:]
  ...       print("data: [" + ", ".join(f"{value:f}" for value in data) + "]")
  ...
  data: [-0.149693, 2.869503, 4.520249, 4.704886, 2.875912, -0.006104, -2.895596, -4.493698, -4.515671, -2.776574]

Plot Data
---------
To visualize the acquired data as a waveform, you can use the **matplotlib.pyplot** third-party module.
Refer to `Pyplot tutorial <https://matplotlib.org/stable/tutorials/pyplot.html#sphx-glr-tutorials-pyplot-py>`_ for detailed usage.

Example code to plot waveform for acquired data using **matplotlib.pyplot** module:

.. code-block:: python

  >>> import nidaqmx
  >>> from nidaqmx.constants import AcquisitionType, READ_ALL_AVAILABLE
  >>> import matplotlib.pyplot as plt
  >>> with nidaqmx.Task() as task:
  ...   task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
  ...   task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.FINITE, samps_per_chan=50)
  ...   data = task.read(READ_ALL_AVAILABLE)
  ...   plt.plot(data)
  ...   plt.ylabel('Amplitude')
  ...   plt.title('Waveform')
  ...   plt.show()
  ...
  AIChannel(name=Dev1/ai0)
  [<matplotlib.lines.Line2D object at 0x00000141D7043970>]
  Text(0, 0.5, 'Amplitude')
  Text(0.5, 1.0, 'waveform')

.. image:: https://raw.githubusercontent.com/ni/nidaqmx-python/ca9b8554e351a45172a3490a4716a52d8af6e95e/waveform.png
  :alt: Waveform
  :align: center
  :width: 400px

For more information on how to use **nidaqmx** package, refer to **Usage** section below.

.. _usage-section:

Usage
=====
The following is a basic example of using an **nidaqmx.task.Task** object.
This example illustrates how the single, dynamic **nidaqmx.task.Task.read**
method returns the appropriate data type.

.. code-block:: python

  >>> import nidaqmx
  >>> with nidaqmx.Task() as task:
  ...     task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
  ...     task.read()
  ...
  -0.07476920729381246
  >>> with nidaqmx.Task() as task:
  ...     task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
  ...     task.read(number_of_samples_per_channel=2)
  ...
  [0.26001373311970705, 0.37796597238117036]
  >>> from nidaqmx.constants import LineGrouping
  >>> with nidaqmx.Task() as task:
  ...     task.di_channels.add_di_chan(
  ...         "cDAQ2Mod4/port0/line0:1", line_grouping=LineGrouping.CHAN_PER_LINE)
  ...     task.read(number_of_samples_per_channel=2)
  ...
  [[False, True], [True, True]]

A single, dynamic **nidaqmx.task.Task.write** method also exists.

.. code-block:: python

  >>> import nidaqmx
  >>> from nidaqmx.types import CtrTime
  >>> with nidaqmx.Task() as task:
  ...     task.co_channels.add_co_pulse_chan_time("Dev1/ctr0")
  ...     sample = CtrTime(high_time=0.001, low_time=0.001)
  ...     task.write(sample)
  ...
  1
  >>> with nidaqmx.Task() as task:
  ...     task.ao_channels.add_ao_voltage_chan("Dev1/ao0")
  ...     task.write([1.1, 2.2, 3.3, 4.4, 5.5], auto_start=True)
  ...
  5

Consider using the **nidaqmx.stream_readers** and **nidaqmx.stream_writers**
classes to increase the performance of your application, which accept pre-allocated
NumPy arrays.

Following is an example of using an **nidaqmx.system.System** object.

.. code-block:: python

  >>> import nidaqmx.system
  >>> system = nidaqmx.system.System.local()
  >>> system.driver_version
  DriverVersion(major_version=16L, minor_version=0L, update_version=0L)
  >>> for device in system.devices:
  ...     print(device)
  ...
  Device(name=Dev1)
  Device(name=Dev2)
  Device(name=cDAQ1)
  >>> import collections
  >>> isinstance(system.devices, collections.Sequence)
  True
  >>> device = system.devices['Dev1']
  >>> device == nidaqmx.system.Device('Dev1')
  True
  >>> isinstance(device.ai_physical_chans, collections.Sequence)
  True
  >>> phys_chan = device.ai_physical_chans['ai0']
  >>> phys_chan
  PhysicalChannel(name=Dev1/ai0)
  >>> phys_chan == nidaqmx.system.PhysicalChannel('Dev1/ai0')
  True
  >>> phys_chan.ai_term_cfgs
  [<TerminalConfiguration.RSE: 10083>, <TerminalConfiguration.NRSE: 10078>, <TerminalConfiguration.DIFFERENTIAL: 10106>]
  >>> from enum import Enum
  >>> isinstance(phys_chan.ai_term_cfgs[0], Enum)
  True

Bugs / Feature Requests
=======================

To report a bug or submit a feature request, please use the
`GitHub issues page <https://github.com/ni/nidaqmx-python/issues>`_.

Information to Include When Asking for Help
-------------------------------------------

Please include **all** of the following information when opening an issue:

- Detailed steps on how to reproduce the problem and full traceback, if
  applicable.
- The python version used::

  $ python -c "import sys; print(sys.version)"

- The versions of the **nidaqmx** and numpy packages used::

  $ python -m pip list

- The version of the NI-DAQmx driver used. Follow
  `this KB article <http://digital.ni.com/express.nsf/bycode/ex8amn>`_
  to determine the version of NI-DAQmx you have installed.
- The operating system and version, for example Windows 7, CentOS 7.2, ...

License
=======

**nidaqmx** is licensed under an MIT-style license (see
`LICENSE <https://github.com/ni/nidaqmx-python/blob/master/LICENSE>`_).
Other incorporated projects may be licensed under different licenses. All
licenses allow for non-commercial and commercial use.
