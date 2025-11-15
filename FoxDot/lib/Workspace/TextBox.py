from __future__ import absolute_import, division, print_function
from .Format import *
from .tximport import *
from textual.message import Message

try:
    import Queue
except ImportError:
    import queue as Queue


class FoxDotTextEditor(TextEditor):
    """Custom TextEditor with FoxDot-specific key bindings using message pattern"""

    BINDINGS = [
        ("ctrl+enter", "exec_block", "Execute Block"),
        ("alt+enter", "exec_line", "Execute Line"),
        ("ctrl+period", "kill_all", "Kill All"),
        ("ctrl+m", "toggle_menu", "Toggle Menu"),
        ("ctrl+k", "toggle_console", "Toggle Console"),
        ("ctrl+0", "toggle_linenumbers", "Toggle Line Numbers"),
        ("ctrl+u", "toggle_treeview", "Toggle Tree View"),
        ("ctrl+f", "toggle_searchbar", "Toggle Search Bar"),
        ("f1", "toggle_midibar", "Toggle MIDI Bar"),
        ("ctrl+s", "save_file", "Save File"),
        ("ctrl+o", "open_file", "Open File"),
        ("ctrl+n", "new_file", "New File"),
        ("ctrl+a", "select_all", "Select All"),
    ]

    def on_key(self, event) -> None:
        """Debug: Log all key events"""
        # Log the event details
        key_info = f"Key: {event.key}"
        if hasattr(event, 'character') and event.character:
            key_info += f", Char: {repr(event.character)}"
        if hasattr(event, 'modifiers'):
            key_info += f", Mods: {event.modifiers}"

        self.app.notify(key_info)

    # Message classes for each action
    class ExecBlock(Message, bubble=True):
        """Message posted when executing a code block"""
        pass

    class ExecLine(Message, bubble=True):
        """Message posted when executing a line"""
        pass

    class KillAll(Message, bubble=True):
        """Message posted when killing all sounds"""
        pass

    class ToggleMenu(Message, bubble=True):
        """Message posted when toggling menu"""
        pass

    class ToggleConsole(Message, bubble=True):
        """Message posted when toggling console"""
        pass

    class ToggleLineNumbers(Message, bubble=True):
        """Message posted when toggling line numbers"""
        pass

    class ToggleTreeView(Message, bubble=True):
        """Message posted when toggling tree view"""
        pass

    class ToggleSearchBar(Message, bubble=True):
        """Message posted when toggling search bar"""
        pass

    class ToggleMidiBar(Message, bubble=True):
        """Message posted when toggling MIDI bar"""
        pass

    class SaveFile(Message, bubble=True):
        """Message posted when saving file"""
        pass

    class OpenFile(Message, bubble=True):
        """Message posted when opening file"""
        pass

    class NewFile(Message, bubble=True):
        """Message posted when creating new file"""
        pass

    class SelectAll(Message, bubble=True):
        """Message posted when selecting all text"""
        pass

    # Action methods that post messages
    async def action_exec_block(self) -> None:
        self.post_message(self.ExecBlock())

    async def action_exec_line(self) -> None:
        self.post_message(self.ExecLine())

    async def action_kill_all(self) -> None:
        self.post_message(self.KillAll())

    async def action_toggle_menu(self) -> None:
        self.post_message(self.ToggleMenu())

    async def action_toggle_console(self) -> None:
        self.post_message(self.ToggleConsole())

    async def action_toggle_linenumbers(self) -> None:
        self.post_message(self.ToggleLineNumbers())

    async def action_toggle_treeview(self) -> None:
        self.post_message(self.ToggleTreeView())

    async def action_toggle_searchbar(self) -> None:
        self.post_message(self.ToggleSearchBar())

    async def action_toggle_midibar(self) -> None:
        self.post_message(self.ToggleMidiBar())

    async def action_save_file(self) -> None:
        self.post_message(self.SaveFile())

    async def action_open_file(self) -> None:
        self.post_message(self.OpenFile())

    async def action_new_file(self) -> None:
        self.post_message(self.NewFile())

    async def action_select_all(self) -> None:
        self.post_message(self.SelectAll())


class ThreadedText(ScrollView):
    """Wrapper for FoxDotTextEditor"""

    def __init__(self, text: str = "", **kwargs):
        kwargs.pop('text', None)
        super().__init__(**kwargs)
        self.text_content = text

    def compose(self) -> ComposeResult:
        with Vertical():
            yield FoxDotTextEditor(
                text=self.text_content,
                id="text-area-content"
            )

    @property
    def text(self):
        return self.query_one("#text-area-content").text

    @text.setter
    def text(self, value: str):
        self.query_one("#text-area-content").text = value

    def insert(self, text: str):
        self.query_one("#text-area-content").insert(text)

    def select_all(self):
        self.query_one("#text-area-content").select_all()

    def cut(self):
        text_area = self.query_one("#text-area-content")
        if text_area.selection:
            import pyperclip
            pyperclip.copy(text_area.selected_text)
            text_area.delete(text_area.selection.start, text_area.selection.end)

    def copy(self):
        text_area = self.query_one("#text-area-content")
        if text_area.selection:
            import pyperclip
            pyperclip.copy(text_area.selected_text)

    def paste(self):
        text_area = self.query_one("#text-area-content")
        import pyperclip
        text_area.insert(pyperclip.paste())

    def clear(self):
        self.query_one("#text-area-content").clear()
