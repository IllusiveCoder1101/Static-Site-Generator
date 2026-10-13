from textnode import TextNode, TextType
from split_nodes_image import split_nodes_image
from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_link import split_nodes_link


def text_to_textnodes(text: str) -> list[TextNode]:
    old_nodes = [
        TextNode(text, TextType.TEXT)
    ]
    res = split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter(old_nodes, "`", TextType.CODE), "**", TextType.BOLD), "_", TextType.ITALIC)

    res1 = split_nodes_image(res)
    res2 = split_nodes_link(res1)

    res3 = [n for n in res2 if not (n.text == "" and n.text_type == TextType.TEXT)]

    return  res3
    



