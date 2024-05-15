from uix.elements import div, button, row
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
    ctx.elements["menu_example"].update(draw_menu)

def locale_example():
    with div("",) as locale_example:
        with row("", id ="menu_example") as menu:
            draw_menu()

title = "Locale"
description = '''
## Locale
1. Uygulamanın dilini değiştirmek için kullanılır.
'''