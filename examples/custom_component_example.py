from uix.elements import div, button, grid
from examples.components.example_component import comp_example
def custom_component_example():
    main = comp_example("Hello World!").style("font-size","30px")
    return main