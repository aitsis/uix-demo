from uix.elements import border, button
example_button = ["A!", "B!", "C!", "D!"]

def border_example():
    for i in range(len(example_button)):
        with border("",) as border_demo:
            button(example_button[i])
    return border_demo

title = "Border"
description = '''
## border(value,id)
1. Border elementi. Kenarında 1px kalınlığında çizgi bulunan bir div oluşturur.
İçerisine elemanlar eklenerek kullanılır.

| attr          | desc                                             |
| :------------ | :------------------------------------------------|
| id            | Border elementinin id'si                         |
| value         | Border elementinin içeriği                       |
'''