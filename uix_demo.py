from uix.elements import link, main, div, input, md, row, col, text 
from uix_components import tree_view
from uix.core.session import context
import pandas as pd
import importlib
import uix
import os
import re
uix.html.add_css_file("uix_demo.css", __file__)

def remove_underscore(key):
    return re.sub(r'_', ' ', key).title() 

def get_info_from_folder(folder_path, folder_name, type):
    global all_items
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
                "code": getattr(module, "code", ""),
                "example_title": remove_underscore(file_name[:-11]),
                "example_name": file_name[:-11],
                "example_type": type
            }

    return all_items

examples = get_info_from_folder("examples", "examples", "examples")
components = get_info_from_folder("examples/components", "examples.components", "components")
all_items = {**examples, **components}
df = pd.DataFrame(all_items).transpose() 

tree_view_items = {
    "Examples": {
        "Elements": [],
        "Components": []
    }
}
for key in examples.keys():
    tree_view_items["Examples"]["Elements"].append({remove_underscore(key) : key })
for key in components.keys():
    tree_view_items["Examples"]["Components"].append({remove_underscore(key) : key })

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

def advanced_search(value):
    result_code_df = df[df['code'].str.contains(value, case=False, regex=False)] 
    result_title_df = df[df['example_name'].str.contains(value, case=False, regex=False)]
    code_results = []
    title_results = []

    if result_code_df.empty and result_title_df.empty:
        return title_results, code_results  
    else:
        for index, row in result_title_df.iterrows():
            title_results.append({
                "example_title": row['example_title'],
                "example_type": row['example_type'],
                "example_name": row['example_name']
            })
        for index, row in result_code_df.iterrows():
            code_lines = row['code'].splitlines()
            for line_num, line in enumerate(code_lines):
                if value.lower() in line.lower():
                    title_results.append({
                    "code_line": line,
                    "example_title": row['example_title'],
                    "example_type": row['example_type'],
                    "example_name": row['example_name']
                    })
         
        return title_results, code_results


def advanced_search_content(title_results, code_results):
    with div(id="search-content").cls("area-content"):
        if not (title_results or code_results):
            text("No results found.").style("font-size: large") 
        else:
            for result in title_results + code_results:
                with div().cls("search-div"):
                    with link("",href=f"/{result['example_type']}/{result['example_name']}").cls("search-link"):
                        with col():
                            text(result["example_title"]).style("font-size: large")
                            if result.get("code_line"):
                                text(result["code_line"]).cls("code-line")

def update_search_area(ctx, id, value):
    with ctx.elements["advanced-search"]:
        title_results, code_results = advanced_search(value)
        advanced_search_content(title_results, code_results)
    ctx.elements["search-content"].update()

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
    if id in examples.keys():
        context.session.navigate(f"/examples/{id}")
    elif id in components.keys():
        context.session.navigate(f"/components/{id}")
    else:
        print("Not found")
    
 
def menu():
    global filter_str
    with div() as menu:
        tree_view(id="tree",data=tree_view_items, callback= select_label, selected= current_path[1] if len(current_path[1]) > 1 else None)
        if len(context.session.paths) > 1:
            if context.session.paths[0] == "examples":
                ctx.elements["details-Elements"].attrs["open"] = "True"
            elif context.session.paths[0] == "components":
                ctx.elements["details-Components"].attrs["open"] = "True"
    return menu


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


def open_search_area(ctx, id, value):
    ctx.elements["search-area"].toggle_class("hidden")

def _root():
    route_checker()
    with row():
        with col().cls("sidebar border"):
            with div(id="menu-content").cls("menu"):
                menu()
        with col().cls("main-content"):
            with row().style("height: 10%; justify-content: end; position: relative; justify-content: center;"):
                input_ = input(id="advanced-search", placeholder="Advanced Search", type="search", autocomplete= False).cls("search-input")
                input_.on("input", update_search_area).on("click", open_search_area)
                with div(id="search-area").cls("border hidden area"):
                    with div(id="search-content").cls("area-content"):
                        text("Search examples by title or code")

            row().style("height: 2px; background-color: var(--border-color)")
            with main():       
                if len(context.session.paths) > 1:
                    with div().cls("example-content"):
                        render_content()
    

uix.start(ui = _root, config = {"debug":True})