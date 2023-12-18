import os
from uix.elements import div, button, grid, border, row

def menu_select(ctx, id, value):
    print("Clicked", id, value)

def menu_item(value):
    btn = button(value).on("click",menu_select)
    btn.cls("menu-item")


def menu():
    with div() as menu_border:
        menu_border.cls("menu border")
        # load menu items from examples folder
        print(os.listdir("examples"))
        for file in os.listdir("examples/basic"):
            if file.endswith(".py"):
                print(file)
                menu_item(file[:-3])
        