import unittest
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes  # adjust to the module where the function lives


class TestTextToTextNodes(unittest.TestCase):

    def test_full_example(self):
        text = (
            "This is **text** with an _italic_ word and a `code block` "
            "and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) "
            "and a [link](https://boot.dev)"
        )
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(text_to_textnodes(text), expected)
    
    def test_returns_list_of_textnodes(self):
        result = text_to_textnodes("Some **bold** text")
        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(n, TextNode) for n in result))

    def test_plain_text(self):
        result = text_to_textnodes("Just some plain text")
        self.assertEqual(result, [TextNode("Just some plain text", TextType.TEXT)])

    def test_bold_only(self):
        result = text_to_textnodes("This is **bold** text")
        self.assertEqual(result, [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ])

    def test_italic_only(self):
        result = text_to_textnodes("This is _italic_ text")
        self.assertEqual(result, [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ])

    def test_code_only(self):
        result = text_to_textnodes("Run `print('hi')` now")
        self.assertEqual(result, [
            TextNode("Run ", TextType.TEXT),
            TextNode("print('hi')", TextType.CODE),
            TextNode(" now", TextType.TEXT),
        ])

    def test_image_only(self):
        result = text_to_textnodes("Look at ![cat](https://example.com/cat.png) here")
        self.assertEqual(result, [
            TextNode("Look at ", TextType.TEXT),
            TextNode("cat", TextType.IMAGE, "https://example.com/cat.png"),
            TextNode(" here", TextType.TEXT),
        ])

    def test_link_only(self):
        result = text_to_textnodes("Visit [boot.dev](https://boot.dev) today")
        self.assertEqual(result, [
            TextNode("Visit ", TextType.TEXT),
            TextNode("boot.dev", TextType.LINK, "https://boot.dev"),
            TextNode(" today", TextType.TEXT),
        ])

    def test_image_is_not_treated_as_link(self):
        result = text_to_textnodes("An ![img](https://example.com/a.png) and more")
        self.assertEqual(
            [n.text_type for n in result],
            [TextType.TEXT, TextType.IMAGE, TextType.TEXT],
        )

    def test_multiple_bold_sections(self):
        result = text_to_textnodes("**one** and **two** and **three**!")
        bold_nodes = [n for n in result if n.text_type == TextType.BOLD]
        self.assertEqual(
            bold_nodes,
            [
                TextNode("one", TextType.BOLD),
                TextNode("two", TextType.BOLD),
                TextNode("three", TextType.BOLD),
            ],
        )

    def test_multiple_links(self):
        result = text_to_textnodes(
            "Go to [one](https://one.com) or [two](https://two.com) now"
        )
        self.assertEqual(result, [
            TextNode("Go to ", TextType.TEXT),
            TextNode("one", TextType.LINK, "https://one.com"),
            TextNode(" or ", TextType.TEXT),
            TextNode("two", TextType.LINK, "https://two.com"),
            TextNode(" now", TextType.TEXT),
        ])

    def test_multiple_images(self):
        result = text_to_textnodes(
            "First ![a](https://a.com/a.png) then ![b](https://b.com/b.png) end"
        )
        self.assertEqual(result, [
            TextNode("First ", TextType.TEXT),
            TextNode("a", TextType.IMAGE, "https://a.com/a.png"),
            TextNode(" then ", TextType.TEXT),
            TextNode("b", TextType.IMAGE, "https://b.com/b.png"),
            TextNode(" end", TextType.TEXT),
        ])

    def test_mixed_types_preserve_order(self):
        text = "Start `code` then **bold** then _italic_ end"
        result = text_to_textnodes(text)
        self.assertEqual(result, [
            TextNode("Start ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" then ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" then ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" end", TextType.TEXT),
        ])

    def test_link_and_image_together(self):
        text = "See ![pic](https://example.com/p.png) and [site](https://example.com) ok"
        result = text_to_textnodes(text)
        self.assertEqual(result, [
            TextNode("See ", TextType.TEXT),
            TextNode("pic", TextType.IMAGE, "https://example.com/p.png"),
            TextNode(" and ", TextType.TEXT),
            TextNode("site", TextType.LINK, "https://example.com"),
            TextNode(" ok", TextType.TEXT),
        ])

    def test_formatted_text_next_to_link(self):
        text = "A **bold** word and a [link](https://boot.dev) after"
        result = text_to_textnodes(text)
        self.assertEqual(result, [
            TextNode("A ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
            TextNode(" after", TextType.TEXT),
        ])


if __name__ == "__main__":
    unittest.main()