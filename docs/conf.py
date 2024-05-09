"""Sphinx Configuration File."""

import datetime
import os
import pathlib
import sys
import toml

sys.path.insert(0, os.path.abspath('../'))


# -- General configuration ------------------------------------------------

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.coverage',
              'sphinx.ext.viewcode',
              'sphinx.ext.napoleon']

source_suffix = '.rst'

master_doc = 'index'

root_path = pathlib.Path(__file__).parent.parent
pyproj_file = root_path / "pyproject.toml"
proj_config = toml.loads(pyproj_file.read_text())

project = proj_config["tool"]["poetry"]["name"]
company = "National Instruments"
author = company
copyright = f"{datetime.datetime.now().year}, {company}"

# Release is the full version, version is only the major component
release = proj_config["tool"]["poetry"]["version"]
version = ".".join(release.split(".")[:2])
description = proj_config["tool"]["poetry"]["description"]

language = 'en'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

pygments_style = 'sphinx'

todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_static_path = []


# -- Options for HTMLHelp output ------------------------------------------

htmlhelp_basename = 'NI-DAQmxPythonAPIdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
}

latex_documents = [
    (master_doc, 'NI-DAQmxPythonAPI.tex', 'NI-DAQmx Python API Documentation',
     'National Instruments', 'manual'),
]


# -- Options for manual page output ---------------------------------------

man_pages = [
    (master_doc, 'ni-daqmxpythonapi', 'NI-DAQmx Python API Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

texinfo_documents = [
    (master_doc, 'NI-DAQmxPythonAPI', 'NI-DAQmx Python API Documentation',
     author, 'NI-DAQmxPythonAPI', 'One line description of project.',
     'Miscellaneous'),
]
