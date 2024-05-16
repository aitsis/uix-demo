import uix
import os
from PIL import Image
from uix.elements import image, div

images_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets/squared")
print("Images path : ", images_path)
allowed_sizes = [50, 100, 150, 200, 250, 300]

def api_handler(paths, args):
    print(paths, "paths")
    if len(paths) == 2:
        return uix.send_file(f"{images_path}/{paths[1]}")
    if len(paths) == 3:
        size = int(paths[1])
        # check size folder
        if size not in allowed_sizes:
            return uix.abort(400, f"Invalid size: {size}")
        
        print("Files : ", os.listdir(images_path))
        if paths[1] not in os.listdir(images_path):
            os.mkdir(f"{images_path}/{size}")

        file_path = f"{images_path}/{size}/{paths[2]}"

        if os.path.isfile(file_path):
            return uix.send_file(file_path)
        else:
            # resize image
            image_path = f"{images_path}/{paths[2]}"
            img = Image.open(image_path)
            img = img.resize((int(size), int(size)))
            img.save(file_path)
            return uix.send_file(file_path)
            
    return uix.abort(404, "Not found")

# Register the api handler with the name "api_example" --------------------------------------

uix.register_api_handler("api_example", api_handler)

# -------------------------------------------------------------------------------------------

def api_example():
    with div("",) as api_demo:
        image("/manual_api/api_example/50/01.png")
        image("/manual_api/api_example/100/05.png")
        image("/manual_api/api_example/300/03.png")
        image("/manual_api/api_example/02.png")
    return api_demo

title="API Example"
description = '''
    API example shows how to create an api handler and use it to serve images.
'''