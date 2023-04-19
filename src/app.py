
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer

from runners import Runners

class GHABoardApp(App):
    """A Textual app to manage stopwatches."""

    CSS_PATH = ["runner.css"]
    BINDINGS=[
        ('ctrl+c', 'quit', 'Quit')
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Runners()
        yield Footer()
