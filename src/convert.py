from htmlnode import (
    ParentNode,
    LeafNode,

)

from blocks import (
    markdown_to_blocks,
    block_to_block_type,
    BlockType
)

from textnode import(
    text_node_to_html_node,
)

from markdownstrings import(
    text_to_textnodes
)

def markdown_to_html_node(markdown):
    
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)

    return ParentNode("div", children, None)

def block_to_html_node(block):
    # write code here that takes different blocks and depending on the type, returns a different html node
    #they called many functions and depending on the type (code etc.) gave it clear instructions for how to treat it
    # so basically one function each for (paragraph, heading, code, olist, ulist and quote) and then one text_to_children  that
    # I created a shared text_to_children(text) function that works for all block types. 
    # It takes a string of text and returns a list of HTMLNodes that represent the inline markdown 
    # using previously created functions (think TextNode -> HTMLNode).
    return




