from uix.elements import text
from uix_components import basic_select

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

title = "Basic Select"
description = """
# basic_select(id, value, options callback)
1. Basic Select bir select komponentidir.
    | attr          | desc                                                       |
    | :------------ | :-----------------------------------------------------     |
    | id            | Komponentin id'si                                          |
    | value         | Komponentin değeri                                         |
    | options       | Komponentin seçenekleri dict veya list olarak verilebilir. |
    | callback      | Komponentin değeri değiştiğinde çalışacak fonksiyon        |
"""