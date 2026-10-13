import re
from textnode import TextNode, TextType


def extract_text_types(text_type: TextType, text: str) -> list[str]:
    bold_pattern = r"\*\*(.+?)\*\*"
    italic_pattern = r"(?<!\w)_([^_]+)_(?!\w)"
    code_pattern = r"`([^`]+)`"

    if text_type == TextType.BOLD:
        return re.findall(bold_pattern, text)
    elif text_type == TextType.ITALIC:
        return re.findall(italic_pattern, text)
    else:
        return re.findall(code_pattern, text)


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    final_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            final_nodes.append(node)
            continue

        extracted_text = extract_text_types(text_type, node.text)
        if len(extracted_text) == 0:
            final_nodes.append(node)
            continue

        remaining = node.text
        for match in extracted_text:
            before, remaining = remaining.split(f"{delimiter}{match}{delimiter}", 1)
            if before != "":
                final_nodes.append(TextNode(before, TextType.TEXT))
            final_nodes.append(TextNode(match, text_type))

        if remaining != "":
            final_nodes.append(TextNode(remaining, TextType.TEXT))

    return final_nodes