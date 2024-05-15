from uix.elements import details, text

def details_example():    
    with details(open=True) as details_example:
        text("Details Content")
    return details_example

title = "Details"
description = '''
## details(value,id = None)
1. Details elementi. Bilgilerin yalnızca widget "açık" duruma getirildiğinde görülebildiği bir açıklama widget'ı oluşturur.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Details elementinin id'si                         |
| value         | Details elementinin başlığı                       |
| open          | Details elementinin açık olup olmadığı            |
'''