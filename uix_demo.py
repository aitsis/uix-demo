import uix
from uix.elements import div, button
# Main Application Instance

def main():
    with div("main") as ui:
        div("Hello World")
        button("Hello World")
    return ui

uix.start(ui = main, debug = True)

