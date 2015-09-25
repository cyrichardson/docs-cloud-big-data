
from wadl2rst import text
from wadl2rst.nodes.base import BaseNode
from wadl2rst import table
from wadl2rst import text


class TableNode(BaseNode):

    def to_rst(self):
        """ Return the rst representation of this tag and its children. """

        trs = self.find('tr')
        columns = [child.to_rst() for child in trs[0].children]
        rows = [[child.to_rst() for child in tr.children] for tr in trs[1:]]
        output = table.create_table(columns,rows)

        caption_nodes = self.find('caption')
        if len(caption_nodes) > 0:
            caption_text = caption_nodes[0].to_rst()
            output = ".. table:: " + caption_text + "\n\n" + text.indent(output)

        return output
