from uix.elements import div
from uix_components import basic_tree_view
from uix_components._basic_tree_view._basic_tree_view import title, description, sample as code


data = {
    "Tree View": {
    "key1": "value1",
    "key2": "value2",
    "key3": {
        "key4": "value4",
        "key5": "value5",
        "key6": {
            "key7": "value7",
            "key8": "value8",
            "key9": "value9",
        }
    }
}
}

def basic_tree_example():
    with div() as basic_tree_view_example:
        basic_tree_view(id="basic_tree_view_example",data=data)
    return basic_tree_view_example