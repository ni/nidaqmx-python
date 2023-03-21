"""This contains the helper methods used in functions generation."""
from codegen.functions.function import Function
from codegen.utilities.helpers import camel_to_snake_case


def get_functions(metadata):
    """Converts the scrapigen metadata into a list of functions."""
    all_functions = metadata["functions"]
    functions_metadata = []
    for function_name, function_data in all_functions.items():
        if "python_class_name" in all_functions[function_name] and all_functions[function_name]["python_class_name"] == "AIChannelCollection":
            function_data["c_function_name"] = function_name
            functions_metadata.append(
                Function(get_function_name(function_name), function_data))

    return sorted(functions_metadata, key=lambda x: x._function_name)


def get_function_name(function_name: str):
    """Replaces the 'create' with 'add' and converts function name to camel to snake case."""
    if function_name.startswith("Create"):
        function_name = "add" + function_name[6:]
    return camel_to_snake_case(function_name)


def get_enums_used(functions):
    """Gets the list of enums used in the attribute metadata."""
    used_enums = []
    for function_data in functions:
        for param in function_data._parameters:
            if param.is_enum:
                used_enums.append(param._python_data_type)
        used_enums = list(set(used_enums))

    return sorted(used_enums)


def order_function_parameters_by_optional(function_parameters):
    """Sorts function prameters by optional and non optional for function defintion."""
    optional_params = []
    non_optional_params = []
    for param in function_parameters:
        if param._optional:
            optional_params.append(param)
        else:
            non_optional_params.append(param)

    return non_optional_params + optional_params
