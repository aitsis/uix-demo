from uix.elements import border, col, div
from uix.elements._col import title, description, sample as code

def column_example():
    with border("").style("padding","10px"):
        with col("").style("text-align","center"):
            div("Column 1")
            div("Column 1")
    with border("").style("padding","10px"):    
        with col("").style("text-align","center"):
            div("Column 2")
            div("Column 2")