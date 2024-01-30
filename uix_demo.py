import uix
import os
import importlib
from threading import Timer
from uix.elements import div, grid, container, md, button, header, page, main, input # type: ignore
from _menu import menu
from uix.pipes import status_pipe

def get_info_from_folder(folder_path, folder_name):
    all_items = {}
    for file_name in sorted(os.listdir(folder_path)):
        if file_name.endswith(".py"):
            module_name = f"{folder_name}.{file_name[:-3]}"
            module = importlib.import_module(module_name)
            all_items[file_name[:-11]] = {
                "module": module,
                "name": module.__name__,
                "title": getattr(module, "title", file_name[:-11]),
                "description": getattr(module, "description", ""),
                "code": getattr(module, "code", "")
            }
    return all_items

examples = get_info_from_folder("examples", "examples")
components = get_info_from_folder("examples/components", "examples.components")
current_list = examples
current_tab = "example_button"
current_link = next(iter(current_list))

uix.html.add_css_file("uix_demo.css")

def get_description(name):
    with div("",id = "description") as description:
        description.cls("description")
        md(current_list[name]["description"])

def get_example(name):
    with div("",id = "example").cls("example").size("100%", "max-content"):
        getattr(current_list[name]["module"], name+"_example")()

def get_code(name):
    with div("",id = "code") as code:
        code.cls("code")
        md(f"```python\n{current_list[name]['code']}\n```")

def update_menu_list(ctx, id, value):
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
    update_menu(ctx, current_list)

def update_menu(ctx, menu_list = current_list):
    global current_link
    current_link = next(iter(menu_list))
    menu_list = [{"title": menu_list[key]["title"], "id": key} for key in menu_list]
    content = ctx.elements["menu"]
    with content:
        menu(updateExample, menu_list)
    content.update()

def updateMenuList(ctx, id, value):
    filtered_dict = {key: item for key, item in current_list.items() if value.lower() in item["title"].lower()}
    update_menu(ctx, filtered_dict)

def updateExample(ctx, id, value):
    global current_link
    print("Clicked", id, value)
    ctx.elements[current_link].add_class("btn-inactive")
    current_link = id
    ctx.elements[current_link].remove_class("btn-inactive")
    content = ctx.elements["content"]
    with content:
        with div("", id="example_container").style("width: 100%;"):
            div(value).cls("title")
            get_description(id)
            get_example(id)
        get_code(id)
    
    content.update()

readme = open("README.md").read()

with page("") as page_:
    with header("").cls("demo-header"):
        button("Example", id="example_button").on("click", update_menu_list)
        button("Component", id="component_button").on("click", update_menu_list).cls("btn-inactive")
    with main("") as main_:
        with grid("", columns="0.5fr 3fr", rows="100%") as grid_:
            grid_.style("height", "100%")
            grid_.style("width", "100%")
            menu_list = [{"title": current_list[key]["title"], "id": key} for key in current_list]
            with div("").style("height: calc(100% - 2.2rem);"):
                input("", placeholder="Filtrele" ,id="filtre").on("input", updateMenuList).cls("filter-input")
                with div("", id="menu").cls("menu border") as menu_border:
                    menu(updateExample, menu_list)
            with container("", id="content") as content:

                content.cls("content border")
                md(readme)

uix.start(ui = page_,config = {"debug" : True, "pipes":[status_pipe()], "locales_path":"locale"})
