from uix.elements import text, div, row
from uix_components import tree_view
from uix.core.session import context

data = {
    "Examples": {
        "Styles": {
            "Colors": ["Red", "Green"],
            "Shapes": ["Circle", "Square"]
        },
        "Components": ["Select", "Tree View"]
    }
 }
# label id'si ve label değeri olan bir veri yapısı
data2 = {
    "Examples": {
        "Colors": [
            {"Red": "red-id"},
            {"Blue": "blue-id"}
        ],
        "Shapes": [
            {"Circle": "circle-id"},
            {"Square": "square-id"}
        ]
    }
}

def select_label(ctx, id, value):
    ctx.elements["output"].value = f'Selected Value: {value}'

def open_components():
    ctx = context.session.context
    # Açık olmasını istediğiniz details elementinin id'si
    # Default olarak "details-" ile başlar
    ctx.elements["details-Components"].attrs["open"] = "True"

def tree_view_example():
    with div():
        with row().style("gap","20px"):
            tree_view(id="tree_1",data=data, callback= select_label)
            tree_view(id="tree_2",data=data2, callback= select_label)
        text("Selected Value:", id="output")
        open_components()

title="Tree View"
description="""
## tree_view(id, data, callback, selected_label)
1. Verilen veri yapısına göre ağaç yapısı oluşturur.
2. Veri yapısı içindeki her bir anahtar bir başlık olarak kullanılır.
3. Anahtarın değeri bir liste ise, liste elemanları alt başlık olarak kullanılır.
4. Anahtarın değeri bir sözlük ise, id ve label değerlerini kullanarak alt ağaç oluşturulur.
5. Label'a tıklandığında callback fonksiyonu çalışır.


| attr                  | desc                                                 |
| :-------------------- | :------------------------------------------------    |
| id                    | tree_view elementinin id'si                          |
| data                  | ağaç yapısının oluşturulması için gerekli veri yapısı|
| callback              | Label'a tıklandığında çalışacak fonksiyon            |
| selected_label        | Önceden seçili olmasını istediğiniz elemanın değeri  |
"""