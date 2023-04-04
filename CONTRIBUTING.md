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
2. Fork the repository on GitHub.
3. Install **nidaqmx** dependencies using ``poetry install``
4. Run the unit tests on your system (see Testing section). At this point, if any tests fail, do not
begin development. Try to investigate these failures. If you're unable to do so, report an issue
through our [GitHub issues page](http://github.com/ni/nidaqmx-python/issues).
5. Write new tests that demonstrate your bug or feature. Ensure that these new tests fail.
6. Make your change.
7. Once the necessary changes are done, update the auto-generated code using ``poetry run python src/codegen --dest generated/nidaqmx``. This will ensure that the latest files are present in the ``generated`` folder.
   > **Note**
   > The codegen scripts require Python 3.8 or later.
8. Run all the unit tests again (which include the tests you just added), and confirm that they all
pass.
9. Send a GitHub Pull Request to the main repository's master branch. GitHub Pull Requests are the
expected method of code collaboration on this project.

# Testing

In order to be able to run the **nidaqmx** unit tests, your setup should meet the following minimum
requirements:

- Setup has a machine with NI-DAQmx or the NI-DAQmx Runtime installed.
   - Currently the minimum supported NI-DAQmx version to run all tests is 21.3.
- Machine has a supported version of CPython or PyPy installed.
- Machine has [poetry](https://python-poetry.org/) installed.
- Machine has an X-Series DAQ device connected to it (we ran the tests 
  using a PCIe-6363 or a USB-6351).

Before running any unit tests, an NI MAX configuration needs be imported. The MAX configuration
simply contains some custom scales used during testing. The MAX configuration file is located at
``tests\max_config\nidaqmxMaxConfig.ini``. Refer to this [KB article](http://digital.ni.com/public.nsf/allkb/0E0D3D7C4AA8903886256B29000C9D5A)
for details on how to import a MAX Configuration.

To run the **nidaqmx** unit tests in a specific version of Python, run the following command in the
root of the distribution:

```sh
$ poetry run pytest
```

To run the unit tests in all Python interpreters supported by **nidaqmx**, run the following
commands in the root of the distribution:

```sh
$ poetry run tox
```
  
This requires you to have all the Python interpreters supported by **nidaqmx** installed on your
machine.

# Building Documentation

To build the documentation install the optional docs packages and run sphinx. For example:

```sh
$ poetry install -E docs
$ poetry run sphinx-build -b html docs docs\_build
```

# Release Process

1. Ensure your git `HEAD` is at the latest version of `master` branch with no pending changes.
2. Note the version currently being released by running:
   ```sh
   $ poetry version
   ```
3. Run tests on every supported Python version. Refer to [Testing](#testing) section for details.
4. Build the documentation and spot check the output. Refer to [Building Documentation](#building-documentation)
section for details. Note that [nidaqmx-python @ readthedocs.io](https://nidaqmx-python.readthedocs.io/en/latest/)
has been configured to automatically update when the tagged GitHub release has been created. That
can be verified once that has been completed.
5. Publish **nidaqmx** to pypi by running:
   ```sh
   $ poetry publish
   ```
6. Create a release on GitHub, attaching the source at the latest commit as follows:
   * **Tag:** Create a new tag matching the version being released.
   * **Release Title:** The version being released.
   * **Description:** Contents of the `CHANGELOG.md` for the version being released.
7. Create a PR to update the version of **nidaqmx**
   * Update `pyproject.toml` version by running:
      ```sh
      $ poetry version [patch|minor|major]
      ```
   * If updating a minor or major version, update `version` and `release` in `docs/conf.py`.
   * Add a section to `CHANGELOG.md` for the new version with empty subsections.

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
