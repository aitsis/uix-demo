from uix.elements import border, col, div
from uix.elements._col import title, description, sample as code

def column_example():
    with border(""):
        with col(""):
            div("Column 1")
            div("Column 1")
    with border(""):
        with col(""):
            div("Column 2")
            div("Column 2")