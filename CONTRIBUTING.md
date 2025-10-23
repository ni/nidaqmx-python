# Contributing to nidaqmx

Contributions to **nidaqmx** are welcome from all!

**nidaqmx** is managed via [git](https://git-scm.com), with the canonical upstream repository hosted
on [GitHub](http://developercertificate.org/).

**nidaqmx** follows a pull-request model for development.  If you wish to contribute, you will need
to create a GitHub account, fork this project, push a branch with your changes to your project, and
then submit a pull request.

See [GitHub's official documentation](https://help.github.com/articles/using-pull-requests/) for
more details.

# Getting Started

To contribute to this project, it is recommended that you follow these steps:

1. Ensure you have [poetry](https://python-poetry.org/) [installed](https://python-poetry.org/docs/#installation)
2. Clone the repository using `git clone https://github.com/ni/nidaqmx-python.git`
3. Get the submodules using `git submodule update --init --recursive`
3. Install **nidaqmx** dependencies using `poetry install --all-extras`
4. Run the regression tests on your system (see Testing section). At this point, if any tests fail, do not
begin development. Try to investigate these failures. If you're unable to do so, report an issue
through our [GitHub issues page](http://github.com/ni/nidaqmx-python/issues).
5. Write new tests that demonstrate your bug or feature. Ensure that these new tests fail.
6. Make your change.
7. Once the necessary changes are done, update the auto-generated code using `poetry run python src/codegen --dest generated/nidaqmx`. This will ensure that the latest files are present in the ``generated`` folder.
   > **Note**
   > The codegen scripts require Python 3.9 or later.
8. Run all the regression tests again (including the tests you just added), and confirm that they all
pass.
9. Run `poetry run ni-python-styleguide lint` to check that the updated code follows NI's Python coding
conventions. If this reports errors, first run `poetry run ni-python-styleguide fix` in order to sort
imports and format the code with Black, then manually fix any remaining errors.
10. Run `poetry run mypy` to statically type-check the updated code.
11. Send a GitHub Pull Request to the main repository's master branch. GitHub Pull Requests are the
expected method of code collaboration on this project.

# Testing

In order to be able to run the **nidaqmx** regression tests, your setup should meet the following minimum
requirements:

- Setup has a machine with NI-DAQmx or the NI-DAQmx Runtime installed.
   - Currently the minimum supported NI-DAQmx version to run all tests is 21.3.
- Machine has a supported version of CPython or PyPy installed.
- Machine has [poetry](https://python-poetry.org/) installed.
- (recommended) Machine has an X Series DAQ device (e.g. PCIe-6363 or USB-6351) connected to it.
  - You can still run the tests without a physical X Series DAQ device, but some tests will be skipped.

Before running the regression tests, import the appropriate NI MAX configuration files:
- ``tests\max_config\nidaqmxMaxConfig.ini``: Contains custom scales, global channels, simulated devices, 
  and tasks used by many regression tests.
   - **Note:** On Linux, use ``tests\max_config\linux\nidaqmxMaxConfig.ini`` to avoid importing an unsupported device.
- ``tests\max_config\examplesMaxConfig.ini``: Contains simulated devices used by the example programs.
  Importing this file is optional. It is used to run a subset of the example programs as test cases.

Refer to this [KB article](http://digital.ni.com/public.nsf/allkb/0E0D3D7C4AA8903886256B29000C9D5A) for
details on how to import a MAX configuration.

To run the **nidaqmx** regression tests in a specific version of Python, run the following command in the
root of the distribution:

```sh
$ poetry run pytest
```

To run the regression tests in all Python interpreters supported by **nidaqmx**, run the following
commands in the root of the distribution:

```sh
$ poetry run tox
```
  
This requires you to have all the Python interpreters supported by **nidaqmx** installed on your
machine.

# Benchmarks

Benchmark tests are not run by default when you run pytest. To run the benchmarks, use this command:

```sh
# Run the benchmarks
#   Compare benchmark before/after a change
#     see https://pytest-benchmark.readthedocs.io/en/latest/comparing.html
#   Run 1:  --benchmark-save=some-name
#   Run N:  --benchmark-compare=0001
$ poetry run pytest -v tests/benchmark --device Dev1
```

Or you can use tox (which skips the gRPC variants):
```
poetry run -- tox -e py39-base-benchmark -- --device Dev1
```

The benchmarks are designed to run on a 6363 device. If you don't specify a specific
device using `--device`, then it will automatically use any real or simulated 6363
that can be found.

# Building Documentation

To build the documentation install the optional docs packages and run sphinx. For example:

```sh
$ poetry install --with docs
$ poetry run sphinx-build -b html docs docs\_build
```

# Branching Policy

Active development for the next release occurs on the `master` branch. 

During finalization, we create a release branch (e.g. `releases/1.2`) in order to control which changes target the imminent
release vs. the next release after that. Changes that are intended for both the imminent release and subsequent releases
should be made in the `master` branch and cherry-picked into the release branch. Changes that only apply to the imminent
release (such as version numbers) may be made directly in the release branch.

# Release Process

1. Ensure your git `HEAD` is at the latest version of the `master` or appropriate `releases/*` branch with no pending changes.
2. Note the version currently being released by running:
   ```sh
   $ poetry version
   ```
3. Run tests on every supported Python version. Refer to [Testing](#testing) section for details.
4. Build the documentation and spot check the output. Refer to [Building Documentation](#building-documentation)
section for details. Note that [nidaqmx-python @ readthedocs.io](https://nidaqmx-python.readthedocs.io/en/latest/)
has been configured to automatically update when the tagged GitHub release has been created. That
can be verified once that has been completed.
5. Create a release on GitHub, attaching the source at the latest commit as follows:
   * **Tag:** Create a new tag matching the version being released.
   * **Release Title:** The version being released.
   * **Description:** Contents of the `CHANGELOG.md` for the version being released.

   Publishing a release automatically triggers the [publish.yml](./.github/workflows/publish.yml)
   workflow, which checks and builds the package, requests approval to publish it using the `pypi`
   deployment environment, publishes the package to PyPI using [Trusted
   Publishing](https://docs.pypi.org/trusted-publishers/), and creates a PR to update the version of
   **nidaqmx** in `pyproject.toml`.
6. GitHub contacts the approvers for the `pypi` deployment environment, who are currently the repo
   admins. One of them must approve the deployment for the publishing to proceed.
7. Find the auto-created PR named `chore: Update project version - <branch>`.
   - If it is waiting for checks to complete, close it and re-open it to work around the issue
     described in [the `ni/python-actions/update-project-version`
     docs](https://github.com/ni/python-actions?tab=readme-ov-file#token).
   - If the new version number is incorrect, update it by posting and committing a suggestion.
8. Create a PR adding a section to `CHANGELOG.md` for the new version with empty subsections.

# Updating gRPC stubs when the .proto file is modified

The `generated\nidaqmx\_stubs` directory contains the auto-generated Python files based on the NI-DAQmx protobuf (`.proto`) file.

The latest NI-DAQmx .proto file is available in the [grpc-device GitHub repo](https://github.com/ni/grpc-device/blob/main/generated/nidaqmx/nidaqmx.proto). Manually download and overwrite the `.proto` file under the location `codegen\protos\nidaqmx.proto`.

Run `poetry run python src/codegen --dest generated/nidaqmx`. This will ensure that the latest stub files are present in the `generated\nidaqmx\_stubs` folder.


# Developer Certificate of Origin (DCO)

Developer's Certificate of Origin 1.1

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
    have the right to submit it under the open source license
    indicated in the file; or

(b) The contribution is based upon previous work that, to the best
    of my knowledge, is covered under an appropriate open source
    license and I have the right under that license to submit that
    work with modifications, whether created in whole or in part
    by me, under the same open source license (unless I am
    permitted to submit under a different license), as indicated
    in the file; or

(c) The contribution was provided directly to me by some other
    person who certified (a), (b) or (c) and I have not modified
    it.

(d) I understand and agree that this project and the contribution
    are public and that a record of the contribution (including all
    personal information I submit with it, including my sign-off) is
    maintained indefinitely and may be redistributed consistent with
    this project or the open source license(s) involved.

(taken from [developercertificate.org](http://developercertificate.org/))

See [LICENSE](https://github.com/ni/nidaqmx-python/blob/master/LICENSE)
for details about how **nidaqmx** is licensed.
