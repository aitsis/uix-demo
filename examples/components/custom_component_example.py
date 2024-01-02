from uix.elements import div, button, grid
from examples.components.component_example import component_example

def custom_component_example():
    main = component_example("Hello World!").style("font-size","30px")
    return main

title="Custom Example"
description = '''
    Custom component example shows how to create a custom component.
'''
sample = """
    Custom Component Example
"""