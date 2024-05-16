from uix_components import basic_table
from uix.elements import div

headers = ["Header 1", "Header 2", "Header 3"]
data = [
    ["Row 1", "Row 1", "Row 1"],
    ["Row 2", "Row 2", "Row 2"],
    ["Row 3", "Row 3", "Row 3"],
]
  
def basic_table_example():
    with div() as table_example:
        basic_table(id= "basic_table_example", headers=headers, data=data)
    return table_example

title="Basic Table"
description="""
## basic_table(id, headers, data)
1. Verilen başlık ve satırlara göre tablo oluşturur.

| attr          | desc                                                          |
| :------------ | :------------------------------------------------------------ |
| id            | Tablo elementinin id'si                                       |
| headers       | Tablo başlıklarını içeren liste                               |
| data          | Tablo satırlarını içeren liste                                |
"""