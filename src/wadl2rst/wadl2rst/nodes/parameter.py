
from wadl2rst.nodes.base import BaseNode


class ParameterNode(BaseNode):

    def get_table_row(self):
        param_type = self.attributes.get('type', '')
        name = self.attributes.get('name', '')

        if self.attributes.get('style', '') == "template":
            name = "{" + name + "}"

        required_attribute = self.attributes.get('required', None)
        if required_attribute is not None:
            param_type_qualifier = 'Required' if required_attribute.lower() == "true" else 'Optional'
            param_type += " *({})*".format(param_type_qualifier)

        return [name, param_type, self.to_rst()]
