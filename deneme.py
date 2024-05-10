from uix_components._tree_view._tree_view import tree_view
from uix.elements import text, div
import uix

data = {
    "Examples": {
        "Colors": ["Red"],
        "Shapes": ["Circle"]
    }
}

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

def _root():
    with div() as main:
        tree_view(id="tree_view_example",data=data2)

uix.start(ui = _root, config = {"debug":True})