from uix.elements import unorderedlist, listitem # type: ignore
from uix.elements._listitem import title, description, sample as code

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
