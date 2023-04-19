
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer


class GHABoardApp(App):
    """A Textual app to manage stopwatches."""

    BINDINGS=[
        ('ctrl+c', 'quit', 'Quit')
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
