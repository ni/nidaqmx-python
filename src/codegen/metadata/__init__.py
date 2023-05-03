from .attributes import attributes
from .functions import functions
from .script_info import script_info
from .enums import enums
from .functions_addon import functions_override_metadata

copy_functions = functions.copy()
def update_functions():
    for function_name, function_data in functions_override_metadata.items():
        copy_functions[function_name] = {**copy_functions[function_name], **functions_override_metadata[function_name]}
    return copy_functions

all_functions = update_functions() 

metadata = {"attributes": attributes, "script_info": script_info, "enums": enums, "functions": all_functions}