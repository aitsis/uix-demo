from uix import Element
from uix.elements import div,button
print("Imported: comp_examples")

# Example 1: Using the Element class --------------------------------------------
class comp_example1(Element):
    def __init__(self,value = None,id = None):
        super().__init__(value, id = id)
        self.enter()
        button(self.value + "Click me 1").on("click",self.click)
        button(self.value + "Click me 2").on("click",self.click)
        self.exit()

    def click(self,id,value,event):
        print("Clicked. id = ",id," value = ",value," event = ",event)
        
# Example 2: Using the with statement --------------------------------------------
class comp_example2(Element):
    def __init__(self,value = None,id = None):
        super().__init__(value, id = id)
        with self:
            button(self.value + "Click me 1").on("click",self.click)
            button(self.value + "Click me 2").on("click",self.click)

    def click(self,id,value,event):
        print("Clicked. id = ",id," value = ",value," event = ",event)
 

# Example 3: Using the with statement and a function ----------------------------

def click(id,value,event):
    print("Clicked. id = ",id," value = ",value," event = ",event)

def comp_example3(value):
    with div("Hello World!") as main:
        button(value + "Click me 1").on("click",click)
        button(value + "Click me 2").on("click",click)
    return main

# -------------------------------------------------------------------------------        
def comp_example(value):
    with div() as main:
        comp_example1(value)
        comp_example2(value)
        comp_example3(value)
    return main