
import re

def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    extract_links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    final_extract = []
    for i in extract_links:
        final_extract.append(i)
    return final_extract