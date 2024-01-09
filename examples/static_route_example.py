import os
import uix
from uix.elements import image
path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")
uix.app.add_static_route("my_images",path)

def static_route_example():
    root = image("my_images/open.svg").size(100,100) 
    return root

title = "Static Route Example"