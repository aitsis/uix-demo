from uix.elements import unorderedlist, listitem

fake_data = [
    {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "leannge@gmail.com"
    },
    {
        "id": 2,
        "name": "Ervin Howell",
        "username": "Antonette",
        "email": "ervin@gmail.com"
    },
    {
        "id": 3,
        "name": "Clementine Bauch",
        "username": "Samantha",
        "email": "clementine@gmail.com"
    },
    {
        "id": 4,
        "name": "Patricia Lebsack",
        "username": "Karianne",
        "email": "patricia@gmail.com"
    },
    {
        "id": 5,
        "name": "Chelsey Dietrich",
        "username": "Kamren",
        "email": "chelsey@gmail.com"
    }
]

def listitem_example():
    with unorderedlist("", id="listitem_example"):
        global fake_data
        for item in fake_data:
            listitem(item["name"], id=item["id"])

title = "List Item"
description = '''
## listitem(value,id)
1. Liste elemanı elementi. Sıralı liste elementine veya sırasız liste elementine eleman eklemek için kullanılır.

| attr          | desc                                                       |
| :------------ | :--------------------------------------------------------- |
| id            | Liste elemanının id'si                                     |
| value         | Liste elemanının içeriği                                   |
| attributes    | Liste elemanına ait attribute'lar                          |
| attrs["class"]| Liste elemanına ait class'lar. Varsayılan değer: list-item |
'''