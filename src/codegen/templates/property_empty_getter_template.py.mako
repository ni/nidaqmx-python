<%def name="script_empty_property_getter(attribute)">\
<%
        from codegen.utilities.text_wrappers import docstring_wrap
    %>\
    @property
    def ${attribute.name}(self):
        """
        ${attribute.description | docstring_wrap(8, 12)}
        """
        raise NotImplementedError(
            'Reading this NI-DAQmx property is not supported.')
</%def>