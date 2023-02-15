import logging
from collections import namedtuple
from nidaqmx_python_generator.utilities.properties.attribute import attribute

_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())

def get_attributes(metadata, className):
    attributes_metadata = []
    for group_Name, attributes in metadata["attributes"].items():
        for id, attribute_data in attributes.items():
            if(attribute_data["python_class_name"] == className):
                attributes_metadata.append(attribute(id, attribute_data))
    return attributes_metadata

