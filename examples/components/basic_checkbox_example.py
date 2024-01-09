from uix.elements import text
from uix_components import basic_checkbox
from uix_components._basic_checkbox._basic_checkbox import title, description, sample as code

def on_change(ctx,id,value):
    ctx.elements["test"].value = value
    ctx.elements["test"].update()

def basic_checkbox_example():
    basic_checkbox(id = "myCheckbox",label_text="Label Text",callback=on_change)
    text(id="test", value="Checkbox Value")




