import uix
import uix_components

from uix.elements import button, col
from uix_components import basic_imagecard

def imagecard_example():
    with col() as content:
        card = basic_imagecard(textstr="Selam", id = "myCard", imagesrc="https://picsum.photos/200/300").on("click", lambda ctx, id, value: print("Card clicked")).style("max-height","400px").style("max-width","400px")
    return content

title="Imagecard Example"

description = '''
    Imagecard example shows how to create an imagecard component.
'''

code = """
import uix
import uix_components

from uix.elements import button, col
from uix_components import basic_imagecard

def imagecard_example():
    with col() as content:
        card = basic_imagecard(textstr="Selam", id = "myCard", imagesrc="https://picsum.photos/200/300").on("click", lambda ctx, id, value: print("Card clicked")).style("max-height","400px").style("max-width","400px")
    return content
"""