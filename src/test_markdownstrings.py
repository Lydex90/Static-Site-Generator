import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from markdownstrings import split_nodes_delimiter

class TestMarkdownStrings(unittest.TestCase):
    def test_bold(self):
        node = TextNode("That's a **bold** move Cotton!", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("That's a ", TextType.TEXT), 
            TextNode("bold", TextType.BOLD), 
            TextNode(" move Cotton!", TextType.TEXT)
        ])
    
    def test_italic(self):
        node = TextNode("Oh so he's _that_ kind of man", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode("Oh so he's ", TextType.TEXT), 
            TextNode("that", TextType.ITALIC), 
            TextNode(" kind of man", TextType.TEXT)
        ])
    

    def test_code(self):
        node = TextNode("I only know `print('Hello World!')`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("I only know ", TextType.TEXT), 
            TextNode("print('Hello World!')", TextType.CODE)
        ])
    
    def test_nottext(self):
        node = TextNode("I WANT PICTURES OF SPIDERMAN", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("I WANT PICTURES OF SPIDERMAN", TextType.BOLD)])
    
    def test_nodelimiter(self):
        node = TextNode("I only know `print('Hello World!')`", TextType.TEXT)
        with self.assertRaises(ValueError) as context:
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_multiple_bolds(self):
        node = TextNode("He's **FAT**, **BALD**, **UGLY**, and: **STUPID!**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("He's ", TextType.TEXT), 
            TextNode("FAT", TextType.BOLD), 
            TextNode(", ", TextType.TEXT),
            TextNode("BALD", TextType.BOLD),
            TextNode(", ", TextType.TEXT),
            TextNode("UGLY", TextType.BOLD),
            TextNode(", and: ", TextType.TEXT),
            TextNode("STUPID!", TextType.BOLD)
        ])

    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()