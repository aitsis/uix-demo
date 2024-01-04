from uix.elements import datalist,input,option,button,text
from uix.elements._datalist import title, description, sample as code

def on_click(ctx,id,value):
    ctx.elements["output"].value = ctx.elements["carInput"].value

def on_change(ctx,id,value):
    ctx.elements["carInput"].value = value

def datalist_example():
    input(list="cars",placeholder="Choose a car",id="carInput").on("change",on_change)
    with datalist(id="cars"):
        option("Ford")
        option("Volvo")
        option("BMW")
    button("Submit").on("click",on_click)
    text("",id="output")