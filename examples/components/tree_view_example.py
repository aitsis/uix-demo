from uix_components._tree_view._tree_view import title, description, sample as code 
from uix_components import tree_view
from uix.elements import text, div

data = {
    "Examples": {
        "Styles": {
            "Colors": ["Red", "Green"],
            "Shapes": ["Circle", "Square"]
        },
        "Components": ["Select", "Tree View"]
    }
 }

def select_label(ctx, id, value):
    ctx.elements["output"].value = f'Selected Value: {value}'

def tree_view_example():
    with div().cls("gap"):
        tree_view(id="tree_view_example",data=data, callback= select_label)
        text("Selected Value:", id="output")