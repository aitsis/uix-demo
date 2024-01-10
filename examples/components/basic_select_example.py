from uix.elements import text
from uix_components import basic_select
from uix_components._basic_select._basic_select import title, description, sample as code

options = [
    {"id":"1","isSelect":False, "value":"Option 1"},
    {"id":"2","isSelect":False, "value":"Option 2"},
    {"id":"3","isSelect":True, "value":"Option 3"},
]

def on_change(ctx,id,value):
    ctx.elements["test"].value = value
    ctx.elements["test"].update()

def basic_select_example():
    basic_select(id = "mySelect",options = options, callback=on_change)
    text(id="test", value="Select Value")