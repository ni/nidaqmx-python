from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        pytest.main(self.test_args)


pypi_name = 'nidaqmx'


def get_version(name):
    import os
    version = None
    script_dir = os.path.dirname(os.path.realpath(__file__))
    script_dir = os.path.join(script_dir, name)
    if not os.path.exists(os.path.join(script_dir, 'VERSION')):
        version = '1.0.0dev0'
    else:
        with open(os.path.join(script_dir, 'VERSION'), 'r') as version_file:
            version = version_file.read().rstrip()
    return version


def read_contents(file_to_read):
    with open(file_to_read, 'r') as f:
        return f.read()


setup(
    name=pypi_name,
    version=get_version(pypi_name),
    description='NI-DAQmx Python API',
    long_description=read_contents('README.rst'),
    author='National Instruments',
    maintainer="Brian Lee, Neil Stoddard",
    maintainer_email="brian.lee@ni.com, neil.stoddard@ni.com",
    keywords=['nidaqmx', 'nidaq', 'daqmx', 'daq'],
    license='MIT',
    include_package_data=True,
    packages=['nidaqmx'],
    install_requires=[
        'enum34;python_version<"3.4"',
        'numpy',
        'six'
    ],
    tests_require=['pytest'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: System :: Hardware :: Hardware Drivers"
    ],
    cmdclass={'test': PyTest},
    package_data={pypi_name: ['VERSION']},
)
