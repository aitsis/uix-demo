import uix
import os
import importlib
from threading import Timer
from uix.elements import div, grid, container, md,button,header, page, main # type: ignore
from _menu import menu
from uix.pipes import status_pipe

def get_component_from_components_folder():
    components = {}
    for file_name in os.listdir("examples/components"):
        print(file_name)
        if file_name.endswith(".py"):
            module = importlib.import_module(f"examples.components.{file_name[:-3]}")
            components[file_name[:-11]] = {
                "module":module,
                "name": module.__name__,
                "title": module.title if hasattr(module,"title") else file_name[:-11],
                "description": module.description if hasattr(module,"description") else "",
                "code": module.code if hasattr(module,"code") else ""
            }
    return components

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
components = get_component_from_components_folder()
current_list = examples
current_tab = "example_button"
current_link = "check"
uix.html.add_css_file("uix_demo.css")

def get_title(name):
    with div("", id = "title") as title:
        title.cls("title")
        md(current_list[name]["title"])

def get_description(name):
    with div("",id = "description") as description:
        description.cls("description")
        md(current_list[name]["description"])

def get_example(name):
    with container("",id = "example"):
        getattr(current_list[name]["module"], name+"_example")()

def get_code(name):
    with div("",id = "code") as code:
        code.cls("code")
        
        md(f"```python\n{current_list[name]['code']}\n```")


def update_menu_list(ctx,id , value):
    global current_list
    global current_tab
    global current_link
    ctx.elements[current_tab].add_class("btn-inactive")
    if id == "example_button":
        current_list = examples
        current_tab = id
        current_link = "check"
    else:
        current_list = components
        current_tab = id
        current_link = "imagecard"
    current_tab = id
    ctx.elements[current_tab].remove_class("btn-inactive")
    update_menu(ctx)


def update_menu(ctx):
    menu_list  = [{"title":current_list[key]["title"], "id":key}for key in current_list]
    content = ctx.elements["menu"]
    with content:
        menu(updateExample, menu_list)
    content.update()

def updateExample(ctx, id, value):
    global current_link
    print("Clicked", id, value)
    ctx.elements[current_link].add_class("btn-inactive")
    current_link = id
    ctx.elements[current_link].remove_class("btn-inactive")
    content = ctx.elements["content"]

    with content: 
            get_title(id)
            get_description(id)
            get_example(id)
            get_code(id)

    content.update()

readme = open("README.md").read()          
with page("") as page_:
    with header("").cls("demo-header"):
        button("Example", id="example_button").on("click",update_menu_list)
        button("Component", id="component_button").on("click",update_menu_list).cls("btn-inactive")
    with main("") as main_: 
        with grid("",columns = "0.5fr 3fr", rows="100%") as grid_:
            grid_.style("height","100%")
            grid_.style("width","100%")
            menu_list  = [{"title":current_list[key]["title"], "id":key}for key in current_list]
            with div("",id ="menu").cls("menu border") as menu_border:
                menu(updateExample, menu_list )
            with container("",id ="content") as content:
                content.cls("content border")
                md(readme)


uix.start(ui = page_,config = {"debug" : True, "pipes":[status_pipe()], "locales_path":"locale"})
