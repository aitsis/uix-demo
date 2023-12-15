import uix
from uix.core.element import Element
# Main Application Instance
app = uix.uix_app

def main():
    ui = Element("Hello World")
    return ui

app.start(ui = main, debug = True)

