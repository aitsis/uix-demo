from uix import Element
from uix.elements import div,button
print("Imported: comp_example")
class comp_example(Element):
    def __init__(self,value = None,id = None):
        super().__init__(value, id = id)
        self.enter()
        with div() as self.div:
            button(self.value + "Click me 1").on("click",self.click)
            button(self.value + "Click me 2").on("click",self.click)
        self.exit()

    def click(self,id,value,event):
        print("Clicked. id = ",id," value = ",value," event = ",event)
        