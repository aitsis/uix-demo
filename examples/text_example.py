from uix.elements import div, text
from uix.elements._text import title, description, sample as code

def text_example():
    value="Hello World!"
    main = text(value)
    return main