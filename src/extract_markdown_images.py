import re

def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    extract_images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    final_extract = []
    for i in extract_images:
        final_extract.append(i)
    return final_extract