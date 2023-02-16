import logging
from collections import namedtuple
from codegen.properties.attribute import Attribute

_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())

def get_attributes(metadata, class_name):
    attributes_metadata = []
    for group_name, attributes in metadata["attributes"].items():
        for id, attribute_data in attributes.items():
            if(attribute_data["python_class_name"] == class_name):
                attributes_metadata.append(Attribute(id, attribute_data))
    return attributes_metadata

