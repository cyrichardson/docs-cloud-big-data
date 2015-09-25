
from wadl2rst.nodes.base import BaseNode
from wadl2rst import text


class RepresentationNode(BaseNode):

    def to_example(self):
        output = u"\n\n".join([child.to_rst() for child in self.children \
            if child.name != 'params'])
        if output.strip() == '':
            return None

        try:
            doc_node = self.find_one_of(["wadl:doc", "doc"])
            title = doc_node.attributes.get("title", None)
        except ValueError, e:
            title = None

        media_type = self.attributes.get('mediaType', None)
        media_type = mimetype_translation.get(media_type, "JSON")

        return {
            "title": title,
            "type": media_type,
            "rst": output
        }


mimetype_translation = {
    "application/json": "JSON",
    "application/xml": "XML",
    "application/http": "HTTP"
}
