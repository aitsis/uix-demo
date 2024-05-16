from uix.elements._textarea import textarea
from uix.elements._div import div

def textarea_example():
    main = textarea("","textare_example", placeholder="Selam").on("input", on_change)
    div(id="test", value="Selam")
    return main

def on_change(ctx, id, value):
    print("Changed", id, value)
    ctx.elements["test"].value = value
    ctx.elements["test"].update()

title = "Textarea"
description = """
## textarea(value,id,placeholder)
1. Temel textarea elementi.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Textarea elementinin id'si                          |
| value         | Textarea elementinin içeriği                       |
| placeholder   | Textarea elementinin placeholder değeri            |
"""