
import re

from wadl2rst.nodes.base import BaseNode

COMMA_CLEANUP = re.compile(r"[\s]+(?P<foo>,|\.)")
SPACE_CLEANUP = re.compile(r"[ ]+")
LEADING_SPACE_CLEANUP = re.compile(r"^[ ]+")

class ParaNode(BaseNode):

    def to_rst(self):
        """ Return the rst representation of this tag and it's children. """

        child_rst = u" ".join([child.to_rst() for child in self.children])

        # collapse any strings of whitespace into a single space
        child_rst = SPACE_CLEANUP.sub(" ", child_rst)

        # remove any whitespace before punctuation.
        child_rst = COMMA_CLEANUP.sub(r"\1", child_rst)
        child_rst = LEADING_SPACE_CLEANUP.sub("", child_rst)

        return child_rst + "\n\n"
