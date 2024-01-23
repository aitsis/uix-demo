from uix_components._custom_button_section._custom_button_section import title, description, sample as code
from uix_components import custom_button_section
from uix.elements import text

def icon_func1(ctx, id, value):
    ctx.elements["text1"].value = "icon_func1"

def icon_func2(ctx, id, value):
    ctx.elements["text1"].value = "icon_func2"

items = {
    "icon1": {
        "icon": "fa-solid fa-trash",
        "onClick": icon_func1,
        "row_styles": {"width": "min-content"},
        "icon_styles": {"font-size": "30px", "color": "red"},
        "btn_styles": {},
    },
    "icon2": {
        "icon": "fa-sharp fa-solid fa-circle-info",
        "onClick": icon_func2,
    },
    "icon3": {
        "icon": "fa-solid fa-download",
        "onClick": icon_func2,
    }
}

def custom_button_section_example():
    custom_button_section(items=items,id="custom-button-section-1")
    text("",id="text1",)