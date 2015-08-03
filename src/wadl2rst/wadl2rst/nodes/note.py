
from wadl2rst import text
from wadl2rst.nodes.base import BaseNode


class NoteNode(BaseNode):

    def to_rst(self):
        """ Return the rst representation of this tag and it's children. """

        child_rst = " ".join([child.to_rst() for child in self.children])
        return ".. note::\n" + text.indent(child_rst, 3)
