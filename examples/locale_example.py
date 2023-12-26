from uix.elements import div, button, row # type: ignore
from uix import T
import uix
example_menu = ["Main", "File", "Help", "About", "Turkish", "English"]

def draw_menu():
    for item in example_menu:
        button(T(item),id=item).on("click", on_menu_click)

def on_menu_click(ctx, id, value):
    if id == "Turkish":
        uix.set_lang("tr")
    elif id == "English":
        uix.set_lang("en")
    with ctx.elements["menu"]:
        draw_menu()
    ctx.elements["menu"].update()

def locale_example():
    with div("",) as locale_example:
        with row("", id ="menu") as menu:
            draw_menu()
    