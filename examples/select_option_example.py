from uix.elements import select, option, text
from uix.elements._select import title, description, sample as code

def on_change(ctx,id, value):
    ctx.elements["output"].value = value

def select_option_example():
    with select("Option 3", "mySelect").on("change",on_change):
        option("Option 1")
        option("Option 2").selected()
        option("Option 3")
    text("", id="output")       