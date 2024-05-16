import uix
from uix.elements import button,row
from uix_components import chart_pie

tupple1 = (1, 2, 3, 4, 5)
tupple2 = ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10],[3,6,3,7,3])
tupple3 = ((1, 2, 3, 4, 5), (6, 7, 8, 9, 10),(3,6,3,7,3))

list1 = [1, 2, 3, 4, 5]
list2 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10],[3,6,3,7,3]]
list3 = [(1, 2, 3, 4, 5), (6, 7, 8, 9, 10),(3,6,3,7,3)]

label1 = ["ocak","şubat","mart","nisan","mayıs"]
dataset_labes = ["imagine","repeater", "upscaler"]
options = {
    "responsive": True,
    "legend_pos": "top",
    "title": "Burası Başlık",
    "backgroundColor": [
        "rgb(255, 99, 132)",
        "rgb(54, 162, 235)",
        "rgb(255, 205, 86)",
        "rgb(75, 192, 192)",
        "rgb(153, 102, 255)"
    ],
    "dataset_labels": dataset_labes,
}

charts = [tupple1,tupple2,tupple3,list1,list2,list3]
button_value =["Tuple1","Tuple2","Tuple3","List1","List2","List3"]
chart_index = 0
def update(ctx,id,value):
    global chart_index
    chart_index = int(id[-1:])
    ctx.elements["chart1"].value = charts[chart_index]

def chart_pie_example():
    with uix.elements.border().size("100%","fit-content").style("overflow-y","auto") as main:
        with row().size("100%","50px").style("gap","10px"):
            for i in range(len(button_value)):
                button(id = f"btn_0{i}", value = button_value[i]).on("click", update)
        chart_pie(id = "chart1", value=charts[chart_index], options=options, labels=label1).size("50%","50%").cls("border")

title = "Chart Pie"
description = """
# chart_bar(id, value=None, labels=None, options=None)

1. Chart Bar bir chart komponentidir.
    | attr          | desc                                                              |
    | :------------ | :---------------------------------------------------------------  |
    | id            | Komponentin id'si                                                 |
    | value         | Chart verisi                                                      |
    | labels        | Chart verilerinin label'ları (x ekseninde altta yazacaklar)       |
    | options       | Chart'ın opsiyonları                                              |
    
```python
    #options kullanım örneği:
    options = {
        "responsive" : True,    #Pencere boyutu değiştiğinde chart'ın yeniden boyutlandırılması
        "legend_pos" : "Top",   #Grafikte görünen veri kümlerinin açıklamalarının konumu(örn: 1.Dataset)
        "title" : "2024"        #Grafik başlığı
        "backgroundColor": [	#Grafikteki veri kümlerinin arkaplan rengi
        	"rgb(255, 99, 132)",
        	"rgb(54, 162, 235)",
        	"rgb(255, 205, 86)",
        	"rgb(75, 192, 192)",
        	"rgb(153, 102, 255)"
    	]
        
        }
```
```python
    #labels kullanım örneği:
    labels = ["ocak","şubat","mart","nisan","mayıs"]
    #Eğer labels parametresi verilmezse chart'ın x ekseninde 1'den başlayarak veri sayısı kadar sayılar otomatik yazılır.
```
```python
    #value kullanım örnekleri:
    #value tuple olabilir, list olabilir.
    #value = [1, 2, 3, 4, 5]
```
"""