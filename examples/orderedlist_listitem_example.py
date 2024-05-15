from uix.elements import listitem, orderedlist

def orderedlist_listitem_example():
    with orderedlist(id="myList") as main:
        listitem(value="Item 1")   
        listitem(value="Item 2")        
        listitem(value="Item 3")
    return main
        
title = "Ordered List"
description = '''
## orderedlist(value,id)
1. Sıralı liste elementi. Listeye eleman eklemek için listitem elementi kullanılır.

| attr          | desc                                |
| :------------ | :-----------------------------------|
| id            | Sıralı Listenin id'si               |
| value         | Liste içeriği                       |
'''
