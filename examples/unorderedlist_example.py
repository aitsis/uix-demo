from uix.elements import listitem, unorderedlist

def unorderedlist_example():
    with unorderedlist(""):
        listitem("Item 1")
        listitem("Item 2")
        listitem("Item 3")

title = "Unorderedlist"
description = '''
## unorderedlist(value,id,role)
1. Temel unorderedlist elementi listitem elementleri ile kullanılır.

| attr          | desc                                          |
| :------------ | :---------------------------------------------|
| id            | unorderedlistin id'si                         |
| value         | unorderedlistin içeriği                       |
| role          | unorderedlistin rolü |
'''