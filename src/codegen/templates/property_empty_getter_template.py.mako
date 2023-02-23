<%def name="script_empty_property_getter(attribute)">\
<%
        from codegen.utilities.text_wrappers import docstring_wrap
    %>\
    @property
    def ${attribute.name}(self):
        """
        ${attribute.get_return_type() + ": " + attribute.python_description | docstring_wrap(initial_indent=8, subsequent_indent=12)}
        """
        raise NotImplementedError(
            'Reading this NI-DAQmx property is not supported.')
</%def>