from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT= "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text: str, text_type: TextType, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other) -> bool:

        if self.url == other.url and self.text == other.text and self.text_type == other.text_type:
            return True
        return False
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node) -> LeafNode:
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, " ".join(text_node.text.split("\n")), None)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text, None)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text, None)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text, None)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, props={"href": text_node.url})
    else :
        return LeafNode("img", None, props={"src":text_node.url, "alt": text_node.text})