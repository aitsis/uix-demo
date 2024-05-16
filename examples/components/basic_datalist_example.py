from uix_components import basic_datalist

options = ["BMW","AUDI","MERCEDES"]

def basic_datalist_example():
    basic_datalist(name="Car List", id = "dl-1", options = options, callback = lambda ctx, id, value: print(f"Datalist {id} changed to: {value}"))

title = "Basic Datalist"
description = """
# basic_datalist(name, value, id, options[], callback)
1. Input elementinin içerinde datalist elementi eklenerek oluşturulan bir componenttir. option elementi ile datalist'in içi doldurulur.
    | attr          | desc                                                          |
    | :------------ | :------------------------------------------------------------ |
    | name          | Datalist Componentinin name'i input'un önünde yazar           |
    | value         | Datalist Componentinin içeriği                                |
    | id            | Datalist Componentinin id'si                                  |
    | option        | Datalist Componentinin liste elemanlarını array olarak alır   |
    | callback      | Listeden bir seçim yapıldıığında çağırılacak fonksiyon        |
"""