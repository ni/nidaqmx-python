# Changelog

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
    * Refactored the repository folder structure as follows:
        * `generated/nidaqmx/` - The output of the code generator and source for the build `nidaqmx` module. Do not directly modify any files in this folder.
        * `nidaqmx_examples/` - Example programs demonstrating how to use the `nidaqmx` module.
        * `src/codegen/` - The code generator.
        * `src/handwritten/` - Hand-maintained files that are copied as-is during code generation.
        * `src/nidaqmx` - Original location of the `nidaqmx` source code. This is now deprecated and no longer exists.
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