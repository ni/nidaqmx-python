"""Structure for storing function parameters metadata from scrapigen."""
from codegen.properties.cluster_elements import ClusterElements


class FunctionsParameter:
    """Structure for storing function metadata from scrapigen."""

    def __init__(self, parameters_metadata):
        """Structure for storing function metadata from scrapigen."""
        self._direction = parameters_metadata["direction"]
        self._parameters_name = parameters_metadata["name"]
        self._type = parameters_metadata["type"]
        self._ctypes_data_type = parameters_metadata["ctypes_data_type"]
        self._python_data_type = parameters_metadata["python_data_type"]
        self._description = parameters_metadata["description"]
        self._is_list = parameters_metadata.get("is_list", False)
        self._has_explicit_buffer_size = parameters_metadata.get("has_explicit_buffer_size", False)
        self._optional = parameters_metadata.get("optional", False)
        self._default = parameters_metadata.get("default", "")
        self._cluster = parameters_metadata.get("cluster", "")
        self._is_enum = False
        if "enum" in parameters_metadata:
            self._enum = parameters_metadata.get("enum")
            self._is_enum = True
        if "cluster_elements" in parameters_metadata:
            self._cluster_elements = []
            for cluster_element in parameters_metadata.get("cluster_elements"):
                self._cluster_elements.append(ClusterElements(cluster_element))

    @property
    def direction(self):
        """str: Direction of the parameter."""
        return self._direction

    @property
    def parameter_name(self):
        """str: The name of the parameter."""
        return self._parameters_name

    @property
    def description(self):
        """str: The description of the parameter."""
        return self._description

    @property
    def enum(self):
        """str: The name of the enum."""
        return self._enum

    @property
    def is_enum(self):
        """bool: Defines if the parameter is boolean or not."""
        return self._is_enum

    @property
    def is_list(self):
        """bool: Defines if the parameter is a list or not."""
        return self._is_list

    @property
    def has_explicit_buffer_size(self):
        """bool: Specifies if an explicit buffer size has to be provided for the c function call."""
        return self._has_explicit_buffer_size

    @property
    def ctypes_data_type(self):
        """str: The type of the attribute as per the ctypes definition in python."""
        return self._ctypes_data_type

    @property
    def python_data_type(self):
        """str: The python data_type of the attribute."""
        return self._python_data_type

    @property
    def optional(self):
        """str: This is used to differentiate the optional from required parameters."""
        return self._optional

    @property
    def default(self):
        """str: The default value of the parameter."""
        return self._default

    @property
    def cluster(self):
        """str: The name of the cluster the parameter."""
        return self._cluster

    @property
    def cluster_elements(self):
        """List of cluster elements: Contains a list of cluster elements."""
        return self._cluster_elements
