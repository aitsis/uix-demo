from uix_components import button_group
from uix.elements import text, col

def icon_func1(ctx, id, value):
    ctx.elements["text1"].value = "icon_func1"

def icon_func2(ctx, id, value):
    ctx.elements["text1"].value = "icon_func2"

icon_btn_group = {
    "icon-btn-1": {
        "icon": "fa-solid fa-trash",
        "onClick": icon_func1,
        "row_styles": {"width": "min-content"},
        "icon_styles": {"font-size": "20px", "color": "red"},
        "btn_styles": {},
    },
    "icon-btn-2": {
        "icon": "fa-sharp fa-solid fa-circle-info",
        "onClick": icon_func2,
    },
    "icon-btn-3": {
        "icon": "fa-solid fa-download",
        "onClick": icon_func2,
    }
}

text_btn_group = {
    "text-btn-1": {
        "text": "Download",
        "onClick": icon_func1,
        "row_styles": {"background-color": "white"},
        "btn_styles": {"background-color": "black"},
        "icon": "fa-solid fa-download",
    },
    "text-btn-2": {
        "text": "Button 2",
        "onClick": icon_func2,
        "btn_styles": {"background-color": "black"},
    },
    "text-btn-3": {
        "text": "Button 3",
        "onClick": icon_func2,
        "btn_styles": {"background-color": "black"},
        "text_styles": {"color": "red"},
    }
}

def button_group_example():
    with col().style("gap","5px"): 
        button_group(items=icon_btn_group,id="custom-button-section-1")
        button_group(items=text_btn_group,id="custom-button-section-2")
        text("",id="text1")

title = "Button Group"
description = """
 # button_section(id, items)
 1. Button Section bir button komponentidir. Style'lar dict, class'lar string olarak verilir.
    | attr          | desc                                                            |
    | :------------ | :-----------------------------------------------------          |
    | id            | Komponentin id'si                                               |
    | items         | Komponentin içindeki iconların dict olarak verilmesi gerekiyor. |
    | onClick       | Komponentin değeri değiştiğinde çalışacak fonksiyon             |
    | row_classes   | Komponentin içine row class tanımlamak için kullanılır.         |
    | row_styles    | Komponentin içine row style tanımlamak için kullanılır.         |
    | icon_styles   | Komponentin içine icon style tanımlamak için kullanılır.        |
    | btn_classes   | Komponentin içine button class tanımlamak için kullanılır.      |
    | btn_styles    | Komponentin içine button style tanımlamak için kullanılır.      |
    | btn_id        | Komponentin içine button id tanımlamak için kullanılır.         |
    | text_styles   | Komponentin içine text style tanımlamak için kullanılır.        |
    | text_classes  | Komponentin içine text class tanımlamak için kullanılır.        |
"""