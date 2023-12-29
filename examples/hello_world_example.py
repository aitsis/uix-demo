from uix.elements import div, button, grid # type: ignore

def hello_world_example():
    main = div("Hello World!").style("font-size","30px")
    return main

title = "Hello World"

description = "A simple example that shows how to create a simple hello world example"

code = """
from uix.elements import div, button, grid # type: ignore

def hello_world_example():
    main = div("Hello World!").style("font-size","30px")
    return main
"""