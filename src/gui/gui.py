#---------------------------------------------
from src.utils import param
from src.gui.style import gui_theme
from src.gui.style import gui_color
import dearpygui.dearpygui as dpg


# GUI creation / Destruction
def initialization():
    dpg.create_context()
    gui_theme.gui_theme()
    setup_gui()
def loop():
    dpg.render_dearpygui_frame()
    return dpg.is_dearpygui_running()
def termination():
    dpg.destroy_context()

# GUI setup
def setup_gui():
    dpg.create_viewport(title='Control Interface', width=param.gui_width, height=param.gui_height)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window(gui_ID.ID_window, True)
