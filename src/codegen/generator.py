"""Codegenerator for generating DAQmx functions."""

import logging
import os
import os.path
import shutil
from pathlib import Path, PureWindowsPath

import codegen.metadata as scrapigen_metadata
from mako.exceptions import text_error_template
from mako.lookup import TemplateLookup
from mako.template import Template

_logger = logging.getLogger(__name__)


def _get_metadata():
    return scrapigen_metadata.metadata


def _get_template(template_file_name):
    """Instantiate the mako template in the given file."""
    current_dir = Path(__file__).parent
    template_directory = current_dir / "templates"
    template_file_path = template_directory / template_file_name
    template_lookup = TemplateLookup(directories=str(template_directory))
    return Template(filename=str(template_file_path), lookup=template_lookup)


def _generate_file(metadata, template_file_name, output_path):
    _logger.info(f"{os.path.basename(output_path)} <-- {template_file_name}")
    template = _get_template(template_file_name)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w+", newline="") as f:
        try:
            output_text = template.render(data=metadata)
        except Exception:
            _logger.error(text_error_template().render())
            raise RuntimeError(
                f'An error occurred while rendering template "{template_file_name}"'
            ) from None
        f.write(output_text)


def _copy_handwritten_files(dest):
    parent_dir = Path(__file__).parent.parent
    source_path = parent_dir / "handwritten"
    shutil.copytree(source_path, dest, dirs_exist_ok=True)


def generate(dest):
    """Generates the DAQmx classes using scrapigen metadata."""
    _logger.info(f"Generating files into {dest}")

    os.makedirs(dest, exist_ok=True)

    codegen_metadata = _get_metadata()

    for info in codegen_metadata["script_info"]["modules"]:
        _generate_file(
            codegen_metadata,
            PureWindowsPath(info["templateFile"]),
            dest / PureWindowsPath(info["relativeOutputPath"]),
        )

    _generate_file(codegen_metadata["enums"], "error_codes.mako", dest / "error_codes.py")

    _generate_file(codegen_metadata, "constants.mako", dest / "constants.py")

    _copy_handwritten_files(dest)
