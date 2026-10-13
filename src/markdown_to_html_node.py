from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from markdown_to_blocks import markdown_to_blocks
from blocktype import block_to_block_type, BlockType
from text_to_textnodes import text_to_textnodes
from textnode import text_node_to_html_node
def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)


    children = []
    for block in blocks:
        
        block_type = block_to_block_type(block)
        if block_type == BlockType.QUOTE and len(block) > 0:
            block_split = block.split("\n")
            for i in block_split:
                if len(i[1:].strip()) > 0:

                    text_nodes = text_to_textnodes(i[1:].strip())
                    final_text_nodes = []
                    for j in text_nodes:
                        final_text_nodes.append(text_node_to_html_node(j))
                                           
                    children.append(ParentNode(
                        tag="blockquote",
                        children=final_text_nodes,
                        props=None
                    ))
        elif block_type == BlockType.PARAGRAPH and len(block) > 0:
            
            text_nodes = text_to_textnodes(block)
            final_text_nodes = []
            for i in text_nodes:
                final_text_nodes.append(text_node_to_html_node(i))
           
            children.append(ParentNode(
                tag="p",
                children=final_text_nodes,
                props=None))
        elif block_type == BlockType.CODE and len(block) > 0:
            print("".join(block.strip("`").strip(" ").lstrip("\n").split("\n")))
            children.append(ParentNode(
                tag="pre",
                children=[
                    LeafNode(
                        tag="code",
                        value=block.strip("`").strip(" ").lstrip("\n"),
                        props=None
                    )
                ],
                props=None))
            
        elif block_type == BlockType.HEADING and len(block) > 0:
            if block.count("#") == 6:
                children.append(LeafNode(
                    tag="h6",
                    value=block[7:].strip(),
                    props=None ))
            elif block.count("#") == 5:
                children.append(LeafNode(
                    tag="h5",
                    value=block[6:].strip(),
                    props=None ))
            elif block.count("#") == 4:
                children.append(LeafNode(
                    tag="h4",
                    value=block[5:].strip(),
                    props=None ))
            elif block.count("#") == 3:
                children.append(LeafNode(
                    tag="h3",
                    value=block[4:].strip(),
                    props=None ))
            elif block.count("#") == 2:
                children.append(LeafNode(
                    tag="h2",
                    value=block[3:].strip(),
                    props=None ))
            elif block.count("#") == 1:
                children.append(LeafNode(
                    tag="h1",
                    value=block[2:].strip(),
                    props=None ))
        
        elif block_type == BlockType.UNORDERED_LIST and len(block) > 0:
            list_unordered = block.split("\n")

            final_list = []

            for i in list_unordered:
                text_nodes = text_to_textnodes(i[2:])
                final_text_nodes = []
                for j in text_nodes:
                    final_text_nodes.append(text_node_to_html_node(j))
                           
                final_list.append(ParentNode(tag="li",
                                children=final_text_nodes,
                                props=None))

            children.append(ParentNode(
                                tag="ul",
                                children=final_list,
                                props=None))
        elif block_type == BlockType.ORDERED_LIST and len(block) > 0:
            list_unordered = block.split("\n")
            
            final_list = []
            
            for i in list_unordered:
                text_nodes = text_to_textnodes(i[3:])
                final_text_nodes = []
                for j in text_nodes:
                    final_text_nodes.append(text_node_to_html_node(j))
                                       
                final_list.append(ParentNode(tag="li",
                                children=final_text_nodes,
                                props=None))
            
            children.append(ParentNode(
                tag="ol",
                children=final_list,
                props=None))

    final_node = ParentNode(
        tag="div",
        children=children,
        props=None
    )
    return final_node

            

