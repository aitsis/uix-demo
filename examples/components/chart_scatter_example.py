import uix
import random
from uix.elements import button,row
from uix_components import chart_scatter
from uix_components._chart_scatter._chart_scatter import title, description, sample as code

scatter1= [{
      'x': -10,
      'y': 0
    }, {
      'x': 0,
      'y': 10
    }, {
      'x': 10,
      'y': 5
    }, {
      'x': 0.5,
      'y': 5.5
    }]
scatter2 = [{'x': random.uniform(-20, 20), 'y': random.uniform(-20, 20)} for _ in range(100)]

options = {
    "responsive": True,
    "legend_pos": "top",
    "title": "Burası Başlık",
}

charts = [scatter1,scatter2]
button_value =["Scatter1","Scatter2"]
chart_index = 0 
def update(ctx,id,value):
    global chart_index
    chart_index = int(id[-1:])
    ctx.elements["chart1"].value = charts[chart_index]

def chart_scatter_example():
    with uix.elements.border().size("100%","fit-content").style("overflow-y","auto") as main:
        with row().size("100%","50px").style("gap","10px"):
            for i in range(len(button_value)):
                button(id = f"btn_0{i}", value = button_value[i]).on("click", update)
        chart_scatter(id = "chart1", value=charts[chart_index], options=options).size("90%","90%").cls("border")