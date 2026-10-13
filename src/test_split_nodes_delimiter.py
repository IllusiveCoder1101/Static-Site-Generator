import unittest
from textnode import TextType, TextNode
from split_nodes_delimiter import split_nodes_delimiter  # adjust to the module where the function lives


class TestSplitNodes(unittest.TestCase):

    def test_split_bold(self):
        nodes = [TextNode("This is **bold** text", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(result, [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ])

    def test_split_italic(self):
        nodes = [TextNode("This is _italic_ text", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
        self.assertEqual(result, [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ])

    def test_split_code(self):
        nodes = [TextNode("Run `print('hi')` now", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(result, [
            TextNode("Run ", TextType.TEXT),
            TextNode("print('hi')", TextType.CODE),
            TextNode(" now", TextType.TEXT),
        ])

    def test_returns_three_nodes_per_input(self):
        nodes = [TextNode("a **b** c", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(n, TextNode) for n in result))

    def test_node_types_are_correct(self):
        nodes = [TextNode("a **b** c", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(
            [n.text_type for n in result],
            [TextType.TEXT, TextType.BOLD, TextType.TEXT],
        )

    def test_empty_input_list(self):
        self.assertEqual(split_nodes_delimiter([], "**", TextType.BOLD), [])

    def test_delimiter_at_start(self):
        nodes = [TextNode("**bold** text", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(result, [
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ])

    def test_delimiter_at_end(self):
        nodes = [TextNode("text **bold**", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        print(result)
        self.assertEqual(result, [
            TextNode("text ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
        ])

    def test_entire_text_is_delimited(self):
        nodes = [TextNode("**bold**", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(result, [
            TextNode("bold", TextType.BOLD),
        ])


if __name__ == "__main__":
    unittest.main()