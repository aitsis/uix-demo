from uix.elements import border, button
from uix.elements._border import title, description, sample as code
example_button = ["A!", "B!", "C!", "D!"]

def border_example():
    for i in range(len(example_button)):
        with border("",) as border_demo:
            button(example_button[i])
    return border_demo
