from uix.elements import header,button
from uix.elements._header import title, description, sample as code

def header_example():
    with header().style("height: 100%;"):
        button("Home")
    return 