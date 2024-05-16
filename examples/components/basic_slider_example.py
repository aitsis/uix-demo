from uix.elements import div
from uix_components import basic_slider

def basic_slider_example():
    with div().cls("border").style("width","50%") as slider_example:
        basic_slider(name="Deneme", id = "mySlider", callback = lambda ctx, id, value: print(f"Slider {id} changed to: {value}"))
    return slider_example

title = "Basic Slider"
description = """
 #basic_slider(name, id, min, max, value, step, callback)
 1. Slider elementinin içerisinde input elementi eklenerek oluşturulan bir componenttir.
    | attr          | desc                                                          |
    | :------------ | :------------------------------------------------------------ |
    | name          | Slider Componentinin name'i input'un önünde yazar             |
    | id            | Slider Componentinin id'si                                    |
    | min           | Slider Componentinin minimum değeri                           |
    | max           | Slider Componentinin maksimum değeri                          |
    | value         | Slider Componentinin başlangıç değeri                         |
    | step          | Slider Componentinin artış değeri                             |
    | callback      | Slider Componentinin değeri değiştiğinde çağırılacak fonksiyon|
 """