import uix
import numpy as np
from uix.elements import button,row
from uix_components import chart_bar

dict1 = {'2010':10, '2011':20, '2012':15, '2013':25, '2014':22, '2015':30, '2016':28}
dict2 = {
    'data1': {'2010':15, '2011':65, '2012':34, '2013':53, '2014':32, '2015':44, '2016':38},
    'data2':{'2010':12, '2011':41, '2012':25, '2013':16, '2014':52, '2015':32, '2016':28}
}   

tupple1 = (1, 2, 3, 4, 5)
tupple2 = ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10],[3,6,3,7,3])
tupple3 = ((1, 2, 3, 4, 5), (6, 7, 8, 9, 10),(3,6,3,7,3))

list1 = [1, 2, 3, 4, 5]
list2 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10],[3,6,3,7,3]]
list3 = [(1, 2, 3, 4, 5), (6, 7, 8, 9, 10),(3,6,3,7,3)]
list4 = np.random.randint(0,100,1000).tolist()

label1 = ["ocak","şubat","mart","nisan","mayıs","haziran","temmuz","ağustos","eylül","ekim","kasım","aralık"]

dataset_labes = ["imagine","repeater", "upscaler"]
dataset_background_colors = ['rgba(255, 99, 132, 0.2)','rgba(255, 159, 64, 0.2)','rgba(54, 162, 235, 0.2)']
dataset_border_colors = ['rgba(255, 99, 132, 1)','rgba(255, 159, 64, 1)','rgba(54, 162, 235, 1)']
dataset_hover_colors = ['rgba(255, 99, 132, 0.6)','rgba(255, 159, 64, 0.6)','rgba(54, 162, 235, 0.6)']

options = {
    "responsive": True,
    "legend_pos": "top",
    "title": "Burası Başlık",
    "dataset_labels": dataset_labes,
    "dataset_background_colors": dataset_background_colors,
    "dataset_border_colors": dataset_border_colors,
    "dataset_hover_colors": dataset_hover_colors,
    }

charts = [dict1,dict2,tupple1,tupple2,tupple3,list1,list2,list3,list4]
button_value =["Dict1","Dict2","Tuple1","Tuple2","Tuple3","List1","List2","List3","List4"]
chart_index = 0 
def update(ctx,id,value):
    global chart_index
    chart_index = int(id[-1:])
    ctx.elements["chart1"].value = charts[chart_index]

def chart_bar_example():
    with uix.elements.border().size("100%","fit-content").style("overflow-y","auto") as main:
        with row().size("100%","50px").style("gap","10px"):
            for i in range(len(button_value)):
                button(id = f"btn_0{i}", value = button_value[i]).on("click", update)
        chart_bar(id = "chart1", value=charts[chart_index], options=options).size("90%","90%").cls("border")

title = "Chart Bar"
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
        }
```
```python
    #labels kullanım örneği:
    labels = ["ocak","şubat","mart","nisan","mayıs","haziran","temmuz","ağustos","eylül","ekim","kasım","aralık"]
    #Eğer labels parametresi verilmezse chart'ın x ekseninde 1'den başlayarak veri sayısı kadar sayılar otomatik yazılır.
    #dict veri tipinde key'ler labels olarak kullanılır.
```
```python
    #value kullanım örnekleri:
    value dict olabilir, tuple olabilir, list olabilir.
    dict içinde dict olabilir.
    tuple içinde tuple veya list olabilir.
    list içinde list veya tuple olabilir.
```
"""