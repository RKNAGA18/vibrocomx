from typing import Dict, Any, List, Optional

class BaseComponent:
    """
    Base class for all Antigravity components.
    Simulates a component-based architecture.
    """
    def __init__(self, props: Optional[Dict[str, Any]] = None, children: Optional[List['BaseComponent']] = None):
        self.props = props or {}
        self.children = children or []
        self.classes = self.props.get('class', '')

    def render(self) -> str:
        """
        Renders the component to an HTML string.
        Should be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must implement render()")

    def render_children(self) -> str:
        """Helper to render all child components."""
        return "".join([child.render() for child in self.children])

class Text(BaseComponent):
    """Simple text component."""
    def __init__(self, content: str, tag: str = "span", **kwargs):
        super().__init__(props=kwargs)
        self.content = content
        self.tag = tag

    def render(self) -> str:
        return f'<{self.tag} class="{self.classes}">{self.content}</{self.tag}>'

class Container(BaseComponent):
    """Generic container component (div, section, etc)."""
    def __init__(self, tag: str = "div", **kwargs):
        super().__init__(props=kwargs, children=kwargs.get('children'))
        self.tag = tag

    def render(self) -> str:
        return f'<{self.tag} class="{self.classes}">{self.render_children()}</{self.tag}>'
