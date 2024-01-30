import uix
import numpy as np
from uix.elements import button,row
from uix_components import chart_pie
from uix_components._chart_pie._chart_pie import title, description, sample as code

tupple1 = (1, 2, 3, 4, 5)
tupple2 = ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10],[3,6,3,7,3])
tupple3 = ((1, 2, 3, 4, 5), (6, 7, 8, 9, 10),(3,6,3,7,3))

list1 = [1, 2, 3, 4, 5]
list2 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10],[3,6,3,7,3]]
list3 = [(1, 2, 3, 4, 5), (6, 7, 8, 9, 10),(3,6,3,7,3)]

label1 = ["ocak","şubat","mart","nisan","mayıs"]

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
    ]
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