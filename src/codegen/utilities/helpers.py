"""Helpers class to generate helper functions for the metadata."""
import re


# Pre-compile regexes to speed up matches
CAMEL_TO_SNAKE_CASE_REGEXES = [
    re.compile("([^_\n])([A-Z][a-z]+)"),
    re.compile("([a-z])([A-Z])"),
    re.compile("([0-9])([^_0-9])"),
    re.compile("([^_0-9])([0-9])"),
]


def camel_to_snake_case(camel_case_string, regexes=CAMEL_TO_SNAKE_CASE_REGEXES):
    """Converts a camelCase string to a snake_case string."""
    partial = camel_case_string
    for regex in regexes:
        partial = regex.sub(r"\1_\2", partial)

    return partial.lower()


def get_enums_to_import(enums_in_attributes, enums_in_functions):
    """Gets the enums that needs to imported for the attributes and functions used."""
    enums_to_import = enums_in_attributes + enums_in_functions
    enums_to_import = list(set(enums_to_import))
    return sorted(enums_to_import)


def strip_class_name(name: str, class_name: str, replace_with=""):
    """Strips class name from name."""
    return re.sub(class_name, replace_with, name)
