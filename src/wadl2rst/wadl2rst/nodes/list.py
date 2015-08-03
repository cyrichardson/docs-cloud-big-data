
import re

from wadl2rst import text
from wadl2rst.nodes.base import BaseNode


class ListNode(BaseNode):

    def to_rst(self):
        symbol = self.list_symbol()
        items = [text.indent(child.to_rst(), 3) for child in self.children]
        items = [item.rstrip() for item in items]
        items = [symbol + item[2:] + "\n" for item in items]
        return u"\n\n" + u"".join(items) + u"\n\n"

    def list_symbol(self):
        if self.name == "orderedlist":
            return "#."
        else:
            return "* "
