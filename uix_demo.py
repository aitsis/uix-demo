import uix
from uix.core.element import Element
# Main Application Instance

def main():
    ui = Element("Hello World")
    return ui

uix.start(ui = main, debug = True)

