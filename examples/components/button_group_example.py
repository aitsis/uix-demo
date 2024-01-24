from uix_components._button_group._button_group import title, description, sample as code
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