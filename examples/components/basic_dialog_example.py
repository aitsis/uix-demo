from uix_components import basic_dialog
from uix.elements import button
from .basic_checkbox_example import basic_checkbox_example

def basic_dialog_example():
    button("Open Dialog", id = "openDialog").style("width","min-content").on("click", lambda ctx, id, value: ctx.elements["myDialog"].show())
    basic_dialog(id = "myDialog",elements=[basic_checkbox_example], close_on_outside = True).style("width","25%").style("text-align","center")

title = "Basic Dialog"
description = """
# basic_dialog(id, elements, close_on_outside = True)
1. Basic Dialog bir dialog komponentidir.
    | attr          | desc                                                |
    | :------------ | :------------------------------------------------   |
    | id            | Komponentin id'si                                   |
    | elements      | Dialog içindeki komponentler                        |
    | close_on_outside | Dışarı tıklandığında kapanma durumu              |
"""