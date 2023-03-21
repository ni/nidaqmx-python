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
    camel_case_string = _fix_tedsairtd(camel_case_string)
    camel_case_string = _fix_tedsai(camel_case_string)
    camel_case_string = _fix_airtd(camel_case_string)
    partial = camel_case_string
    for regex in CAMEL_TO_SNAKE_CASE_REGEXES:
        partial = regex.sub(r"\1_\2", partial)

    return partial.lower()


def _fix_tedsairtd(input_string: str) -> str:
    # change TEDSAIRTD to TEDS_AI_RTD.
    return input_string.replace("TEDSAIRTD", "TEDS_AI_RTD")


def _fix_tedsai(input_string: str) -> str:
    # change TEDSAI to TEDS_AI.
    return input_string.replace("TEDSAI", "TEDS_AI")


def _fix_airtd(input_string: str) -> str:
    # change AIRTD to AI_RTD.
    return input_string.replace("AIRTD", "AI_RTD")
