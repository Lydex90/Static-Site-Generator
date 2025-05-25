from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    list_nodes = []

    for node in old_nodes:
        if node.text_type != text_type.TEXT:
            list_nodes.extend([node])
            continue
        elif delimiter not in node.text:
            list_nodes.extend([node])
            continue
            
            #raise ValueError("delimiter not found")
        
        node_split = node.text.split(delimiter)
        for i in range(0,len(node_split)):
                if node_split[i] == "":
                        continue
                        
                elif i % 2 == 0:
                    nu_node = TextNode(node_split[i], TextType.TEXT)
                else:
                    nu_node = TextNode(node_split[i], text_type)
                list_nodes.extend([nu_node])             
        
    return list_nodes


def extract_markdown_images(text):
    target_list = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return target_list

def extract_markdown_links(text):
    target_list = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return target_list

def split_nodes_image(old_nodes):
    list_nodes = []
    
    for node in old_nodes:
        text = node.text
        matches = extract_markdown_images(text)
        if not matches:
             list_nodes.append(node)
             continue
        current_index = 0
        for alt_text, url in matches:
            # Create the full markdown pattern to find the position
            markdown = f"![{alt_text}]({url})"
            index = text.find(markdown, current_index)
            if index == -1:
                 continue # shouldn't happen, but safety check
            
            # Add any plain text before this markdown image
            if index > current_index:
                 plain_text = text[current_index: index]
                 list_nodes.append(TextNode(plain_text, TextType.TEXT))
            
            # Add Image node
            list_nodes.append(TextNode(alt_text, TextType.IMAGE, url))

            current_index = index + len(markdown)

        if current_index < len(text):
            list_nodes.append(TextNode(text[current_index:], TextType.TEXT))
    return list_nodes

def split_nodes_link(old_nodes):
    list_nodes = []
    
    for node in old_nodes:
        text = node.text
        matches = extract_markdown_links(text)
        if not matches:
             list_nodes.append(node)
             continue
        current_index = 0
        for vis_text, url in matches:
            # Create the full markdown pattern to find the position
            markdown = f"[{vis_text}]({url})"
            index = text.find(markdown, current_index)
            if index == -1:
                 continue # shouldn't happen, but safety check
            
            # Add any plain text before this markdown link
            if index > current_index:
                 plain_text = text[current_index: index]
                 list_nodes.append(TextNode(plain_text, TextType.TEXT))
            
            # Add Link node
            list_nodes.append(TextNode(vis_text, TextType.LINK, url))

            current_index = index + len(markdown)

        if current_index < len(text):
            list_nodes.append(TextNode(text[current_index:], TextType.TEXT))
    return list_nodes


def text_to_textnodes(text):
     main_node = TextNode(text, TextType.TEXT)
    
     extracted_bold = split_nodes_delimiter([main_node], "**", TextType.BOLD)
    
     extracted_italic = split_nodes_delimiter(extracted_bold, "_", TextType.ITALIC)
    
     extracted_code = split_nodes_delimiter(extracted_italic, "`", TextType.CODE)
    
     extracted_imag = split_nodes_image(extracted_code)
    
     extracted_link = split_nodes_link(extracted_imag)
    
     return extracted_link



