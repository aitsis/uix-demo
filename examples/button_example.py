from uix.elements import button # type: ignore
from uix.elements._button import title, description, sample as code

def button_example():
    main = button("Click me!").style("margin","auto").style("display","block")
    return main

