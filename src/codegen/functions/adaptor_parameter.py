"""Structure for storing adaptor parameter from scrapigen."""


class AdaptorParameter:
    """Structure for storing adaptor parameter from scrapigen."""

    def __init__(self, adaptor_parameter):
        """Structure for storing adaptor parameter from scrapigen."""
        self._adaptor = adaptor_parameter["python_adaptor"]
        self._data_type = adaptor_parameter["python_data_type"]
        self._direction = adaptor_parameter["direction"]
        self._description = adaptor_parameter["description"]

    @property
    def adaptor(self):
        """str: Defines the string that should be used when using the parameter."""
        return self._adaptor

    @property
    def data_type(self):
        """str: Defines the data type of the parameter."""
        return self._data_type

    @property
    def direction(self):
        """str: Direction of the parameter."""
        return self._direction

    @property
    def description(self):
        """str: The documentation of the parameter."""
        return self._description
