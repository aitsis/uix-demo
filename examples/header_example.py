from uix.elements import header,button

def header_example():
    with header().style("height: 100%;"):
        button("Home")
    return 


title = "Header"
description = '''
## header(value,id = None)
1. Header elementi. Html header elementine karşılık gelir. İçerisine eklenen elemanlar, kullanıldığı divin en üstünde yer alır.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Header elementinin id'si                          |
| value         | Header elementinin içeriği                       |
'''