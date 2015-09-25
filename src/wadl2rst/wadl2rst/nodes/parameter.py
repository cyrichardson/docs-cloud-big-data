
from wadl2rst.nodes.base import BaseNode


class ParameterNode(BaseNode):
    """
    Parameters in WADL were rendered in tree-format to show a
    nested relationship of parameters.  Each element has a name
    as well as a path to indicate the parent element(s).
    """

    def get_table_row(self):
        param_type = self.attributes.get('type', '')
        if(param_type.find(":") != -1):
            param_type = (param_type.split(":")[1]).capitalize()
        else:
            param_type = param_type.capitalize()

        name = self.attributes.get('name', '')

        if self.attributes.get('style', '') == "template":
            name = "{" + name + "}"

        required_attribute = self.attributes.get('required', None)
        if required_attribute is not None:
            param_type_qualifier = 'Required' if required_attribute.lower() == "true" else 'Optional'
            param_type += " *({})*".format(param_type_qualifier)

        path = self.attributes.get('path', None)
        if path is not None:
            # escaping whitespace in order to do rst inline markup
            name = path.lstrip('$.').replace(name, "\ **%s**" % (name))

        return [name, param_type, self.to_rst()]
