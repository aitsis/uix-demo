from uix.elements import listitem, orderedlist

def orderedlist_listitem_example():
    with orderedlist(id="myList") as main:
        listitem(value="Item 1")   
        listitem(value="Item 2")        
        listitem(value="Item 3")
    return main