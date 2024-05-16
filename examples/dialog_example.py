from uix.elements import dialog, container, button, text

def dialog_example1():
    with dialog(id="dialog_example",close_on_outside=True) as dialog1:
        with container("",):
            text("Dialog Example 1")
            text("Click anywhere to close")
            button("Close").on("click", lambda ctx, id, value: dialog.hide(dialog1))
    button("Dialog 1").on("click", lambda ctx, id, value: dialog.show(dialog1))
    return dialog1

def dialog_example2():
    with dialog(id="dialog1", close_on_outside=False) as dialog2:
        with container("",):
            text("Dialog Example 2")
            text("Click the close button to close")
            button("Close").on("click", lambda ctx, id, value: dialog.hide(dialog2))
    button("Dialog 2").on("click", lambda ctx, id, value: dialog.show(dialog2))
    return dialog2

def dialog_example():
    dialog_example1()
    dialog_example2()

title = "Dialog"
description = '''
## dialog(value,id = None, is_clickable_anywhere = True)
1. Dialog elementi. Bir dialog penceresi açar.

| attr                  | desc                                             |
| :-------------------- | :------------------------------------------------|
| id                    | Dialog elementinin id'si                         |
| value                 | Dialog elementinin içeriği                       |
| close_on_outside      | Dışarı tıklanınca kapanma özelliği               |
'''