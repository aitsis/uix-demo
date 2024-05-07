from uix_components._tree_view._tree_view import title, description, sample as code 
from uix_components import tree_view

data = {
    "Examples": {
        "Elements": ["Jupiter", "Saturn"], 
        "Components": ["Uranus", "Neptune"],
        "Styles": {
            "Colors": ["Red", "Green"],
            "Shapes": ["Circle", "Square"]
        }
    }
 }

def tree_view_example():
    tree_view(id="tree_view_example",data=data)