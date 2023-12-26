import uix
import os
import importlib
from threading import Timer
from uix.elements import div, grid, container, md # type: ignore
from _menu import menu
from uix.pipes import status_pipe

readme = open("README.md").read()
def get_examples_from_examples_folder():
    examples = {}
    for file_name in os.listdir("examples"):
        if file_name.endswith(".py"):
            module = importlib.import_module(f"examples.{file_name[:-3]}")
            examples[file_name[:-11]] = {"module":module,"name":module.__name__}
    return examples
            
examples = get_examples_from_examples_folder()

uix.html.add_css_file("uix_demo.css")

def get_example(name):
    return getattr(examples[name]["module"], name+"_example")()

def updateExample(ctx, id, value):
    content = ctx.elements["content"]
    with content:
        get_example(value)
    content.update()
            
with div("") as page:
    with grid("",columns = "150px 600px") as main:
        main.cls("main")
        menu(updateExample,examples.keys())
        with container("",id ="content") as content:
            content.cls("content border")
            md(readme)
            

uix.start(ui = page,config = {"debug" : True, "pipes":[status_pipe()], "locales_path":"locale"})
