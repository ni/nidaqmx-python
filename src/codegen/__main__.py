"""DAQmx code generator."""

import logging
import pathlib
import sys

import click

try:
    sys.path.append(str(pathlib.Path(__file__).parent.parent))
    import codegen.generator
    import codegen.stub_generator
finally:
    pass

_logger = logging.getLogger(__name__)


def _get_logging_level(verbose, quiet):
    if 0 < verbose and 0 < quiet:
        click.exceptions.error("Mixing --verbose and --quiet is contradictory")
    verbosity = 2 + quiet - verbose
    verbosity = max(verbosity, 0)
    verbosity = min(verbosity, 4)
    logging_level = {
        0: logging.DEBUG,
        1: logging.INFO,
        2: logging.WARNING,
        3: logging.ERROR,
        4: logging.CRITICAL,
    }[verbosity]

    return logging_level


@click.command()
@click.option("--dest", type=pathlib.Path)
@click.option("--verbose", type=int, default=0, required=False)
@click.option("--quiet", type=int, default=0, required=False)
def main(dest, verbose, quiet):
    """Starts the code generator based on the out folders."""
    logging_level = _get_logging_level(verbose, quiet)

    log_format = "[%(relativeCreated)6d] %(levelname)-5s %(funcName)s: %(message)s"
    logging.basicConfig(level=logging_level, format=log_format)

    codegen.generator.generate(dest)
    codegen.stub_generator.generate_stubs()


if __name__ == "__main__":
    main()
