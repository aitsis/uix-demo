import uix
import os
import importlib
from threading import Timer
from uix.elements import div, grid, container, md,text # type: ignore
from _menu import menu
from uix.pipes import status_pipe

# import examples.hello_world_example

# from examples.hello_world_example import hello_world_example

def get_examples_from_examples_folder():
    examples = {}
    for file_name in os.listdir("examples"):
        if file_name.endswith(".py"):
            module = importlib.import_module(f"examples.{file_name[:-3]}")
            examples[file_name[:-11]] = {
                "module":module,
                "name": module.__name__,
                "title": module.title if hasattr(module,"title") else file_name[:-11],
                "description": module.description if hasattr(module,"description") else "",
                "code": module.code if hasattr(module,"code") else ""}
    return examples
            
examples = get_examples_from_examples_folder()

uix.html.add_css_file("uix_demo.css")

def get_example(name):
    return getattr(examples[name]["module"], name+"_example")()

def updateExample(ctx, id, value):
    print("Clicked", id, value)
    
    content = ctx.elements["content"]
    with content:
        get_example(id)
    content.update()

readme = open("README.md").read()          
with div("") as page:
    with div("Header",id = "header") as header:
        header.cls("header example_header")
    with grid("",columns = "150px 600px") as main:
        main.cls("main")
        menu_list  = [{"title":examples[key]["title"], "id":key}for key in examples]
        menu(updateExample, menu_list )
        with container("",id ="content") as content:
            content.cls("content border")
            md(readme)
            

uix.start(ui = page,config = {"debug" : True, "pipes":[status_pipe()], "locales_path":"locale"})
