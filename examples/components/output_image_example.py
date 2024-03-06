import uix
from uix.elements import page, main, col
from uix_components import output_image
from uix_components._output_image._output_image import title, description, sample as code


def output_image_example():

    with col(id="imagine-input-col").cls("border").style("width","50%") as output_image_test:
        output_image(id="output_image").style("height","500px")
    return output_image_test