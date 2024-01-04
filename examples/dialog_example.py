from uix.elements import dialog, container, button, text
from uix.elements._dialog import title, description, sample as code


def dialog_example1():
    with dialog(id="dialog_example",is_clickable_anywhere=True) as dialog1:
        with container("",):
            text("Dialog Example 1")
            text("Click anywhere to close")
            button("Close")
    button("Dialog 1").on("click", lambda ctx, id, value: dialog.open(dialog1))
    return dialog1

def dialog_example2():
    with dialog(id="dialog1", is_clickable_anywhere=False) as dialog2:
        with container("",):
            text("Dialog Example 2")
            text("Click the close button to close")
            button("Close")
    button("Dialog 2").on("click", lambda ctx, id, value: dialog.open(dialog2))
    return dialog2

def dialog_example():
    dialog_example1()
    dialog_example2()