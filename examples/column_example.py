from uix.elements import border, col, div

def column_example():
    with border("").style("padding","10px"):
        with col(""):
            div("Column 1")
            div("Column 1")
    with border("").style("padding","10px"):    
        with col(""):
            div("Column 2")
            div("Column 2")