from __future__ import absolute_import, division, print_function

from .tximport import *
from ..Settings import *
from .Format import *
import os.path


class Preferences(ModalScreen):
    """Preferences dialog as a modal screen"""

    CSS = """
    Preferences {
        align: center middle;
    }

    #preferences-container {
        width: 80;
        height: 40;
        border: solid $primary;
        background: $surface;
    }

    #button-row {
        dock: bottom;
        height: 3;
        padding: 1;
    }

    TabbedContent {
        height: 1fr;
    }
    """

    def __init__(self):
        super().__init__()
        self.w = 850
        self.h = 600
        self.themes = ()
        self.theme_colors = {}

        # Load theme colors from JSON
        with open(FOXDOT_EDITOR_THEMES, 'r') as openfile:
            json_object = json.load(openfile)
            theme_list = json_object["themes"]
            for item in theme_list:
                theme = list(item.keys())[0]
                self.themes = self.themes + (theme,)
                if theme == COLOR_THEME:
                    self.theme_colors['primary'] = item[COLOR_THEME]["colors"]['primary']
                    self.theme_colors['secondary'] = item[COLOR_THEME]["colors"]['secondary']
                    self.theme_colors['success'] = item[COLOR_THEME]["colors"]['success']
                    self.theme_colors['info'] = item[COLOR_THEME]["colors"]['info']
                    self.theme_colors['warning'] = item[COLOR_THEME]["colors"]['warning']
                    self.theme_colors['danger'] = item[COLOR_THEME]["colors"]['danger']
                    self.theme_colors['light'] = item[COLOR_THEME]["colors"]['light']
                    self.theme_colors['dark'] = item[COLOR_THEME]["colors"]['dark']
                    self.theme_colors['bg'] = item[COLOR_THEME]["colors"]['bg']
                    self.theme_colors['fg'] = item[COLOR_THEME]["colors"]['fg']
                    self.theme_colors['border'] = item[COLOR_THEME]["colors"]['border']
                    self.theme_colors['active'] = item[COLOR_THEME]["colors"]['active']
                    self.theme_colors['selectfg'] = item[COLOR_THEME]["colors"]['selectfg']
                    self.theme_colors['selectbg'] = item[COLOR_THEME]["colors"]['selectbg']
                    self.theme_colors['inputfg'] = item[COLOR_THEME]["colors"]['inputfg']
                    self.theme_colors['inputbg'] = item[COLOR_THEME]["colors"]['inputbg']
                    self.theme_colors['type'] = item[COLOR_THEME]["type"]

        self.settings = {}
        self.conf_json = FOXDOT_CONFIG_FILE
        self.alert_text = "MODIFYING THIS FILE WILL OVERWRITE CHANGES DONE IN 'General' AND 'Appearance'. SAVE 'Preferences' FIRST TO CONTINUE!"
        self.unsaved = True

        # Load config file
        try:
            with open(self.conf_json) as f:
                self.text = f.read().rstrip()
        except FileNotFoundError:
            print("conf.json file not found")
            self.text = ""

        self.theme_name = ""

        # Settings values (using reactive variables)
        self.menu_start = MENU_ON_STARTUP
        self.linenumbers_start = LINENUMBERS_ON_STARTUP
        self.console_start = CONSOLE_ON_STARTUP
        self.treeview_start = TREEVIEW_ON_STARTUP
        self.midibar_start = MIDIBAR_ON_STARTUP
        self.recover_work = RECOVER_WORK
        self.check_update = CHECK_FOR_UPDATE
        self.linenumber_offset = str(LINE_NUMBER_MARKER_OFFSET)
        self.brackets_auto = AUTO_COMPLETE_BRACKETS
        self.address = ADDRESS
        self.port = str(PORT)
        self.port2 = str(PORT2)
        self.font = FONT
        self.sc_path = SUPERCOLLIDER
        self.sc_start = BOOT_ON_STARTUP
        self.sc3_start = SC3_PLUGINS
        self.max_ch = str(MAX_CHANNELS)
        self.samples_dir = SAMPLES_DIR
        self.sample_pack = str(SAMPLES_PACK_NUMBER)
        self.sc_info = GET_SC_INFO
        self.use_alpha = USE_ALPHA
        self.alpha_val = str(ALPHA_VALUE)
        self.alpha_start = TRANSPARENT_ON_STARTUP
        self.cpu_use = str(CPU_USAGE)
        self.clk_lat = str(CLOCK_LATENCY)
        self.fwd_address = FORWARD_ADDRESS
        self.fwd_port = str(FORWARD_PORT)
        self.theme = COLOR_THEME

    def compose(self) -> ComposeResult:
        with Container(id="preferences-container"):
            yield Static("Preferences", id="preferences-title")

            with TabbedContent():
                with TabPane("General", id="general-tab"):
                    yield self.create_general_settings()

                with TabPane("Appearance", id="appearance-tab"):
                    yield self.create_appearance_settings()

                with TabPane("Advanced", id="advanced-tab"):
                    yield self.create_advanced_settings()

            with Horizontal(id="button-row"):
                yield Button("Cancel", id="cancel-btn")
                yield Button("Save Changes", id="save-btn", variant="primary")

    def create_general_settings(self) -> ComposeResult:
        with Vertical():
            yield Static("ACTIVATED ON START", classes="section-header")
            yield Switch(value=self.menu_start, id="menu-start")
            yield Label("Menu")
            yield Switch(value=self.console_start, id="console-start")
            yield Label("Console")
            yield Switch(value=self.linenumbers_start, id="linenumbers-start")
            yield Label("Line Numbers")
            yield Switch(value=self.treeview_start, id="treeview-start")
            yield Label("Treeview")
            yield Switch(value=self.midibar_start, id="midibar-start")
            yield Label("Midibar")

            yield Static("OTHER SETTINGS", classes="section-header")
            yield Switch(value=self.recover_work, id="recover-work")
            yield Label("Recover Work")
            yield Switch(value=self.check_update, id="check-update")
            yield Label("Check for Updates")

            yield Static("EDITOR", classes="section-header")
            yield Label("Line Number Offset:")
            yield Input(value=self.linenumber_offset, id="linenumber-offset")
            yield Switch(value=self.brackets_auto, id="brackets-auto")
            yield Label("Auto Complete Brackets")

    def create_appearance_settings(self) -> ComposeResult:
        with Vertical():
            yield Static("THEME", classes="section-header")
            yield Select(
                options=[(theme, theme) for theme in self.themes],
                value=self.theme,
                id="theme-select"
            )

            yield Static("FONT", classes="section-header")
            yield Input(value=self.font, id="font-input")

    def create_advanced_settings(self) -> ComposeResult:
        with Vertical():
            yield Static(self.alert_text, classes="alert-text")
            yield TextArea(
                text=self.text,
                language="json",
                id="config-editor"
            )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "save-btn":
            self.save_changes()
        elif event.button.id == "cancel-btn":
            self.save_and_close()

    def save_and_close(self):
        """Close without saving"""
        self.app.pop_screen()

    def save_changes(self):
        """Save settings to config file"""
        text_settings = self.query_one("#config-editor").text

        if text_settings != self.text:
            try:
                self.settings.clear()
                self.settings = json.loads(text_settings)
            except Exception:
                self.app.notify("Cannot convert text to json file. Please check your changes!", severity="error")
                return
        else:
            self.settings.clear()
            self.settings['ADDRESS'] = self.address
            self.settings['PORT'] = int(self.port)
            self.settings['PORT2'] = int(self.port2)
            self.settings['FONT'] = self.font
            self.settings['SUPERCOLLIDER'] = self.sc_path
            self.settings['BOOT_ON_STARTUP'] = self.sc_start
            self.settings['SC3_PLUGINS'] = self.sc3_start
            self.settings['MAX_CHANNELS'] = int(self.max_ch)
            self.settings['SAMPLES_DIR'] = self.samples_dir
            self.settings['SAMPLES_PACK_NUMBER'] = int(self.sample_pack)
            self.settings['GET_SC_INFO'] = self.sc_info
            self.settings['USE_ALPHA'] = self.use_alpha
            self.settings['ALPHA_VALUE'] = float(self.alpha_val)
            self.settings['MENU_ON_STARTUP'] = self.query_one("#menu-start").value
            self.settings['CONSOLE_ON_STARTUP'] = self.query_one("#console-start").value
            self.settings['LINENUMBERS_ON_STARTUP'] = self.query_one("#linenumbers-start").value
            self.settings['TREEVIEW_ON_STARTUP'] = self.query_one("#treeview-start").value
            self.settings['MIDIBAR_ON_STARTUP'] = self.query_one("#midibar-start").value
            self.settings['TRANSPARENT_ON_STARTUP'] = self.alpha_start
            self.settings['RECOVER_WORK'] = self.query_one("#recover-work").value
            self.settings['CHECK_FOR_UPDATE'] = self.query_one("#check-update").value
            self.settings['LINE_NUMBER_MARKER_OFFSET'] = int(self.query_one("#linenumber-offset").value)
            self.settings['AUTO_COMPLETE_BRACKETS'] = self.query_one("#brackets-auto").value
            self.settings['CPU_USAGE'] = int(self.cpu_use)
            self.settings['CLOCK_LATENCY'] = int(self.clk_lat)
            self.settings['FORWARD_ADDRESS'] = self.fwd_address
            self.settings['FORWARD_PORT'] = int(self.fwd_port)
            self.settings['COLOR_THEME'] = self.query_one("#theme-select").value

        settings_file = open(self.conf_json, "w")
        json.dump(self.settings, settings_file, indent=6)
        settings_file.close()

        self.app.notify("A restart of FoxDot is required for the changes to take effect", severity="warning")
        self.app.pop_screen()
