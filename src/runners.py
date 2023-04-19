
from textual.app import ComposeResult
from textual.widgets import Static
from textual.containers import Grid


class RunnerStatBox(Static):
    """Box that contains a runner statistic"""

    stat: int = 0

    def __init__(self, stat_title: str):
        self.stat_title = stat_title
        super().__init__()

    def compose(self):
        yield Static(f"{self.stat_title}")
        yield Static(f"{self.stat}")

class Runners(Grid):
    """Container for runner data"""

    def compose(self) -> ComposeResult:
        yield RunnerStatBox("Idle")
        yield RunnerStatBox("Active")
        yield RunnerStatBox("Offline")
