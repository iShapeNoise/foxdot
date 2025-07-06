from .tximport import *
#from .tkimport import Text, SEL, END, SEL_FIRST, SEL_LAST, INSERT
from .Format import *


class SearchBar(Static):
    """Search and replace functionality with scrolling support"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.search_list = []
        self.search_term = ""
        self.current_index = 0

    def compose(self) -> ComposeResult:
        with Vertical():
            with Horizontal(id="search-controls"):
                yield Label("Search:", classes="search-label")
                yield Input(
                    placeholder="Enter search term",
                    id="search-input",
                    classes="search-input"
                )
                yield Button("Find", id="find-button", classes="search-button")
                yield Button("Replace", id="replace-button", classes="search-button")
                yield Button("Replace All", id="replace-all-button", classes="search-button")

            with Horizontal(id="replace-controls"):
                yield Label("Replace:", classes="search-label")
                yield Input(
                    placeholder="Replace with",
                    id="replace-input",
                    classes="search-input"
                )
                yield Label("ENTER to search << >> 2 x TAB to get back!", classes="search-hint")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle search button clicks"""
        if event.button.id == "find-button":
            self.perform_search()
        elif event.button.id == "replace-button":
            self.perform_replace()
        elif event.button.id == "replace-all-button":
            self.perform_replace_all()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        """Handle Enter key in search input"""
        if event.input.id == "search-input":
            self.perform_search()

    def perform_search(self):
        """Perform search operation - placeholder"""
        search_term = self.query_one("#search-input").value
        if search_term:
            self.search_term = search_term
            # Get reference to main text editor
            try:
                text_editor = self.app.query_one("#text-editor")
                # Implement search logic here
                # This would integrate with the text editor's search functionality
                self.highlight_search_results(text_editor, search_term)
            except Exception:
                pass  # Text editor not found

    def perform_replace(self):
        """Perform single replace operation - placeholder"""
        search_term = self.query_one("#search-input").value
        replace_term = self.query_one("#replace-input").value

        if search_term and replace_term:
            # Implement replace logic here
            pass

    def perform_replace_all(self):
        """Perform replace all operation - placeholder"""
        search_term = self.query_one("#search-input").value
        replace_term = self.query_one("#replace-input").value

        if search_term and replace_term:
            # Implement replace all logic here
            pass

    def highlight_search_results(self, text_editor, search_term):
        """Highlight search results in the text editor"""
        # Based on the current SearchBar implementation logic
        # This would need to integrate with Textual's TextArea highlighting
        pass

    def reset_search(self):
        """Reset search state"""
        self.search_list.clear()
        self.search_term = ""
        self.current_index = 0

        # Clear input fields
        self.query_one("#search-input").value = ""
        self.query_one("#replace-input").value = ""

    def focus_search_input(self):
        """Focus the search input field"""
        self.query_one("#search-input").focus()


# class SearchBar:
#
#     def __init__(self, parent):
#         self.root = parent.root
#         self.parent = parent
#         self.f_height = 50
#         self.sb_frame = tb.Frame(
#             self.root, height=self.f_height)
#         self.sb_frame.grid(row=1, column=2, sticky='ew')
#         self.hide()
#         self.search_list = list()
#         self.search = ""
#         self.idx = ""
#         self.sb_label = tb.Label(
#             self.sb_frame, text="Enter search")
#         self.sb_label.grid(row=0, column=0, padx=10)
#         self.search_entry = tb.Entry(
#             self.sb_frame, width=40, justify="left")
#         self.search_entry.grid(row=0, column=1, pady=5, padx=10)
#         self.sb_label2 = tb.Label(
#             self.sb_frame, text="ENTER to search << >> 2 x TAB to get back!")
#         self.sb_label2.grid(row=0, column=2, pady=5, padx=10)
#         # self.search_btn = tb.Button(
#         #     self.sb_frame, text="Search", command=self.search_task)
#         # self.search_btn.grid(row=0, column=2, padx=10, pady=5, sticky="e")
#         self.root.bind('<Return>', self.search_task)
#
#     def reset_list(self):
#         if self.search != self.search_entry.get():
#             self.search_list.clear()
#             self.parent.text.tag_remove(SEL, "1.0", "end-1c")
#
#     def search_task(self, event):
#         self.reset_list()
#         # self.parent.text.focus_set()
#         self.search = self.search_entry.get()
#
#         if self.search:
#             if self.search_list == []:
#                 self.idx = "1.0"
#             else:
#                 self.idx = self.search_list[-1]
#             self.idx = self.parent.text.search(self.search,
#                                                self.idx,
#                                                nocase=1,
#                                                stopindex=END)
#             self.lastidx = '%s+%dc' % (self.idx, len(self.search))
#             try:
#                 self.parent.text.tag_remove(SEL, "1.0", self.lastidx)
#             except Exception:
#                 pass
#             try:
#                 self.parent.text.tag_add(SEL, self.idx, self.lastidx)
#                 self.counter_list = []
#                 self.counter_list = str(self.idx).split('.')
#                 self.parent.text.mark_set("insert", "%d.%d" % (float(int(self.counter_list[0])), float(int(self.counter_list[1]))))
#                 self.parent.text.see(float(int(self.counter_list[0])))
#                 self.search_list.append(self.lastidx)
#             except Exception:
#                 tkMessageBox.showinfo("Search complete", "No further matches")
#                 self.search_list.clear()
#                 self.parent.text.tag_remove(SEL, "1.0", "end-1c")
#
#     def hide(self):
#         """ Removes searchbar from interface """
#         self.sb_frame.grid_remove()
#         return
#
#     def show(self):
#         self.sb_frame.grid()
#         self.search_entry.focus()
#         return
