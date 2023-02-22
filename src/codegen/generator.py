import logging
import os
import os.path

from pathlib import Path

from mako.lookup import TemplateLookup
from mako.template import Template

import codegen.metadata as scrapigen_metadata

_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())


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
        f.write(template.render(data=metadata))


def generate(dest):
    _logger.info(f"Generating files into {dest}")

    os.makedirs(dest, exist_ok=True)

    codegen_metadata = _get_metadata()

    for info in codegen_metadata["script_info"]["modules"]:
        _generate_file(
            codegen_metadata, info["templateFile"], dest / info["relativeOutputPath"]
        )
