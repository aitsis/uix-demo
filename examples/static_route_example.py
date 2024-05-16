import os
import uix
from uix.elements import image
path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")
uix.app.add_static_route("my_images",path)

def static_route_example():
    root = image("my_images/open.svg").size(100,100) 
    return root

title = "Static Route"
description = '''
## add_static_route(route,path)
1. Uygulamanın statik dosyalarına erişmek için kullanılır.
2. route: Erişim yolunu belirler.
3. path: Erişim yolunun nereden erişileceğini belirler.
'''