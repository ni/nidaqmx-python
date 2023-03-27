<%def name="script_deprecated_property(attributes)">\
<%
        from codegen.utilities.attribute_helpers import get_deprecated_attributes
        deprecated_attributes = get_deprecated_attributes(attributes)
    %>\
%for old_property, attribute in deprecated_attributes.items():
    @property
    @deprecation.deprecated(deprecated_in="${attribute["deprecated_in"]}", details="Use ${attribute["new_name"]} instead.")
    def ${old_property}(self):
        return self.${attribute["new_name"]}

    %if attribute["access"] != "read":
    @${old_property}.setter
    @deprecation.deprecated(deprecated_in="${attribute["deprecated_in"]}", details="Use ${attribute["new_name"]} instead.")
    def ${old_property}(self, val):
        self.${attribute["new_name"]} = val

    %endif
    %if attribute["resettable"]:
    @${old_property}.deleter
    @deprecation.deprecated(deprecated_in="${attribute["deprecated_in"]}", details="Use ${attribute["new_name"]} instead.")
    def ${old_property}(self):
        del self.${attribute["new_name"]}

    %endif
%endfor
</%def>