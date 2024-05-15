from uix.elements import text
from uix_components import basic_checkbox

def on_change(ctx,id,value):
    ctx.elements["test"].value = value
    ctx.elements["test"].update()

def basic_checkbox_example():
    basic_checkbox(id = "myCheckbox",label_text="Label Text",callback=on_change)
    text(id="test", value="Checkbox Value")

title = "Basic Checkbox"
description = """
# basic_checkbox(id, label_text, value, callback)
1. Basic Checkbox bir checkbox komponentidir.
    | attr          | desc                                                |
    | :------------ | :------------------------------------------------   |
    | id            | Komponentin id'si                                   |
    | label_text    | Komponentin yanındaki yazı                          |
    | value         | Komponentin değeri                                  |
    | callback      | Komponentin değeri değiştiğinde çalışacak fonksiyon |
"""




