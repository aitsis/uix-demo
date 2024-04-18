import uix
import numpy as np
from uix.elements import button,row
from uix_components import chart_line
from uix_components._chart_line._chart_line import title, description, sample as code

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
list4 = np.random.randint(0,100,100).tolist()

label1 = ["ocak","şubat","mart","nisan","mayıs","haziran","temmuz","ağustos","eylül","ekim","kasım","aralık"]

dataset_labes = ["imagine","repeater", "upscaler"]
dataset_border_colors = ['rgba(255, 99, 132, 1)','rgba(255, 159, 64, 1)','rgba(54, 162, 235, 1)']

options = {
    "responsive": True,
    "legend_pos": "top",
    "title": "Burası Başlık",
    "tension": 0.2,
    "dataset_labels": dataset_labes,
    "dataset_border_colors": dataset_border_colors,
}

charts = [dict1,dict2,tupple1,tupple2,tupple3,list1,list2,list3,list4]
button_value =["Dict1","Dict2","Tuple1","Tuple2","Tuple3","List1","List2","List3","List4"]
chart_index = 0 
def update(ctx,id,value):
    global chart_index
    chart_index = int(id[-1:])
    ctx.elements["chart1"].value = charts[chart_index]

def chart_line_example():
    with uix.elements.border().size("100%","fit-content").style("overflow-y","auto") as main:
        with row().size("100%","50px").style("gap","10px"):
            for i in range(len(button_value)):
                button(id = f"btn_0{i}", value = button_value[i]).on("click", update)
        chart_line(id = "chart1", value=charts[chart_index], options=options).size("90%","90%").cls("border")