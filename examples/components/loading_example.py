import uix
import uix_components

from uix.elements import button, col
from uix_components import basic_loading

def loading_example():
    with col() as content:
        loading = basic_loading(id = "myLoading").style("height","400px")
        button("Start Loading", id = "show_loading").on("click", lambda ctx, id, value : loading.start())
        button("Stop Loading", id = "hide_loading").on("click", lambda ctx, id, value : loading.stop())
    return content

title="Loading Example"

description = '''
    Loading example shows how to create a loading component.
'''

code = """
import uix
import uix_components

from uix.elements import button, col
from uix_components import basic_loading

def loading_example():
    with col() as content:
        loading = basic_loading(id = "myLoading").style("height","400px")
        button("Start Loading", id = "show_loading").on("click", lambda ctx, id, value : loading.start())
        button("Stop Loading", id = "hide_loading").on("click", lambda ctx, id, value : loading.stop())
    return content
"""

