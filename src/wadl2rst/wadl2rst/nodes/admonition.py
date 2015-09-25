
from wadl2rst import text
from wadl2rst.nodes.base import BaseNode


class AdmonitionNode(BaseNode):
    """
    Admonitions are specially marked topics that can appear anywhere
    an ordinary body element can.  They contain arbitrary body elements.

    http://docutils.sourceforge.net/docs/ref/rst/directives.html#admonitions
    """
    directive = 'admonition'

    def to_rst(self):
        """
        Return the rst representation of this tag and it's children.
        """
        child_rst = u"".join([child.to_rst() for child in self.children])
        rst = ".. %s::\n" % (self.directive)

        return rst + text.indent(child_rst, 3)


class WarningNode(AdmonitionNode):
    """
    Specifically the warning directive type.
    """
    directive = 'warning'


class ImportantNode(AdmonitionNode):
    """
    Specifically the important directive type.
    """
    directive = 'important'


class NoteNode(AdmonitionNode):
    """
    Specifically the important directive type.
    """
    directive = 'note'
