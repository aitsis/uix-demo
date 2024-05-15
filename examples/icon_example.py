from uix.elements import div, icon, text # type: ignore

def icon_example():
    with div():
        icon("fa-solid fa-house fa-1x")
        icon("fa-solid fa-house fa-2x")
        icon("fa-solid fa-house fa-3x")
        icon("fa-solid fa-house").style("font-size","30px").style("color","var(--ait)")
        icon("fa-solid fa-house fa-5x")
        text("Merhaba").cls("fa-shake")
        icon("fa-solid fa-house fa-7x fa-bounce")
        icon("fa-solid fa-house fa-10x")

title = "Icon"
description = '''
## icon(value,id = None)
1. Icon elementi. Html'deki i elementine karşılık gelir. Fontawesome sınıfları kullanılarak svg iconlar oluşturulabilir.
2. [https://fontawesome.com/search?o=r&m=free](https://fontawesome.com/search?o=r&m=free) adresinden kullanılabilir iconlara ulaşılabilir.
3. Bulunduğu yerin font büyüklüğü ne ise büyüklük olarak varsayılan onu alır.
4. Büyüklüğünü ayarlamak için "font-size" stil i kullanılmalı.
5. Büyüklüğünü ayarlamanın başka bir yolu sınıfa "fa-10x" gibi değer eklemektir. fa-1x ile fa-10x arası verilebilir.
6. Rengini yazıya renk verir gibi verebiliriz.
7. Çekirdeğe eklenen fontawesome sınıfları sayesinde animasyonların hepsi sınıf olarak isttenen her elemente eklenebilir hale geldi.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Icon elementinin id'si                            |
| value         | Fontawesome sitesinden alınan classlar kullanılır |
'''