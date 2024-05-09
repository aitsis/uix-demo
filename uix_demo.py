from uix.elements import link, button, main, div, input, md, row, col, text
from uix_components import tree_view
from uix.core.session import context
import importlib
import uix
import os
import pandas as pd
uix.html.add_css_file("uix_demo.css", __file__)

def get_info_from_folder(folder_path, folder_name):
    global df, all_items
    all_items = {}
    df = pd.DataFrame()
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
                "example_name": file_name[:-11] 
            }

    return all_items

examples = get_info_from_folder("examples", "examples")
components = get_info_from_folder("examples/components", "examples.components")
all_items = {**examples, **components}
df = pd.DataFrame(all_items).transpose() 
print(df)
df.to_csv(os.path.join("examples", "data.csv"), index=False)  

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
def advanced_search(value):
    result_df = df[(df['code'].str.contains(value, case=False, regex=False)) | 
        (df['example_name'].str.contains(value, case=False, regex=False))] 
    print(result_df)
    if result_df.empty:
        return None
    else:
        results = []
        for index, row in result_df.iterrows():

            code_lines = row['code'].splitlines()
            for line_num, line in enumerate(code_lines):
                if value.lower() in line.lower():
                    results.append({
                    "title": row['title'],
                    "code_line": line,
                    "line_number": line_num + 1,
                    "module": row['module'],
                    "name": row['name'],
                    "example_name": row['example_name']
                    })
         
        return results


def advanced_search_content(results):
    with div(id="search-content").cls("area-content"):
        if results is None:
            text("No results found.").style("font-size: large") 
        else:
            for result in results:
                example_name = result["name"].split(".")[1].split("_")[0]
                example_type = result["name"].split(".")[0]
                with div().cls("result-div"): 
                    with link("",href=f"/{example_type}/{example_name}"):
                        with col():
                            text(result["example_name"])
                            text(result["code_line"])

def update(ctx, id, value):
    with ctx.elements["advanced-search"]:
            search_results = advanced_search(value)
            advanced_search_content(search_results)
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
    if filter_str != "":
        ctx.elements["filtre"].value = filter_str

def open_search_area(ctx, id, value):
    ctx.elements["search-area"].toggle_class("hidden")

def _root():
    route_checker()
    with row():
        with col().cls("sidebar border"):
            input(id="filtre", placeholder="Filtrele", type="search").cls("search-input").on("input", filter_menu).style("width: 100%;")
            last_input_value()
            with div(id="menu-content").cls("menu"):
                menu()
        with col().cls("main-content"):
            with row().style("height: 10%; justify-content: end; position: relative; justify-content: center;"):
                input_ = input(id="advanced-search", placeholder="Advanced Search", type="search", autocomplete= False).cls("search-input")
                input_.on("input", update).on("click", open_search_area)
                with div(id="search-area").cls("border hidden area"):
                    with div(id="search-content").cls("area-content"):
                        pass

            row().style("height: 2px; background-color: var(--border-color)")
            with main():       
                if len(context.session.paths) > 1:
                    with div().cls("example-content"):
                        render_content()
    

uix.start(ui = _root, config = {"debug":True})