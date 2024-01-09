from uix_components import basic_slider
from uix_components._basic_slider._basic_slider import title, description, sample as code

def basic_slider_example():
    return basic_slider(name="Deneme", id = "mySlider", callback = lambda ctx, id, value: print(f"Slider {id} changed to: {value}"))