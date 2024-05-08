from uix.elements import select, option, text
from uix.elements._select import title, description, sample as code

def on_change(ctx,id, value):
    ctx.elements["output"].value = value

def select_option_example():
    with select(id= "mySelect").on("change",on_change):
        option(text="Option 1", value="1")
        option(text="Option 2", value="2").selected()
        option(text="Option 3", value="3").disabled()
    text("Selected Value", id="output")       