from uix.elements import div, button, grid
from uix.elements._grid import title, description, sample as code
counter = 0
def next_counter():
    global counter
    counter = counter + 1
    return counter

def on_click(ctx, id, value):
    print("Clicked", id, value)
    ctx.element.value = "Clicked!" + str(next_counter())

def button1(value):
    button(value).on("click",on_click)

def comp1():
    with grid("",columns= "40% 1fr").style("margin","auto") as grid1:
        grid1.style("width","400px")
        grid1.style("border","1px #aaa solid")
        grid1.style("padding","10px")
        grid1.style("gap","10px")
        grid1.style("border-radius","10px")
        button1("A!")
        button1("B!")
        button1("C!")
        button1("D!")


def grid_example():
    with div("") as main:
        comp1()
    return main
