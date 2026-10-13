import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH="paragraph"
    HEADING="heading"
    CODE="code"
    QUOTE="quote"
    UNORDERED_LIST="unordered_list"
    ORDERED_LIST="ordered_list" 

def is_ordered_list(lines):
    ordered_pattern   = r"^(\d+)\. (.+)$"
    for i, line in enumerate(lines, start=1):
        m = re.match(ordered_pattern, line)
        if not m or int(m.group(1)) != i:
            return False
    return True

def block_to_block_type(markdown : str) ->  BlockType:
    original_block = markdown
    block = markdown.split("\n")

    heading_pattern   = r"^(#{1,6}) (.+)$"
    code_pattern      = r"\A```\n(.*?)\n```\Z"
    quote_pattern     = r"^>[ ]?(.*)$"
    unordered_pattern = r"^- (.+)$"
    

    if re.match(heading_pattern, original_block):
        return BlockType.HEADING
    if (original_block.startswith("```\n") and original_block.endswith("```")) or (original_block.startswith("`") and original_block.endswith("`")):
        return BlockType.CODE
    if all(re.match(quote_pattern, l) for l in block):
        return BlockType.QUOTE
    if all(re.match(unordered_pattern, l) for l in block):
        return BlockType.UNORDERED_LIST
    if is_ordered_list(block):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH