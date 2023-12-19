import uix
import os
import importlib
from uix.elements import div, grid, container, md
from _menu import menu
examples = {}
readme = open("README.md").read()

for file_name in os.listdir("examples"):
    if file_name.endswith(".py"):
        module = importlib.import_module(f"examples.{file_name[:-3]}")
        examples[file_name[:-11]] = {"module":module,"name":module.__name__}
        

uix.html.add_css_file("uix_demo.css")

def chooseExample(ctx, id, value):
    print("Choose example", value)
    content = ctx.elements["content"]
    with content:
        getattr(examples[value]["module"], value+"_example")()
    content.update()
        


    
with div("") as page:
    with grid("",columns = "150px 600px") as main:
        main.cls("main")
        menu(chooseExample,examples.keys())
        with container("",id ="content") as content:
            content.cls("content border")
            md(readme)
            
        
uix.start(ui = page,debug=True)
