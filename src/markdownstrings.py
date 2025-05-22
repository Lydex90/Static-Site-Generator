from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    list_nodes = []

    for node in old_nodes:
        if node.text_type != text_type.TEXT:
            list_nodes.extend([node])
            continue
        elif delimiter not in node.text:
            raise ValueError("delimiter not found")
        
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