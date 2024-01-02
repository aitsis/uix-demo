import os
from uix.elements import div, button # type: ignore

_on_selection_changed = None

def menu_select(ctx, id, value):
    ctx.data["menu-selection"] = id[-2:]
    if _on_selection_changed:
        _on_selection_changed(ctx, id, value)

def menu_item(title, id):
    button(title,id=id).on("click",menu_select).cls("menu-item").style("height","fit-content")
    
def menu(on_selection_changed = None,menu_list = None):
    global _on_selection_changed
    _on_selection_changed = on_selection_changed
    with div() as menu_border:
        menu_border.cls("menu border")
        for item in menu_list:
            menu_item(item["title"], item["id"])
        