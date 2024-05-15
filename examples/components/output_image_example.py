from uix.elements import col
from uix_components import output_image

def output_image_example():
    with col(id="title").cls("description").style("width","50%") as output_image_test:
        output_image(id="description").style("height","500px")
    return output_image_test

title = "Output Image"
description = """
## output_image(value=None, id=None, viewer="seadragon",callback=None, add_to_favorite=None)

1- Resim göstermek için kullanılır.

| attr                  | desc                                                     |
| :-------------------- | :----------------------------------------------------    |
| viewer                | Resim gösterme türü. "seadragon" veya "fabric" olabilir. |
| setinputImage         | Resmi input_image kısmına göndermek için kullanılır.     |
| add_to_favorite       | Resmi favorilere eklemek için kullanılır.                |
"""