from __future__ import absolute_import, division, print_function
import os.path
from functools import partial
from ..Settings import *
from ..Code import FoxDotCode
from .Format import *
from .tximport import *

ctrl = "Command" if SYSTEM == MAC_OS else "Ctrl"


class Menu(ModalScreen):
    """Modal screen for displaying menu options"""

    BINDINGS = [("escape", "dismiss", "Close")]

    def __init__(self, menu_items: list, title: str):
        super().__init__()
        self.menu_items = menu_items
        self.title = title

    def compose(self) -> ComposeResult:
        with Container(id="menu-modal"):
            yield Static(self.title, id="menu-title")
            yield OptionList(*self.menu_items, id="menu-options")

    def on_option_list_option_selected(self, event: OptionList.OptionSelected) -> None:
        """Handle menu option selection"""
        selected = str(event.option_prompt)
        self.dismiss(selected)


class MenuBar(Static):
    """Complete reactive menu bar with all FoxDot menu options"""

    # Track currently focused menu button
    focused_menu_index = reactive(0)
    menu_buttons = ["file-menu", "edit-menu", "view-menu", "language-menu", "tools-menu", "help-menu"]

    BINDINGS = [
        ("left", "previous_menu", "Previous Menu"),
        ("right", "next_menu", "Next Menu"),
        ("enter", "open_menu", "Open Menu"),
    ]

    def compose(self) -> ComposeResult:
        yield Horizontal(
            Button("File", id="file-menu", classes="menu-button"),
            Button("Edit", id="edit-menu", classes="menu-button"),
            Button("View", id="view-menu", classes="menu-button"),
            Button("Language", id="language-menu", classes="menu-button"),
            Button("Tools", id="tools-menu", classes="menu-button"),
            Button("Help", id="help-menu", classes="menu-button"),
            id="menu-container"
        )

    def on_mount(self) -> None:
        """Set initial focus on first menu button"""
        try:
            first_button = self.query_one("#file-menu", Button)
            first_button.focus()
        except Exception:
            pass

    def action_previous_menu(self) -> None:
        """Move focus to previous menu button"""
        self.focused_menu_index = (self.focused_menu_index - 1) % len(self.menu_buttons)
        self._focus_current_menu()

    def action_next_menu(self) -> None:
        """Move focus to next menu button"""
        self.focused_menu_index = (self.focused_menu_index + 1) % len(self.menu_buttons)
        self._focus_current_menu()

    def action_open_menu(self) -> None:
        """Open the currently focused menu"""
        current_menu_id = self.menu_buttons[self.focused_menu_index]
        try:
            button = self.query_one(f"#{current_menu_id}", Button)
            # Trigger the button press
            self.on_button_pressed(Button.Pressed(button))
        except Exception:
            pass

    def _focus_current_menu(self) -> None:
        """Set focus on the current menu button"""
        current_menu_id = self.menu_buttons[self.focused_menu_index]
        try:
            button = self.query_one(f"#{current_menu_id}", Button)
            button.focus()
        except Exception:
            pass

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle menu button clicks"""
        # Update focused index when button is clicked
        if event.button.id in self.menu_buttons:
            self.focused_menu_index = self.menu_buttons.index(event.button.id)

        if event.button.id == "file-menu":
            self.show_file_menu()
        elif event.button.id == "edit-menu":
            self.show_edit_menu()
        elif event.button.id == "view-menu":
            self.show_view_menu()
        elif event.button.id == "language-menu":
            self.show_language_menu()
        elif event.button.id == "tools-menu":
            self.show_tools_menu()
        elif event.button.id == "help-menu":
            self.show_help_menu()

    def show_file_menu(self):
        """File menu options"""
        file_options = [
            f"New Document ({ctrl}+N)",
            f"Open ({ctrl}+O)",
            f"Save ({ctrl}+S)",
            "Save As...",
            "---",
            "Quit"
        ]

        def handle_file_action(selection):
            if selection is None or selection == "---":
                return

            if "New Document" in selection:
                self.app.notify("New Document - not yet implemented")
            elif "Open" in selection:
                self.app.notify("Open - not yet implemented")
            elif "Save As" in selection:
                self.app.notify("Save As - not yet implemented")
            elif "Save" in selection:
                self.app.notify("Save - not yet implemented")
            elif "Quit" in selection:
                self.app.exit()

        self.app.push_screen(Menu(file_options, "File"), handle_file_action)

    def show_edit_menu(self):
        """Edit menu options"""
        edit_options = [
            f"Undo ({ctrl}+Z)",
            f"Redo ({ctrl}+Y)",
            "---",
            f"Cut ({ctrl}+X)",
            f"Copy ({ctrl}+C)",
            f"Paste ({ctrl}+V)",
            f"Select All ({ctrl}+A)",
            "---",
            f"Increase Font Size ({ctrl}+=)",
            f"Decrease Font Size ({ctrl}+-)",
            "---",
            f"Preferences ({ctrl}+P)"
        ]

        def handle_edit_action(selection):
            if selection is None or selection == "---":
                return
            self.app.notify(f"Edit: {selection} - not yet implemented")

        self.app.push_screen(Menu(edit_options, "Edit"), handle_edit_action)

    def show_view_menu(self):
        """View menu options"""
        view_options = [
            f"Toggle Menu ({ctrl}+M)",
            f"Toggle Line Numbers ({ctrl}+0)",
            f"Toggle Treeview ({ctrl}+U)",
            f"Toggle Searchbar ({ctrl}+F)",
            "Toggle Midibar",
            "---",
            "Toggle Console",
            "Clear Console",
            "Export Console Log"
        ]

        def handle_view_action(selection):
            if selection is None or selection == "---":
                return
            self.app.notify(f"View: {selection} - not yet implemented")

        self.app.push_screen(Menu(view_options, "View"), handle_view_action)

    def show_language_menu(self):
        """Language menu options"""
        lang_options = [
            f"Evaluate Block ({ctrl}+Return)",
            "Evaluate Line (Alt+Return)",
            f"Clear Scheduling Clock ({ctrl}+.)",
            "---",
            "Listen for connections"
        ]

        def handle_lang_action(selection):
            if selection is None or selection == "---":
                return
            self.app.notify(f"Language: {selection} - not yet implemented")

        self.app.push_screen(Menu(lang_options, "Language"), handle_lang_action)

    def show_tools_menu(self):
        """Tools menu options"""
        tools_options = [
            "Samples Chart App",
            "Midi Mapper"
        ]

        def handle_tools_action(selection):
            if selection is None:
                return
            self.app.notify(f"Tools: {selection} - not yet implemented")

        self.app.push_screen(Menu(tools_options, "Tools"), handle_tools_action)

    def show_help_menu(self):
        """Help menu options"""
        help_options = [
            f"Display help message ({ctrl}+H)",
            "Visit Renardo Homepage",
            "Documentation",
            "---",
            "Open Samples Folder"
        ]

        def handle_help_action(selection):
            if selection is None or selection == "---":
                return
            self.app.notify(f"Help: {selection} - not yet implemented")

        self.app.push_screen(Menu(help_options, "Help"), handle_help_action)
