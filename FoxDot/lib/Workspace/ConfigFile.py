from __future__ import absolute_import, division, print_function

from .tximport import *
from ..Settings import FOXDOT_ICON, FOXDOT_ICON_GIF
import os.path


class Config(ModalScreen):
    """Config file editor as a modal screen"""

    CSS = """
    Config {
        align: center middle;
    }

    #config-container {
        width: 80;
        height: 40;
        border: solid $primary;
        background: $surface;
    }

    #config-title {
        dock: top;
        height: 3;
        content-align: center middle;
        background: $primary;
    }

    #button-row {
        dock: bottom;
        height: 3;
        padding: 1;
    }

    #config-editor {
        height: 1fr;
    }
    """

    def __init__(self, path):
        super().__init__()
        self.filepath = os.path.realpath(path)
        self.unsaved = True

        with open(self.filepath) as f:
            self.text = f.read().rstrip()

    def compose(self) -> ComposeResult:
        with Container(id="config-container"):
            yield Static("conf.txt", id="config-title")
            yield TextArea(
                text=self.text,
                language="json",
                id="config-editor"
            )
            with Horizontal(id="button-row"):
                yield Button("Cancel", id="cancel-btn")
                yield Button("Save Changes", id="save-btn", variant="primary")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "save-btn":
            self.save_changes()
        elif event.button.id == "cancel-btn":
            self.save_and_close()

    def save_and_close(self):
        """Ask user if they want to save changes"""
        current_text = self.query_one("#config-editor").text

        if current_text != self.text:
            # In Textual, we'd use a custom confirmation dialog
            # For now, just close
            self.app.pop_screen()
        else:
            self.app.pop_screen()

    def get_text(self):
        return self.query_one("#config-editor").text

    def save_changes(self):
        """Save changes to config file"""
        text = self.get_text()

        with open(self.filepath, "w") as f:
            f.write(text)

        self.app.notify("A restart of FoxDot is required for the changes to take effect", severity="warning")
        self.app.pop_screen()
