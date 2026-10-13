import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "hello world", None, None)
        node2 = HTMLNode("p", "hello world", None, None)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = HTMLNode("p", "hello world", None, None)
        node2 = HTMLNode("h1", "hello world", None, None)
        self.assertNotEqual(node, node2)

    def missing_value(self):
        node = HTMLNode("p", "", None, None)
        node2 = HTMLNode("p", "", None, None)
        self.asserttEqual(node, node2)



if __name__ == "__main__":
    unittest.main()