# Python main
import sys
import os
import json
from queue import Queue
import threading
from pathlib import Path
import time
# Textual
from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Header, Footer, Static, OptionList, Label
from textual.scroll_view import ScrollView
from textual.reactive import reactive
from textual.message import Message
from textual.binding import Binding
from textual.screen import ModalScreen
from textual import events
from textual.widgets import RichLog, DirectoryTree, Input, Button
from textual_textarea import TextEditor
