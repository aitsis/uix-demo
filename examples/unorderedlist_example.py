from uix.elements import listitem, unorderedlist
from uix.elements._unorderedlist import title, description, sample as code


def unorderedlist_example():
    with unorderedlist("").style("margin","auto").style("display","block"):
        listitem("Item 1")
        listitem("Item 2")
        listitem("Item 3")
