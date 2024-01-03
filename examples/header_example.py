from uix.elements import header,button,div
from uix.elements._header import title, description, sample as code

def header_example():
    with div("") as header_example:
        header_example.style("height","100%")
        with header("",):
            button("Home")
    return header_example