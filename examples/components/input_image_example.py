import uix
from uix.elements import page, main, col
from uix_components import input_image
from uix_components._input_image._input_image import title, description, sample as code

def input_image_example():
    with col(id="imagine-input-col").cls("border").style("width","50%") as input_image_test:
    
        input_image(id="input_image").style("height","500px")
    return input_image_test