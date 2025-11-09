from __future__ import absolute_import, division, print_function
from .tximport import *
from ..Settings import LINE_NUMBER_MARKER_OFFSET
from ..Code import execute
from rich.text import Text


class LineNumbers(Static):
    """Line numbers widget that syncs with text editor"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.line_count = 1
        self.current_line = 1

    def compose(self) -> ComposeResult:
        yield Static("  1", id="line-numbers-content")

    def update_line_numbers(self, count: int, current: int = 1):
        """Update line numbers based on text content"""
        self.line_count = count
        self.current_line = current

        lines = []
        for i in range(1, count + 1):
            if i == current:
                lines.append(f"[bold cyan]{i:>3}[/bold cyan]")
            else:
                lines.append(f"{i:>3}")

        content = "\n".join(lines)

        try:
            widget = self.query_one("#line-numbers-content", Static)
            # Use Rich Text with no_wrap to prevent wrapping
            from rich.text import Text
            text_obj = Text(content, no_wrap=True, overflow="ignore")
            widget.update(text_obj)
        except Exception as e:
            self.log(f"Failed to update line numbers: {e}")

        # Make sure the widget exists before updating
        try:
            widget = self.query_one("#line-numbers-content", Static)
            widget.update(content)
        except Exception as e:
            self.log(f"Failed to update line numbers: {e}")


# class LineNumbers(Tk.Canvas):
#     def __init__(self, master, *args, **kwargs):
#         Tk.Canvas.__init__(self, *args, **kwargs)
#         self.root = master
#         self.textwidget = master.text
#
#     def redraw(self, *args):
#         '''redraw line numbers'''
#         # Update player line numbers
#         # execute.update_line_numbers(self.textwidget)
#         # Clear
#         self.delete("all")
#         # Draw a line
#         w = self.winfo_width() - 1
#         h = self.winfo_height()
#         self.create_line(w, 0, w, h, fill="gray")
#         i = self.textwidget.index("@0,0")
#
#         while True:
#             dline = self.textwidget.dlineinfo(i)
#             if dline is None:
#                 break
#             y = dline[1]
#             h = dline[3]
#             linenum = int(str(i).split(".")[0])
#             curr_row = int(self.textwidget.index(Tk.INSERT).split(".")[0])
#
#             if linenum == curr_row:
#                 x1, y1 = 0, y + LINE_NUMBER_MARKER_OFFSET
#                 x2, y2 = w - 2, y + h
#                 self.create_rectangle(x1,
#                                       y1,
#                                       x2,
#                                       y2,
#                                       fill="gray30",
#                                       outline="gray30")
#
#             self.create_text(w - 4, y, anchor="ne",
#                              justify=Tk.RIGHT,
#                              text=linenum,
#                              font=self.root.codefont,
#                              fill="#c9c9c9")
#
#             i = self.textwidget.index("{}+1line".format(i))
#
#         # Update console beat counter here too
#         self.root.console.counter.redraw()
#         self.after(30, self.redraw)
#
#     def hide(self):
#         """ Removes treeview from interface """
#         self.grid_remove()
#         return
#
#     def show(self):
#         self.grid()
#         return
