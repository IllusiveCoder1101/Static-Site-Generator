
from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag : str, children : list[HTMLNode], props : dict[str, str] | None = None):
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
    
            if self.tag is None:
                raise ValueError("value cannot be None.")
            if self.children is None:
                raise ValueError("Children cannot be None.")
    
            children_html = ""

            for i in self.children:
                children_html += i.to_html()

            return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
    

    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, {str(self.children)}, {self.props_to_html()})"
    

    
    
