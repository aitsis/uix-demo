from uix_components._tree_view._tree_view import title, description, sample as code 
from uix_components import tree_view
from uix.core.session import context
from uix.elements import text, div, row

data = {
    "Examples": {
        "Styles": {
            "Colors": ["Red", "Green"],
            "Shapes": ["Circle", "Square"]
        },
        "Components": ["Select", "Tree View"]
    }
 }
# label id'si ve label değeri olan bir veri yapısı
data2 = {
    "Examples": {
        "Colors": [{
            "Red": "red-id",
            "Blue": "blue-id"
        }],
        "Shapes": [{
            "Circle": "circle-id",
            "Square": "square-id"
        }]
    }
}

def select_label(ctx, id, value):
    ctx.elements["output"].value = f'Selected Value: {value}'

def open_components():
    ctx = context.session.context
    # Açık olmasını istediğiniz details elementinin id'si
    # Default olarak "details-" ile başlar
    ctx.elements["details-Components"].attrs["open"] = "True"

def tree_view_example():
    with div():
        with row().style("gap","20px"):
            tree_view(id="tree_1",data=data, callback= select_label)
            tree_view(id="tree_2",data=data2, callback= select_label)
        text("Selected Value:", id="output")
        open_components()