
def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    final_res = []
    for i in blocks:
        text_split = i.split("\n")
        res = "\n".join([k.strip() for k in text_split])
        final_res.append(res.strip("\n"))


    return final_res