<%def name="script_empty_property_getter(attribute)">\
<%
        from nidaqmx_python_generator.utilities.text_wrappers import docstring_wrap
    %>\
    @property
    def ${attribute.name}(self):
        """
        ${attribute.description | docstring_wrap(8, 12)}
        """
        raise NotImplementedError(
            'Reading this NI-DAQmx property is not supported.')
</%def>