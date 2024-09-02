import uix
from uix.elements import md
from uix_components import chart

chart_value = {
            "type": "bar",
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
                "plugins": {
                    "title": {
                        "display": True,
                        "text": "Custom Chart Title"
                    },
                    "datalabels": {
                        "anchor": 'center',
                        "align": 'center',
                        "color": 'black',
                        "font": {
                            "size": 16,
                            "weight": 'bold'
                        }
                    }
                }
            },
    }


def chart_example():
    with uix.elements.border().size("100%","fit-content") as main:
        c1 = chart(id="chart1",value= chart_value).size("100%","100%")
        c1.attrs["height"] ="500px"
    return main

title = "Chart"
description = """
# chart(id, value=None)
Chart componenti ile chartjs kütüphanesindeki tüm chartlar kullanılabilir.
-----
## Temel Chart Kullanımı
Bu kullanımda chart componenti oluşturulur ve value değişkeni ile chart'ın tüm özellikleri belirlenir.

Bu en temel kullanım şeklidir.

[https://www.chartjs.org/docs/latest/](https://www.chartjs.org/docs/latest/) adresinden chart'ın tüm özelliklerine ulaşabilirsiniz.

Temel kullanımda aşağıdaki gibi tüm veri seti belirlenir:
```python
chart_value = {
            "type": "bar",
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
            "options": {
                "plugins": {
                    "title": {
                        "display": True,
                        "text": "Custom Chart Title"
                    },
                    "datalabels": {
                        "anchor": 'end',
                        "align": 'end',
                        "color": 'black',
                        "font": {
                            "weight": 'bold'
                        }
                    }
                }
            },
        }}
```
Ardından chart componenti oluşturulur:
```python

from uix_components import chart

chart1 = chart(id="chart1",value= chart_value).size("100%","500px")

```
"""