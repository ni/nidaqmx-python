"""Helpers class to generate helper functions for the metadata."""
from enum import Enum
import re
from collections import namedtuple

# Pre-compile regexes to speed up matches
CAMEL_TO_SNAKE_CASE_REGEXES = [
    re.compile("([^_\n])([A-Z][a-z]+)"),
    re.compile("([a-z])([A-Z])"),
    re.compile("([0-9])([^_0-9])"),
    re.compile("([^_0-9])([0-9])"),
]

PascalTokenSubstitution = namedtuple(
    "PascalTokenSubstitution", ["pascal_representation", "preferred_representation"]
)

SPECIAL_CASE_PASCAL_TOKENS = [
    # NI uses UInt, not Uint, and never U_INT when converting to snake.
    PascalTokenSubstitution("Uint", "UInt"),
]

NAME_CHANGE_SET = {
    "cdaq": "CDAQ",
    "ao": "AO",
    "ai": "AI",
    "co": "CO",
    "do": "DO",
    "teds": "TEDS",
    "iepe": "IEPE",
    "rms": "RMS",
    "dc": "DC",
    "lvdt": "LVDT",
    "rvdt": "RVDT",
    "airtd": "AIRTD",
    "ci": "CI",
    "di": "DI",
    "cigps": "CIGPS",
    "tedsai": "TEDSAI",
    "tedsairtd": "TEDSAIRTD",
}


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


def snake_to_pascal(snake_string):
    """Return a PascalString for a given snake_string."""
    snake_string = _modify_function_name(snake_string)
    snake_string = list(snake_string)
    index = 0
    snake_string[index] = snake_string[index].upper()
    for x in snake_string:
        if x == "_":
            snake_string[index + 1] = snake_string[index + 1].upper()
            del snake_string[index]
        index = index + 1
    result = "".join(snake_string)
    return _insert_special_case_pascal_tokens(result)


def _insert_special_case_pascal_tokens(normal_pascal_string: str) -> str:
    for pascal_token, special_case_override in SPECIAL_CASE_PASCAL_TOKENS:
        normal_pascal_string = normal_pascal_string.replace(pascal_token, special_case_override)
    return normal_pascal_string


def _modify_function_name(snake_string):
    function_names = snake_string.split("_")
    substituted_name = []
    for name in function_names:
        if name in NAME_CHANGE_SET:
            substituted_name.append(NAME_CHANGE_SET[name])
        else:
            substituted_name.append(name)
    return "_".join(substituted_name)

class AttributeFunctionType(Enum):
    GET = 0
    SET = 1
    RESET = 2
    NONE = 3    

def get_attribute_function_type(function_name: str):
    """Sets attribute function type as get/set/reset or not a attribute function."""
    if "attribute" in function_name:
        if function_name.startswith("get"):
            return AttributeFunctionType.GET
        elif function_name.startswith("set"):
            return AttributeFunctionType.SET    
        elif function_name.startswith("reset"):
            return AttributeFunctionType.RESET
        
    return AttributeFunctionType.NONE