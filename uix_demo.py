import uix
from uix.elements import div, button, grid, border, row

from examples.basic.grid_example import grid_example
from _menu import menu

uix.html.add_css_file("uix_demo.css")

def chooseExample(ctx, id, value):
    print("Clicked", id, value)
    
with div("") as page:
    page.style("padding","10px")
    with grid("",columns = "150px 600px") as main:
        main.cls("main")
        menu()
        with div("") as content:
            content.cls("content border")
        
uix.start(ui = main,debug=True)
