from uix.elements import col
from uix_components import basic_imagecard

def imagecard_example():
    with col() as content:
        basic_imagecard(textstr="Selam", id = "myCard", imagesrc="https://picsum.photos/200/300")
    return content

title="Imagecard Example"
description = '''
    Imagecard example shows how to create an imagecard component.
'''