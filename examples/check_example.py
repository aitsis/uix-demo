from uix.elements import check, div

def check_example():
    main = check("", id="check_example").on("click", on_click)
    div("test", "test")
    return main

def on_click(ctx, id, value):
    print("Clicked", id, value)
    if value == False:
        ctx.elements["test"].value = "Unchecked!"
    else:
        ctx.elements["test"].value = "Checked!"
    ctx.elements["test"].update()

title = "Check"
description = """
## check(value,id,checked,disabled)
1. Checkbox bir input elementidir.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Check elementinin id'si                           |
| value         | Check elementinin içeriği                         |
| checked       | Check'in seçili olup olmadığı                     |
| disabled      | Check'in etkinliğini kapatır.                     |
"""