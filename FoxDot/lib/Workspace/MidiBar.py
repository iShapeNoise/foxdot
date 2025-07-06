from .tximport import *
from ..Utils import midi_cmd
from ..Settings import *
from .Format import *


class MidiBar(ScrollView):
    """MIDI parameter display bar with scrolling"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.midi_slots = 16
        self.data_list = [""] * self.midi_slots
        self.is_running = True
        self.setup_midi_monitoring()

    def compose(self) -> ComposeResult:
        with Vertical():
            # Parameter names row
            with Horizontal(id="midi-names-row"):
                for i in range(self.midi_slots):
                    yield Static(f"CH{i+1:02d}", classes="midi-slot", id=f"midi-name-{i}")

            # Parameter values row
            with Horizontal(id="midi-values-row"):
                for i in range(self.midi_slots):
                    yield Static("---", classes="midi-value", id=f"midi-value-{i}")

    def setup_midi_monitoring(self):
        """Start MIDI monitoring thread"""
        self.midi_thread = threading.Thread(target=self.midi_update_loop, daemon=True)
        self.midi_thread.start()

    def midi_update_loop(self):
        """Continuously update MIDI parameters"""
        while self.is_running:
            # Based on current MidiBar.py implementation
            # Get MIDI messages and update display
            time.sleep(0.05)

    def update_midi_slot(self, slot: int, name: str, value: str, active: bool = False):
        """Update a specific MIDI slot"""
        name_widget = self.query_one(f"#midi-name-{slot}")
        value_widget = self.query_one(f"#midi-value-{slot}")

        name_widget.update(name)
        value_widget.update(value)

        # Color coding for active parameters
        if active:
            name_widget.add_class


# class MidiBar:
#     def __init__(self, parent):
#         self.root = parent.root
#         self.parent = parent
#         self.f_height = 100
#         self.fontH1 = tkFont.Font(size=14)
#         self.fontH2 = tkFont.Font(size=12)
#         self.midi_cmd = midi_cmd()
#         self.midi_msg = self.midi_cmd.get_msg()
#         self.mb_frame = tb.Frame(
#             self.root, height=self.f_height)
#         self.mb_frame.grid(row=0, column=2, columnspan=4, sticky='sew')
#         self.hide()
#         self.slots = 16
#         self.var_list = []
#         self.lbl_list = []
#         self.data_list = []
#         self.in_list = False
#         self.txt_active = colour_map['strings']
#         self.txt_inactive = colour_map['key_types']
#         self.bg = colour_map['background']
#         self.bg_active = colour_map['numbers']
#         # Create label list, strings var list, and data buffer list
#         for i in range(self.slots):
#             self.data_list.append("")
#             self.var_list.append([tb.StringVar(), tb.StringVar()])
#             self.lbl_list.append(tb.Label(self.mb_frame,
#                                           textvariable=self.var_list[i][0],
#                                           font=self.fontH2,
#                                           foreground=self.txt_inactive,
#                                           background=self.bg_active,
#                                           width=1))
#             self.var_list.append([tb.StringVar(), tb.StringVar()])
#             self.lbl_list.append(tb.Label(self.mb_frame,
#                                           textvariable=self.var_list[i][1],
#                                           font=self.fontH2,
#                                           foreground=self.txt_inactive,
#                                           background=self.bg,
#                                           width=16))
#             num = i + 1
#         for i in range(self.slots*2):
#             if i < self.slots:
#                 self.lbl_list[i].grid(row=0, column=i, sticky="ew")
#             else:
#                 num = i - self.slots
#                 self.lbl_list[i].grid(row=1, column=num, sticky="ew")
#         # Start running update thread
#         self.setText_thread = Thread(target=self.set_text)
#         self.is_running = True
#         self.setText_thread.setDaemon(True)
#         self.setText_thread.start()
#
#     def set_text(self):
#         cur_attr = ""
#         while self.is_running:
#             msg = self.midi_cmd.get_msg()
#             attr = msg[1].split("=")[0]
#             self.in_list = False
#             if attr != "":
#                 for item in self.data_list:
#                     if item != "":
#                         new_attr = item.split("=")[0]
#                         if new_attr == attr:
#                             idx = self.data_list.index(item)
#                             self.var_list[idx][1].set(msg[1])
#                             self.data_list[idx] = msg[1]
#                             if msg[2] != "":
#                                 self.var_list[idx][0].set(msg[2])
#                             self.lbl_list[idx*2+1].config(
#                                 foreground=self.txt_active
#                             )
#                             self.lbl_list[idx*2].config(
#                                 foreground=self.txt_active
#                             )
#                             self.in_list = True
#                 if cur_attr != attr:
#                     if self.in_list is False:
#                         for i in reversed(range(self.slots)):
#                             if i > 0:
#                                 num = i - 1
#                                 new_entry = self.data_list[num]
#                                 del_entry = self.data_list[i]
#                                 self.data_list.remove(del_entry)
#                                 self.data_list.insert(i, new_entry)
#                                 swap1 = self.var_list[i-1][0].get()
#                                 self.var_list[i][0].set(swap1)
#                                 swap2 = self.var_list[i-1][1].get()
#                                 self.var_list[i][1].set(swap2)
#                             else:
#                                 self.data_list[0] = msg[1]
#                                 self.var_list[0][0].set(msg[2])
#                                 self.var_list[0][1].set(msg[1])
#             if attr != cur_attr:
#                 for i in range(self.slots*2):
#                     self.lbl_list[i].config(
#                         foreground=self.txt_inactive
#                     )
#             cur_attr = msg[1].split("=")[0]
#             time.sleep(0.05)
#
#     def close(self):
#         self.midi_cmd.is_running = False
#         self.is_running = False
#         self.setText_thread.join()
#
#     def hide(self):
#         """ Removes searchbar from interface """
#         self.mb_frame.grid_remove()
#         return
#
#     def show(self):
#         self.mb_frame.grid()
#         return
