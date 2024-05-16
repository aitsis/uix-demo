from uix.elements import label

def label_example():
    main = label("This Text is a Label!").style("font-size","20px")
    return main

title = "Label"
description = '''
## label(value,id,tabindex = -1,usefor = None)
1. Label elementi. Bir input elementine ait label elementi için kullanılır.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Labelin id'si                          |
| value         | Label içeriği                       |
| tabindex      | Labelin tabindex'i. Varsayılan değer: -1. Değer -1 ise tab ile focuslanamaz. |
| usefor        | Labelin kullanıldığı input elementinin id'si |
'''