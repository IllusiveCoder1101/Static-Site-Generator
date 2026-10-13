
from textnode import TextNode, TextType
from extract_markdown_links import extract_markdown_links

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    final_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            final_nodes.append(node)
            continue

        images = extract_markdown_links(node.text)
        if len(images) == 0:
            final_nodes.append(node)
            continue

        remaining = node.text
        for alt, url in images:
            before, remaining = remaining.split(f"[{alt}]({url})", 1)
            if before != "":
                final_nodes.append(TextNode(before, TextType.TEXT))
            final_nodes.append(TextNode(alt, TextType.LINK, url))

        if remaining != "":
            final_nodes.append(TextNode(remaining, TextType.TEXT))

    return final_nodes

