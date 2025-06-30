# Changelog
* [1.2.0](#120)
* [1.1.0](#110)
* [1.0.2](#102)
* [1.0.1](#101)
* [1.0.0](#100)
* [0.9.0](#090)
* [0.8.0](#080)
* [0.7.0](#070)
* [0.6.5](#065)
* [0.6.4](#064)
* [0.6.3](#063)
* [0.6.2](#062)
* [0.6.1](#061)
* [0.6.0](#060)
* [0.5.8](#058)
* [0.5.7](#057)
* [0.5.6](#056)
* [0.5.5](#055)
* [0.5.4](#054)
* [0.5.2](#052)
* [0.5.0](#050)

All notable changes to this project will be documented in this file.

## 1.2.0
* ### Merged Pull Requests
    * [Full changelog: 1.1.0...1.2.0](https://github.com/ni/nidaqmx-python/compare/1.1.0...1.2.0)

* ### Resolved Issues
    * Fix PEP 660 builds by setting `build-system` to use `poetry-core`
    * [579: nidaqmx does not generate numbered virtual channel names correctly](https://github.com/ni/nidaqmx-python/issues/579)
    * [692: Cannot set "ai_conv_rate" on NI DAQ 9209 due to missing active device modifier for timing attributes](https://github.com/ni/nidaqmx-python/issues/692)

* ### Major Changes
    * Removed the `docs` extra and converted it to a Poetry dependency group.
    * Updated hightime dependency from `^0.2.2` to `>=0.2.2` to allow for newer versions.

* ### Known Issues
    * ...

## 1.1.0
* ### Merged Pull Requests
    * [Full changelog: 1.0.2...1.1.0](https://github.com/ni/nidaqmx-python/compare/1.0.2...1.1.0)

* ### Resolved Issues
    * [656: Missing usage of slots in classes with DAQmx attributes](https://github.com/ni/nidaqmx-python/issues/656)

* ### Major Changes
    * Added support for mioDAQ configurable digital voltage.
    * Added support for mioDAQ ID Pin.
    * Removed support for Python 3.8.

* ### Known Issues
    * ...

## 1.0.2
* ### Merged Pull Requests
    * [Full changelog: 1.0.1...1.0.2](https://github.com/ni/nidaqmx-python/compare/1.0.1...1.0.2)

* ### Resolved Issues
    * [644: nidaqmx doesn't support Python 3.13+](https://github.com/ni/nidaqmx-python/issues/644)
    * [641: No devices found](https://github.com/ni/nidaqmx-python/issues/641)
        * Fall back to ASCII encoding if the system locale is not set.

* ### Known Issues
    * [639: first_samp_timestamp_val property does not work because LibraryInterpreter is missing a method](https://github.com/ni/nidaqmx-python/issues/639)

## 1.0.1
* ### Merged Pull Requests
    * [Full changelog: 1.0.0...1.0.1](https://github.com/ni/nidaqmx-python/compare/1.0.0...1.0.1)

* ### Resolved Issues
    * [540: Task.wait_for_valid_timestamp doesn't return the timestamp](https://github.com/ni/nidaqmx-python/issues/540)
    * [606: CERTIFICATE_VERIFY_FAILED occurs when executing installdriver command on Windows system](https://github.com/ni/nidaqmx-python/issues/606)
    * [615: Onboard device memory overflow](https://github.com/ni/nidaqmx-python/issues/615)
    * [623: installdriver CLI doesn't prompt or indicate what versions are being downloaded/installed on a clean system](https://github.com/ni/nidaqmx-python/issues/623)

* ### Known Issues
    * [613: InStream.logging_file_path setter type hint is not effective](https://github.com/ni/nidaqmx-python/issues/613)
    * [620: InStream.get_channels_buffer_size uses wrong encoding](https://github.com/ni/nidaqmx-python/issues/620)
    * [621: InStream.get_channels_buffer_size should not be public](https://github.com/ni/nidaqmx-python/issues/621)

## 1.0.0
* ### Merged Pull Requests
    * [Full changelog: 0.9.0...1.0.0](https://github.com/ni/nidaqmx-python/compare/0.9.0...1.0.0)

* ### Resolved Issues
    * [38: No spacing in raw-read function names](https://github.com/ni/nidaqmx-python/issues/38)
    * [384: Support internationalization](https://github.com/ni/nidaqmx-python/issues/384)
    * [392: Indexing PhysicalChannelCollection fails for slices and strings containing a list/range of channels](https://github.com/ni/nidaqmx-python/issues/392)
    * [482: Default argument values for bridge create channel functions are unusable](https://github.com/ni/nidaqmx-python/issues/482)

* ### Major Changes
    * Add support for strain calibration (offset nulling and shunt calibration)
    * Add support for DAQmx calibration info properties
    * Add support for WaitForValidTimestamp
    * Fix naming issues:
        * Rename `ShuntCalSelect.AAND_B` to `A_AND_B`.
    * Automate Driver Install Experience within nidaqmx Module
    * Update libtime to accept time before 1970

* ### Known Issues
    * ...

## 0.9.0

* ### Merged Pull Requests
    *  [460: enabled support for DAQmxSelfCal](https://github.com/ni/nidaqmx-python/pull/460)
* ### Major Changes
    * `nidaqmx.errors.DaqNotFoundError`, `nidaqmx.errors.DaqNotSupportedError`, and
    `nidaqmx.errors.DaqFunctionNotSupportedError` are now public exceptions.
    * Consistently return `nidaqmx.errors.DaqNotFoundError` on all platforms when the NI-DAQmx
    driver is not installed.
    * Updated supported Python versions to 3.8, 3.9, 3.10, 3.11, and 3.12
* ### Known Issues
    * ...

## 0.8.0

* ### Merged Pull Requests
    * [Full changelog: 0.7.0...0.8.0](https://github.com/ni/nidaqmx-python/compare/0.7.0...0.8.0)
    * [Query: Closed PRs with the label: interpreter_implementation](https://github.com/ni/nidaqmx-python/pulls?q=label%3Ainterpreter_implementation+is%3Aclosed)
    * [Query: Closed PRs with the label: library_interpreter](https://github.com/ni/nidaqmx-python/pulls?q=label%3Alibrary_interpreter+is%3Aclosed)
    * [Query: Closed PRs with the label: grpc_interpreter](https://github.com/ni/nidaqmx-python/pulls?q=label%3Agrpc_interpreter+is%3Aclosed)
    * [Query: Closed PRs with the label: test_improvements](https://github.com/ni/nidaqmx-python/pulls?q=label%3Atest_improvements+is%3Aclosed)
    * [Query: Closed PRs with the label: interpreter_fixes](https://github.com/ni/nidaqmx-python/pulls?q=label%3Ainterpreter_fixes+is%3Aclosed)
    * [Query: Closed PRs with the label: interpreter_testcase_update](https://github.com/ni/nidaqmx-python/pulls?q=label%3Ainterpreter_testcase_updates+is%3Aclosed)
    * [Query: Closed PRs with the label: event_handling](https://github.com/ni/nidaqmx-python/pulls?q=label%3Aevent_handling+is%3Aclosed)

* ### Major Changes

    * Added support for communicating with DAQmx devices through gRPC using [NI gRPC Device Server](https://github.com/ni/grpc-device). This enables using DAQmx with the MeasurementLink session management service.
        * The initialization methods for `Task`, `Scale`, and other classes now accept a keyword-only `grpc_options` parameter. Pass a `GrpcSessionsOptions` object to enable gRPC support.
        * The `System` class now has a `remote()` method which accepts a `GrpcSessionOptions` object.
        * [NI gRPC Device Server](https://github.com/ni/grpc-device) version 2.2 or later is required. Older versions of NI gRPC Device Server are unsupported because they are missing bug fixes needed to support nidaqmx-python.
    * The following functions now emit `DeprecationWarning` when called:
        * `nidaqmx.errors` module: `check_for_error`, `is_string_buffer_too_small`, and `is_array_buffer_too_small` are `ctypes`-specific helper functions, so they have been moved to an internal module.
        * `System` class: `set_analog_power_up_states` does not support `PowerUpStates.TRISTATE` and `get_analog_power_up_states` has design issues that make the previous implementation unworkable, so they have been deprecated in favor of `set_analog_power_up_states_with_output_type` and `get_analog_power_up_states_with_output_type`.
    * The internals of the `nidaqmx` package have been refactored to support gRPC:
        * Access to the DAQmx driver is now handled by the internal `BaseInterpreter` abstract base class. There are separate implementations of this abstract base class for `ctypes` vs. gRPC.
        * Internal initialization methods now accept an `interpreter` parameter. Methods that take an `interpreter` are not part of the public API.
        * Added a stub generator which will generate the gRPC stub files based on the proto files present in `src/codegen/protos`. The files will be generated into `generator/nidaqmx/_stubs`.
        * The internal `nidaqmx._task_modules.read_functions` and `nidaqmx._task_modules.write_functions` modules have been removed. If your application uses these modules, you must update it to use public APIs such as `task.read()`/`task.write()`, `task.in_stream.read()`/`task.out_stream.write()`, or `nidaqmx.stream_readers`/`nidaqmx.stream_writers`.
        * Updated the existing tests to run with and without gRPC support.
        * Added multiple test cases to improve the overall test coverage.

* ### Known Issues
   * Comparisons between DAQmx object instances do not take gRPC remoting into account. For example, `Device("Dev1")` refers to a local device and `Device("Dev1", grpc_options=...)` refers to a remote device, but they are considered equal. Likewise, two instances of `Device("Dev1", grpc_options=...)` with different remote hosts are considered equal.

## 0.7.0

* ### Merged Pull Requests
    * [217: Handle leading zeros in flatten/unflatten implementation](https://github.com/ni/nidaqmx-python/issues/217)
    * [219: nidaqmx: Use in-project virtualenvs](https://github.com/ni/nidaqmx-python/pull/219)
    * [Query: Closed PRs with label:generator_refactor](https://github.com/ni/nidaqmx-python/pulls?page=1&q=is%3Apr+is%3Aclosed+label%3Agenerator_refactor)
    * [Query: Closed PRs with label:test_improvements](https://github.com/ni/nidaqmx-python/pulls?page=1&q=is%3Apr+is%3Aclosed+label%3Atest_improvements)
    * [256: nidaqmx: Remove Python 2.7 workarounds](https://github.com/ni/nidaqmx-python/pull/256)
* ### Resolved Issues
    * [216: Can read channel_names of PersistedTask but not channels](https://github.com/ni/nidaqmx-python/issues/216)
* ### Major Changes
    * Added a generator that produces the `nidaqmx` module code.
    * Some properties were renamed in an effort to improve the consistency of the `nidaqmx` module and to support maintainability of the generator. The previous names are still usable, but will emit a `DeprecationWarning` on usage. These deprecated properties may be removed in a future update.
    * Unused enums have been removed. This affects enums that are solely used by DAQmx features that are not supported in the `nidaqmx` module, such as external calibration, the DAQmx switch API, and internal APIs.
    * Refactored the repository folder structure as follows:
        * `generated/nidaqmx/` - The output of the code generator and source for the build `nidaqmx` module. Do not directly modify any files in this folder.
        * `examples/` - Example programs demonstrating how to use the `nidaqmx` module.
        * `src/codegen/` - The code generator.
        * `src/handwritten/` - Hand-maintained files that are copied as-is during code generation.
        * `tests` - Test code that exercises the `nidaqmx` module to ensure it functions correctly and doesn't introduce regressions.
    * Multiple various test improvements in support of the generator refactoring.

## 0.6.5

* ### Resolved Issues
    * [194: Multiple Voltage Measurement Types in the same task causes errors on Read](https://github.com/ni/nidaqmx-python/pull/194)

## 0.6.4

* ### Merged Pull Requests
    * [179: Optimize for happy path](https://github.com/ni/nidaqmx-python/pull/179)
    * [180: Use ndarray.size instead of numpy.prod](https://github.com/ni/nidaqmx-python/pull/180)
    * [182: fix enum bitfields](https://github.com/ni/nidaqmx-python/pull/182)
    * [183: add support for reverse voltage error attributes to nidaqmx-python](https://github.com/ni/nidaqmx-python/pull/183)
    * [185: update testing to allow for some simulation](https://github.com/ni/nidaqmx-python/pull/185)
* ### Resolved Issues
    * [181: mismatched enum names in ai_term_cfgs](https://github.com/ni/nidaqmx-python/issues/181)

## 0.6.3

* ### Major Changes
    * DAQmx 22.0 updates.

## 0.6.2

* ### Major Changes
    * Added NI-DAQmx Power Channel APIs.

## 0.6.1

* ### Resolved Issues
    * [37: ai_raw example is bad](https://github.com/ni/nidaqmx-python/issues/37)
    * [54: Linux supported?](https://github.com/ni/nidaqmx-python/issues/54)
    * [64: nidaqmx-python and pynidaqmx projects use the same package name](https://github.com/ni/nidaqmx-python/issues/64)
    * [65: ci_count_edges.py REQUIRES A START COMMAND](https://github.com/ni/nidaqmx-python/issues/65)
    * [100: How to clear task and create a new task with same name?](https://github.com/ni/nidaqmx-python/issues/100)
    * [101: Use IntEnum instead of Enum](https://github.com/ni/nidaqmx-python/issues/101)
    * [102: handle types and daqmx versions](https://github.com/ni/nidaqmx-python/issues/102)
    * [117: Error in example](https://github.com/ni/nidaqmx-python/issues/117)
    * [131: task.write for COUNTER_OUTPUT - UsageTypeCO.PULSE_FREQUENCY has frequency and duty cycle reversed](https://github.com/ni/nidaqmx-python/issues/131)
    * [124: nidaqmx_examples/system_properties.py errors out as of version 0.5.7](https://github.com/ni/nidaqmx-python/issues/124)
    * [151: Write functions require writable numpy array](https://github.com/ni/nidaqmx-python/issues/151)
    * [154: Problem with task.write() when not enough buffer free](https://github.com/ni/nidaqmx-python/issues/154)
* ### Major Changes
    * Scrubbed all examples to ensure they all function correctly and use DAQmx best practices.
    * Added `DaqReadError` and `DaqWriteError` subclasses of `DaqError` that provide important metadata for partial reads and writes.
    * Linux is officially supported.

## 0.6.0

* ### Resolved Issues
    * [132: __future__ imports are now all mandatory in the minimum supported python version](https://github.com/ni/nidaqmx-python/issues/132)
* ### Major Changes
    * Add support for most NI-DAQmx 16.1-21.5 APIs.
        * APIs using time data types are not yet supported.
    * Various other improvements:
        * No more empty docstrings on constants.
        * Fix C API function mapping for attributes - dozens were incorrect.
        * Remove some internal-only enumerations that were unused.
        * **(compat breaker)** Fix two egregious naming issues when translating the API to `SNAKE_CASE`. `M_HZ` is now
        `MHZ` (megahertz) and `<word>m_VOLTS` is now `MILLIVOLTS`.
        * **(compat breaker)** Fix various constant names that didn't make any sense.
        * Add a header to all auto-generated files indicating that they should not be edited by hand.


## 0.5.8

* ### Merged Pull Requests
    * [Bug in InStream.readinto()](https://github.com/ni/nidaqmx-python/pull/45)
    * [Fix for Linux where DAQmxGetSysNIDAQUpdateVersion is not available](https://github.com/ni/nidaqmx-python/pull/75)
    * [Fix RelativeTo function names to match DLL names](https://github.com/ni/nidaqmx-python/pull/86)
    * [fix: exported symbol names](https://github.com/ni/nidaqmx-python/pull/93)
    * [fix: dev dependencies to avoid security alerts](https://github.com/ni/nidaqmx-python/pull/94)
    * [fix: task.__del__ to use _saved_name](https://github.com/ni/nidaqmx-python/pull/95)
    * [remove: python2.7 support](https://github.com/ni/nidaqmx-python/pull/96)
    * [update: requirements](https://github.com/ni/nidaqmx-python/pull/97)
    * [Fix warning regarding ABC import from collections](https://github.com/ni/nidaqmx-python/pull/104)
    * [remove: py2, py27 support from classifiers](https://github.com/ni/nidaqmx-python/pull/105)
    * [Correct Network Connection Loss Property](https://github.com/ni/nidaqmx-python/pull/111)
* ### Resolved Issues
    * Fixed `test_many_sample_pulse_ticks` test
    * Added a bridge device to test MAX config to enable `test_list_of_floats_property` to run
    * [36: no version information available](https://github.com/ni/nidaqmx-python/issues/36)
* ### Major Changes
    * Switched to [poetry](https://python-poetry.org/) build system.
    * Updated supported Python versions to 3.7, 3.8, 3.9, and 3.10
    * Updated to latest dependencies
        * Replaced `numpy.bool` with `bool` native type

## 0.5.7
* ### Resolved Issues
    * [40: is_task_done() cannot be used.](https://github.com/ni/nidaqmx-python/issues/40)
    * [42: register signal event not supported?](https://github.com/ni/nidaqmx-python/issues/42)

## 0.5.6
* ### Resolved Issues
    * [32: Incorrect types in samp_quant_samp_per_chan and total_samp_per_chan_generated parameters](https://github.com/ni/nidaqmx-python/issues/32)
    * [1: nidaqmx doesn't work on Python 2.7.13](https://github.com/ni/nidaqmx-python/issues/1)

## 0.5.5
* ### Resolved Issues
    * Adding lock around `argtypes` to prevent race condition between setting `argtypes` and calling functions, in cases
    the functions run in parallel.
    * Some special cases needed unconditional locks around both the setting of `argtypes` and the actual function call,
    like the variadic power-up state functions in system.py, and the register events functions in task.py.

## 0.5.4
* ### Merged Pull Requests
    * [Fix for unregistering callbacks](https://github.com/ni/nidaqmx-python/pull/15)
* ### Resolved Issues
    * [13: Should _import_lib error for unsupported platforms?](https://github.com/ni/nidaqmx-python/issues/13)
    * [12: Cannot catch load/version issues with public API](https://github.com/ni/nidaqmx-python/issues/12)
    * [11: CONTRIBUTING.rst link to Issues is broken](https://github.com/ni/nidaqmx-python/issues/11)

## 0.5.2
* Initial public release of nidaqmx
* Update setup.py description and fix issues 2, 3, 5, and 6 raised by Ed Page.
    * Splitting joined acronyms AIADC, AIDC, AILVDT, AIRVDT and CITC.
    * Adding link to LICENSE file.
    * Updating README.rst file in source directory to eliminate Sphinx domaindirectives and add link to documentation on
    readthedocs.

## 0.5.0
* Initial pre-release of nidaqmx
