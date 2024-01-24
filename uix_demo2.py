import uix

from uix.elements import container,div, border

from uix_components import fabric

def main():
    with border() as main: 
        fabric(id="fabric1", width=1000, height=1000).cls("center")
    return main

uix.start(ui=main(), config={"debug": True})