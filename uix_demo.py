import uix
from uix.elements import div, button, grid
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
    with grid("",columns= "40% 1fr") as grid1:
        grid1.style("width","400px")
        button1("A!")
        button1("B!")
        button1("C!")
        button1("D!")


with div("Example") as main:
    comp1()

print(main.render())
uix.start(ui = main,debug=True)
