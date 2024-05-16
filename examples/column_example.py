from uix.elements import border, col, div

def column_example():
    with border(""):
        with col(""):
            div("Column 1")
            div("Column 1")
    with border(""):
        with col(""):
            div("Column 2")
            div("Column 2")
            
title = "Column"
description = '''
## col(value,id = None)
1. Temel column elementi.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Column elementinin id'si                         |
| value         | Column elementinin içeriği                      |
'''