from uix.elements import table, tr, td, tbody, th, thead # type: ignore
from uix.elements._table import title, description, sample as code

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

def table_example():
    with table("", id="table_example"):
        global fake_data
        with thead("",id="table_example_header"):
            with tr("",id="table_example_header_row"):
                th("ID")
                th("Name")
                th("Username")
                th("Email")
        with tbody("",id="table_example_body"):
            for item in fake_data:
                with tr("",id=item["id"]):
                    td(item["id"])
                    td(item["name"])
                    td(item["username"])
                    td(item["email"])
                    