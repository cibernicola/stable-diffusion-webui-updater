import modules.scripts as scripts
import gradio as gr
import os

import modules.extras
import modules.ui
from modules.shared import opts, cmd_opts
from modules import shared, scripts
from modules import script_callbacks

def on_ui_settings():
    section = ('updates-history', "Custom updater")
    shared.opts.add_option("always_check_and_update", shared.OptionInfo(False, "Check and update always", section=section))
script_callbacks.on_ui_settings(on_ui_settings)