import uix
import uix_components

from uix.elements import div,col, button
from uix_components import basic_slider, basic_details

from uix_components._basic_details._basic_details import title, description, sample as code 

def acc_elements_example():
    with col() as col1:
        col1.cls("border")
        basic_slider(name="Deneme1", id = "mySlider1", callback = lambda ctx, id, value: print(f"Slider {id} changed to: {value}")).size("100%","max-content")
        basic_slider(name="Deneme2", id = "mySlider2",callback=lambda ctx, id, value: print(f"Slider {id} changed to: {value}")).size("100%","max-content")
        basic_slider(name="Deneme3", id = "mySlider3",callback=lambda ctx, id, value: print(f"Slider {id} changed to: {value}")).size("100%","max-content")
        button("Button 1")
def basic_details_example():
    with div() as details:
        details.size("50%","max-content")
        basic_details("",id = "myDetails",label_="Accordion Example", acc_elements = [acc_elements_example] )
    return details     


