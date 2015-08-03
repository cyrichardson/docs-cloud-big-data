
from wadl2rst import text
from wadl2rst.nodes.base import BaseNode


class WarningNode(BaseNode):

    def to_rst(self):
        """ Return the rst representation of this tag and it's children. """

        child_rst = u"".join([child.to_rst() for child in self.children])
        return ".. warning::\n" + text.indent(child_rst, 3)
