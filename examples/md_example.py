from uix.elements import md

def md_example():
    main = md('''# Hello World!
```python
from uix.elements import div

def hello_world_example():
    main = div("Hello World!").style("font-size","30px")
    return main
```
               ''')
    return main

title = "Markdown"
description = '''
## md(value,id)
1. Markdown elementi. Markdown dilinde yazılmış metni html'e çevirir.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Markdown elementinin id'si                        |
| value         | Markdown elementinin içeriği                      |
'''