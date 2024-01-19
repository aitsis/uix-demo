import uix
from uix.elements import border, md
from uix_components import chart
print("Imported: chart_example")

chart_value = {
            "type": "line",
            "data": {
            "labels": ["January", "February", "March", "April", "May", "June", "July"],
            "datasets": [
                {
                    "label": "My First dataset",
                    "backgroundColor": "rgba(255,99,132,0.2)",
                    "borderColor": "rgba(255,199,132,1)",
                    "borderWidth": 2,
                    "hoverBackgroundColor": "rgba(255,99,132,0.4)",
                    "hoverBorderColor": "rgba(255,99,132,1)",
                    "data": [65, 59, 80, 81, 56, 55, 40],
                }
            ],
        },
        "options": {
            "responsive": True,
            "plugins": {
                "legend": {
                "position": 'top',
                },
            "title": {
            "display": True,
            "text": 'Example Chart'
                }
            }
        }
    }


descriptions = [
"""
-----
# chart
## 1 - Temel Chart Kullanımı
## 2 - Basit Chart Kullanımı
----
## 1 - Temel Chart Kullanımı
Bu kullanımda chart componenti oluşturulur ve value değişkeni ile chart'ın tüm özellikleri belirlenir.

Bu en temel kullanım şeklidir.

[https://www.chartjs.org/docs/latest/](https://www.chartjs.org/docs/latest/) adresinden chart'ın tüm özelliklerine ulaşabilirsiniz.

Temel kullanımda aşağıdaki gibi tüm veri seti belirlenir:
```python
chart_value = {
            "type": "line",
            "data": {
            "labels": ["January", "February", "March", "April", "May", "June", "July"],
            "datasets": [
                {
                    "label": "My First dataset",
                    "backgroundColor": "rgba(255,99,132,0.2)",
                    "borderColor": "rgba(255,99,132,1)",
                    "borderWidth": 1,
                    "hoverBackgroundColor": "rgba(255,99,132,0.4)",
                    "hoverBorderColor": "rgba(255,99,132,1)",
                    "data": [65, 59, 80, 81, 56, 55, 40],
                }
            ],
        }}
```
Ardından chart componenti oluşturulur:
```python

from uix_components import chart

 chart1 = chart(id="chart1",value= chart_value).size("100%","500px")

```
"""
,
"""
## 2 - Basit Chart Kullanımı
Bu kullanımda chart componenti oluşturulur ve value değişkeni ile chart'ın tüm özellikleri belirlenir.

Bu en temel kullanım şeklidir.





"""
]

import numpy as np
test_data = np.random.randint(0, 100, size=(2, 100))
print(test_data)

def chart_example():
    with uix.elements.border().size("100%","100%").style("overflow-y","auto") as main:
        md(descriptions[0])
        c1 = chart(id="chart1",type="line",value= chart_value).size("100%","500px")
        c1.attrs["height"] ="500px"
        md(descriptions[1])
    return main

uix.start(ui = chart_example(), config={"debug":True})


# TODO

# eklenecek elementler
# !? meter
# object ???

