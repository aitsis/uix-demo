from uix.elements import button, col
from uix_components import basic_loading

def loading_example():
    with col() as content:
        loading = basic_loading(id = "myLoading", timer = 5).style("height","400px")
        button("Start Loading", id = "show_loading").on("click", lambda ctx, id, value : loading.start())
        button("Stop Loading", id = "hide_loading").on("click", lambda ctx, id, value : loading.stop())
    return content

title="Loading Example"

description = '''
## basic_loading(id, timer)
1. Temel loading elementi.
2. Timer parametresi ile loading süresi belirlenebilir. Varsayılan değeri 10 saniyedir.
3. Start ve stop metotları ile loading başlatılıp durdurulabilir.

| attr          | desc                                            |
| :------------ | :-----------------------------------------------|
| id            | Loading elementinin id'si                       |
| timer         | Loading süresi (saniye)                         |
'''

code = """
from uix.elements import button, col
from uix_components import basic_loading

def loading_example():
    with col() as content:
        loading = basic_loading(id = "myLoading", timer = 5).style("height","400px")
        button("Start Loading", id = "show_loading").on("click", lambda ctx, id, value : loading.start())
        button("Stop Loading", id = "hide_loading").on("click", lambda ctx, id, value : loading.stop())
    return content
"""

