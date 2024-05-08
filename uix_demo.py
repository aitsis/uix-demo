from uix.elements import link, button, icon, main, div, input, md, row, col
from uix_components import tree_view
from uix.core.session import context
import importlib
import uix
import os
uix.html.add_css_file("uix_demo.css", __file__)

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

data = {
    "Examples": {
        "Elements": list(examples.keys()),
        "Components": list(components.keys()),
    }
}

lists = [
    {
        "title": "examples",
        "list": examples
    },
    {
        "title": "components",
        "list": components
    }
]

filter_str = ""

def render_content():
    current_list = get_current_list()
    if current_list:
        for item_name, item_data in current_list["list"].items():
            if context.session.paths[1] == item_name:
                md(item_data["description"]) 
                with div().cls("example-center"): 
                    getattr(item_data["module"], item_name + "_example")()  
                md(f"```python\n{item_data['code']}\n```").cls("example-center")

def get_current_list():
    for list_item in lists:
        if context.session.paths[0] == list_item["title"]: 
            return list_item
    return None

def select_label(ctx, id, value):
    if value in data["Examples"]["Elements"]:
        context.session.navigate(f'/examples/{value}')
    else:
        context.session.navigate(f'/components/{value}')

def current_selected_tree():
    global current_tree_title
    if len(context.session.paths) > 1:
        if context.session.paths[0] == "examples":
            ctx.elements["details-Elements"].attrs["open"] = "True"
        elif context.session.paths[0] == "components":
            ctx.elements["details-Components"].attrs["open"] = "True"
            
def menu():
    global filter_str
    with div() as menu:
        tree= tree_view(id="tree",data=data, callback= select_label, selected = current_path[1] if len(current_path[1]) > 1 else None)
        current_selected_tree()
        
        if filter_str != "":
            tree.style("display", "none")
            for list_item in lists:
                for item in list_item["list"]:
                    if filter_str.lower() in item.lower():
                        link(id=f'{item}"-label"', value = item, href=f"/{list_item['title']}/{item}").cls("btn btn-inactive menu-item").style("text-decoration", "none").style("color", "var(--font-color)")
                        if len(context.session.paths) > 1 and context.session.paths[1] == item:
                            ctx.elements[f'{item}"-label"'].set_style("background-color","var(--ait)")      
    return menu

def filter_menu(ctx, id, value):
    global filter_str
    filter_str = value
    ctx.elements["menu-content"].update(menu)

def route_checker():
    global current_path, ctx
    if context.session.paths[0] == '' and len(context.session.paths) == 1:
        context.session.navigate(f'/{lists[0]["title"]}')
    for list_item in lists:
        if context.session.paths[0] == list_item["title"]:
            if len(context.session.paths) > 1:
                if context.session.paths[1] not in list_item["list"]:
                    context.session.navigate(f'/{list_item["title"]}/{next(iter(list_item["list"]))}')
            else:
                context.session.navigate(f'/{list_item["title"]}/{next(iter(list_item["list"]))}')
    current_path = context.session.paths
    ctx = context.session.context


def last_input_value():
    if filter_str is not "":
        ctx.elements["filtre"].value = filter_str

def _root():
    route_checker()
    with row():
        with col().cls("sidebar border"):
            input(id="filtre", placeholder="Filtrele", type="search").cls("search-input").on("input", filter_menu)
            last_input_value()
            with div(id="menu-content").cls("menu"):
                menu()
        with col().cls("main-content"):
            with row().style("height: 10%; justify-content: end;"):
                    with button(""):
                        icon("fa-solid fa-filter")
            row().style("height: 2px; background-color: var(--border-color)")
            with main():       
                if len(context.session.paths) > 1:
                    with div().cls("example-content"):
                        render_content()
    

uix.start(ui = _root, config = {"debug":True})