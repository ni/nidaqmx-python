"""Structure for storing cluster metadata from scrapigen."""


class ClusterElements:
    """Structure for storing cluster metadata from scrapigen."""

    def __init__(self, cluster_metadata):
        """Structure for storing cluster metadata from scrapigen."""
        self._name = cluster_metadata["name"]
        self._ctypes_data_type = cluster_metadata["ctypes_data_type"]

    @property
    def name(self):
        """str: The name of the cluster element."""
        return self._name

    @property
    def ctypes_data_type(self):
        """str: The type of the attribute as per the ctypes definition in python."""
        return self._ctypes_data_type
