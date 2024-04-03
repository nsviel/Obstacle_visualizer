#---------------------------------------------
from src.gui import gui
from src.utils import param
from src.utils import terminal
import time


def program():
    init()
    loop()
    end()

def init():
    gui.initialization()
    terminal.addLog("OK", "Program initialized...")
    terminal.addLine()

def loop():
    is_running = True
    param.run_loop = True
    while param.run_loop and is_running:
        is_running = gui.loop()

def end():
    terminal.shutdown()
