from markdown_to_blocks import markdown_to_blocks
def extract_title(markdown: str)-> str:
    blocks = markdown_to_blocks(markdown)

    for i in blocks:
        if i.startswith("# "):
            return i[2:].strip()

    raise Exception("No title found!")
