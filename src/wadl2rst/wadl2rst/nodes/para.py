
import re

from wadl2rst.nodes.base import BaseNode

COMMA_CLEANUP = re.compile(r"[\s]+(?P<foo>,|\.)")
SPACE_CLEANUP = re.compile(r"[ ]+")
LEADING_SPACE_CLEANUP = re.compile(r"^[ ]+")
IGNORE_TABLE_LINES = re.compile(r"^ *[+|]")

class ParaNode(BaseNode):

    def to_rst(self):
        """ Return the rst representation of this tag and it's children. """

        child_rst = ""

        for child in self.children:
            if child.name == "table":
                child_rst += "\n\n"
            else:
                child_rst += " "
            child_rst += child.to_rst()

        lines = child_rst.split("\n")
        child_rst = ""

        for line in lines:
            child_rst += cleanup_spaces(line) + "\n"

        return child_rst + "\n"

def cleanup_spaces(rst_text):
    if IGNORE_TABLE_LINES.match(rst_text):
        return rst_text

    # collapse any strings of whitespace into a single space
    rst_text = SPACE_CLEANUP.sub(" ", rst_text)

    # remove any whitespace before punctuation.
    rst_text = COMMA_CLEANUP.sub(r"\1", rst_text)
    rst_text = LEADING_SPACE_CLEANUP.sub("", rst_text)
    return rst_text
