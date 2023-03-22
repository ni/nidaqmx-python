"""Helpers class to generate helper functions for the metadata."""
import re


# Pre-compile regexes to speed up matches
CAMEL_TO_SNAKE_CASE_REGEXES = [
    re.compile("([^_\n])([A-Z][a-z]+)"),
    re.compile("([a-z])([A-Z])"),
    re.compile("([0-9])([^_0-9])"),
    re.compile("([^_0-9])([0-9])"),
]


def camel_to_snake_case(camel_case_string):
    """Converts a camelCase string to a snake_case string."""
    partial = camel_case_string
    for regex in CAMEL_TO_SNAKE_CASE_REGEXES:
        partial = regex.sub(r"\1_\2", partial)

    return partial.lower()
