<%def name="script_property(attribute)">\
<%namespace name="property_getter_template" file="/property_getter_template.py.mako"/>\
<%namespace name="property_empty_getter_template" file="/property_empty_getter_template.py.mako"/>\
<%namespace name="property_setter_template" file="/property_setter_template.py.mako"/>\
<%namespace name="property_deleter_template" file="/property_deleter_template.py.mako"/>\
    %if attribute.access == "read":
${property_getter_template.script_property_getter(attribute)}
    %elif attribute.access == "write":
${property_empty_getter_template.script_empty_property_getter(attribute)}
${property_setter_template.script_property_setter(attribute)}
    %elif attribute.access == "read-write":
${property_getter_template.script_property_getter(attribute)}
${property_setter_template.script_property_setter(attribute)}
    %endif
\
    %if attribute.resettable:
${property_deleter_template.script_property_deleter(attribute)}
    %endif
</%def>