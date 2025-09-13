"""'nidaqmx' command line utility."""

from __future__ import annotations

import logging

import click

from . import _install_daqmx


@click.group("nidaqmx")
@click.option(
    "-v",
    "--verbose",
    "verbosity",
    count=True,
    help="Enable verbose logging. Repeat to increase verbosity.",
)
def main(  # noqa: D103 - Missing docstring in public function (auto-generated noqa)
    verbosity: int,
) -> None:
    _configure_logging(verbosity)


@main.command()
def installdriver():  # noqa: D103 - Missing docstring in public function (auto-generated noqa)
    _install_daqmx.installdriver()


def _configure_logging(verbosity: int) -> None:
    """Configure logging for this process."""
    if verbosity > 1:
        level = logging.DEBUG
    elif verbosity == 1:
        level = logging.INFO
    else:
        level = logging.WARNING
    logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", level=level)


if __name__ == "__main__":
    main()
