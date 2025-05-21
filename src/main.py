from textnode import *

def main():
    print("hello world")
    test_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(test_node)


main()
