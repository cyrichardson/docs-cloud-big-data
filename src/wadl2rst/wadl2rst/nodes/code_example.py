
from wadl2rst import text
from wadl2rst.nodes.base import BaseNode


class CodeExampleNode(BaseNode):

    def __init__(self, parent, char_data):
        super(CodeExampleNode, self).__init__(parent, "char", {'text': char_data})

    def clone(self):
        clone = self.__class__(self.parent, self.attributes['text'])
        clone.children = [c.clone() for c in self.children]
        return clone

    def to_rst(self):
        """ Return the rst representation of this tag and it's children. """

        return ".. code::\n\n" + text.indent(self.attributes['text'], 3) + "\n"
