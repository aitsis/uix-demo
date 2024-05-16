from uix.elements import text

def text_example():
    value="Hello World!"
    main = text(value)
    return main

title = "Text"
description = '''
## text(value,id = None)
1. Html'deki p elementine karşılık gelir. Sayfada görüntülenmesi istenen yazılar için kullanılır.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Text elementinin id'si                          |
| value         | Text elementinin içeriği                       |
'''