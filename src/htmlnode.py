

class HTMLNode:
    def __init__(self, tag : str | None = None, value : str | None = None, children = None, props : dict[str, str] | None = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    def props_to_html(self) -> str:
        res = ""

        if self.props is None or len(list(self.props.keys())) == 0:
            return ""
        
        for i in self.props:
            res += f' {i}={self.props[i]}'
        return res

    def __eq__(self, other) -> bool:
    
            if self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props:
                return True
            return False
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {str(self.children)}, {self.props_to_html()})"
    

    
    
