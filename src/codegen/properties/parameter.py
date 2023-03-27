"""Structure for storing parameter metadata from scrapigen."""


class Parameter:
    """Structure for storing parameter metadata from scrapigen."""

    def __init__(self, name, parameter_metadata):
        """Structure for storing parameter metadata from scrapigen."""
        self._handle_name = name
        self._accessor = parameter_metadata.get(
            "python_accessor", parameter_metadata.get("accessor")
        )
        assert self._accessor is not None
        self._ctypes_data_type = parameter_metadata["ctypes_data_type"]
        self._cvi_name = parameter_metadata["cvi_name"]

    @property
    def handle_name(self):
        """str: The key of the parameter."""
        return self._handle_name

    @property
    def accessor(self):
        """str: Defines how to access the handle parameter.

        This value would be directly substituted when trying to use the handle parameter
        """
        return self._accessor

    @property
    def ctypes_data_type(self):
        """str: Defines the ctypes data_type of the handle parameter.

        This is used when mentioning the data_type of the handle parameter.
        """
        return self._ctypes_data_type

    @property
    def cvi_name(self):
        """str: The cvi name of the parameter.

        This is kept for the gRPC client implementation.
        """
        return self._cvi_name
