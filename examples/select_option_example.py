from uix.elements import select, option, text

def on_change(ctx,id, value):
    ctx.elements["output"].value = value

def select_option_example():
    with select(id= "mySelect").on("change",on_change):
        option(text="Option 1", value="1")
        option(text="Option 2", value="2").selected()
        option(text="Option 3", value="3").disabled()
    text("Selected Value", id="output")

title = "Select"
description = '''
## select(value,id)
1. Temel select elementi. Tek başına kullanılmaz. Option elementleri ile kullanılır.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Select elementinin id'si                          |
| value         | Option elementi seçildiğinde alınacak değer       |
| text          | Option elementinin metni                          |
| disabled      | Select içeriğinin seçilmesini engeller            |
| selected      | Başlangıçta seçili olacak option elementi         |
'''