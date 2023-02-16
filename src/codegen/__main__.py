import logging
import pathlib
import sys

import codegen.generator as generator

_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())

def _parse_args(argv):
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--dest",
        type=pathlib.Path,
        help="Destination directory",
        required=True,
    )

    debug_group = parser.add_argument_group("Debug")
    debug_group.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Print debug information.  Can be repeated for more detailed output.",
    )
    debug_group.add_argument(
        "-q",
        "--quiet",
        action="count",
        default=0,
        help="Print only essential information.  Can be repeated for quieter output.",
    )

    args = parser.parse_args(argv)

    if 0 < args.verbose and 0 < args.quiet:
        parser.error("Mixing --verbose and --quiet is contradictory")
    verbosity = 2 + args.quiet - args.verbose
    verbosity = max(verbosity, 0)
    verbosity = min(verbosity, 4)
    args.logging_level = {
        0: logging.DEBUG,
        1: logging.INFO,
        2: logging.WARNING,
        3: logging.ERROR,
        4: logging.CRITICAL,
    }[verbosity]

    return args

def main(argv=None):
    if argv is None:
        argv = sys.argv
    args = _parse_args(argv[1:])

    log_format = "[%(relativeCreated)6d] %(levelname)-5s %(funcName)s: %(message)s"
    logging.basicConfig(level=args.logging_level, format=log_format)

    try:
        generator.generate(args)
    except Exception:
        _logger.exception("Failed to generate")
        return 1

if __name__ == "__main__":
    sys.exit(main())
