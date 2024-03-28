import uix
from uix.elements import container, col, link, image, button, text, page, header, main, grid, div, input, md # type: ignore
from uix.core.session import context
import importlib
import os

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

uix.html.add_css_file("uix_demo.css", __file__)

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

def get_description():
    with div("", id="description"):
        current_list = get_current_list()
        if current_list:
            for item_name, item_data in current_list["list"].items():
                if context.session.paths[1] == item_name:
                    md(item_data["description"])

def get_example():
    with div("", id="example").cls("example").size("100%", "max-content"):
        current_list = get_current_list()
        if current_list:
            for item_name, item_data in current_list["list"].items():
                if context.session.paths[1] == item_name:
                    getattr(item_data["module"], item_name+"_example")()

def get_code():
    with div("", id="code"):
        current_list = get_current_list()
        if current_list:
            for item_name, item_data in current_list["list"].items():
                if context.session.paths[1] == item_name:
                    md(f"```python\n{item_data['code']}\n```")

def get_current_list():
    for list_item in lists:
        if context.session.paths[0] == list_item["title"]:
            return list_item
    return None

def menu():
    with div().style("overflow-x","hidden") as menu:
        current_list = get_current_list()
        if current_list:
            for item in current_list["list"]:
                if filter_str.lower() in item.lower():
                    if len(context.session.paths) > 1 and context.session.paths[1] == item:
                            link(item, href=f"/{current_list['title']}/{item}").cls("btn btn-active menu-item").style("text-decoration", "none").style("color", "var(--font-color)")
                    else:
                            link(item, href=f"/{current_list['title']}/{item}").cls("btn btn-inactive menu-item").style("text-decoration", "none").style("color", "var(--font-color)")
    return menu

def filter_menu(ctx, id, value):
    global filter_str
    filter_str = value
    print(value)
    ctx.elements["filtre_result"].update(menu)

def route_checker():
    if context.session.paths[0] == '' and len(context.session.paths) == 1:
        context.session.navigate(f'/{lists[0]["title"]}')
    for list_item in lists:
        if context.session.paths[0] == list_item["title"]:
            if len(context.session.paths) > 1:
                if context.session.paths[1] not in list_item["list"]:
                    context.session.navigate(f'/{list_item["title"]}/{next(iter(list_item["list"]))}')
            else:
                context.session.navigate(f'/{list_item["title"]}/{next(iter(list_item["list"]))}')

def _root():
    route_checker()
    with page("") as page_:
        with header("").cls("demo-header"):
            for list_item in lists:
                if context.session.paths[0] == list_item["title"]:
                        link(list_item["title"], href=f"/{list_item['title']}").cls("btn").style("text-decoration", "none").style("color", "var(--font-color)")
                else:
                        link(list_item["title"], href=f"/{list_item['title']}").cls("btn btn-inactive").style("text-decoration", "none").style("color", "var(--font-color)")
        
        with main("") as main_:
            with grid("", columns="0.5fr 3fr", rows="100%") as grid_:
                grid_.style("height", "100%")
                grid_.style("width", "100%")
                with div("").style("height: calc(100% - 2.2rem);"):
                    input("", placeholder="Filtrele" ,id="filtre").cls("filter-input").on("input", filter_menu)
                    with div(id="filtre_result").cls("menu border"):
                        menu()
                        
                with container("", id="content").cls("content") as content:
                    if len(context.session.paths) > 1:
                        with div("", id="example_container").style("width: 100%;"):
                            get_description()
                            get_example()
                        get_code()
    return page_

uix.start(ui = _root, config = {"debug":True})