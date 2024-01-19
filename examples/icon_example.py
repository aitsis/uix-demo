from uix.elements import div, icon # type: ignore

def icon_example():
    with div().cls("row").style("gap","10px"):
        icon("fa-solid fa-house fa-1x")
        icon("fa-solid fa-house fa-2x")
        icon("fa-solid fa-house fa-3x")
        icon("fa-solid fa-house").style("font-size","30px").style("color","var(--ait)")
        icon("fa-solid fa-house fa-5x")
        icon("fa-solid fa-house fa-7x")
        icon("fa-solid fa-house fa-10x")

title = "Icon"

description = '''
## icon(value,id = None)
1. Icon elementi. Html'deki i elementine karşılık gelir. Fontawesome sınıfları kullanılarak svg iconlar oluşturulabilir.
2. https://fontawesome.com/search?o=r&m=free adresinden kullanılabilir iconlara ulaşılabilir.
3. Bulunduğu yerin font büyüklüğü ne ise büyüklük olarak varsayılan onu alır.
4. Büyüklüğünü ayarlamak için "font-size" stil i kullanılmalı.
5. Büyüklüğünü ayarlamanın başka bir yolu sınıfa "fa-10x" gibi değer eklemektir. fa-1x ile fa-10x arası verilebilir.
6. Rengini yazıya renk verir gibi verebiliriz.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Icon elementinin id'si                            |
| value         | Fontawesome sitesinden alınan classlar kullanılır |
'''

code = """
from uix.elements import div, icon # type: ignore

def icon_example():
    with div().cls("row").style("gap","10px"):
        icon("fa-solid fa-house fa-1x")
        icon("fa-solid fa-house fa-2x")
        icon("fa-solid fa-house fa-3x")
        icon("fa-solid fa-house").style("font-size","30px").style("color","var(--ait)")
        icon("fa-solid fa-house fa-5x")
        icon("fa-solid fa-house fa-7x")
        icon("fa-solid fa-house fa-10x")
"""