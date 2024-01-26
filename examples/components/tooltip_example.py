from uix.elements import div, icon, text, button # type: ignore
from uix_components import tooltip

def tooltip_example():
    with div().cls("row").style("gap","10px"):
        with button("BUTTON", type="reset").attr("uix-tooltip-location","right").attr("uix-tooltip", "Merhaba Dünya! Buraya uix-tooltip geliyor."):
            with tooltip(position="right"):
                    icon("fa-solid fa-heart fa-beat").style("float: left; margin: 3px; color: red;")
                    text("Merhabalar buraya text geliyor.")
        text("Buraya yazı gelecek. Yazılar burda yazarken sonra")
        with text(" burada"):
            tooltip("Buraya da istenilen açıklama")
        text(" bir açıklama eklenerek.")
        with text("Aşağıda"):
             tooltip("Burayada aşağıda bir açıklama ekliyoruz.", position="bottom")
        text("da bir açıklama ekleyebiliriz.")
                 


title = "Tooltip"

description = '''
## tooltip("AÇIKLAMA BURAYA", position="top")

1. tooltip position parametresi alabileceği seçenekler: top, bottom, right, left. (String olarak yazılmalı)
2. postion parametresi eklenmezse varsayılan olarak top gelir.
3. Her elemana alt eleman olarak eklenebilir.(button, text, icon vs.) Parent ına tooltip stil sınıfını otomatik ekler.
4. with ile yazılırsa içine istenilen eleman eklenebilir.


| attr                  | desc                                                      |
| :-------------------- | :-------------------------------------------------------- |
| tooltip               | Tooltip içeriğinde yazacak metin.                         |
| position              | Tooltip balonu görüntüleneceği yön.                       |
'''

code = """
from uix.elements import div, icon, text, button # type: ignore
from uix_components import tooltip

def tooltip_example():
    with div().cls("row").style("gap","10px"):
        with button("BUTTON", type="reset").attr("uix-tooltip-location","right").attr("uix-tooltip", "Merhaba Dünya! Buraya uix-tooltip geliyor."):
            with tooltip(position="right"):
                    icon("fa-solid fa-heart fa-beat").style("float: left; margin: 3px; color: red;")
                    text("Merhabalar buraya text geliyor.")
        text("Buraya yazı gelecek. Yazılar burda yazarken sonra")
        with text(" burada"):
            tooltip("Buraya da istenilen açıklama")
        text(" bir açıklama eklenerek.")
        with text("Aşağıda"):
             tooltip("Burayada aşağıda bir açıklama ekliyoruz.", position="bottom")
        text("da bir açıklama ekleyebiliriz.")
"""