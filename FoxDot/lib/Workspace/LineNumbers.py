from __future__ import absolute_import, division, print_function
from .tximport import *
from ..Settings import LINE_NUMBER_MARKER_OFFSET
from ..Code import execute


class LineNumbers(Static):
    """Line numbers widget that syncs with text editor"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.line_count = 1
        self.current_line = 1

    def compose(self) -> ComposeResult:
        yield Static("1", id="line-numbers-content")

    def update_line_numbers(self, count: int, current: int = 1):
        """Update line numbers based on text content"""
        self.line_count = count
        # Ensure current line doesn't exceed line count (fix for bounds error)
        self.current_line = min(current, count)

        lines = []
        for i in range(1, count + 1):
            if i == self.current_line:
                # Highlight current line
                lines.append(f"[bold cyan]{i:>3}[/bold cyan]")
            else:
                lines.append(f"{i:>3}")

        content = "\n".join(lines)
        self.query_one("#line-numbers-content").update(content)

    def sync_with_editor(self, editor_widget):
        """Synchronize with text editor cursor position"""
        # Get cursor position from editor
        # Update highlighting accordingly
        pass
