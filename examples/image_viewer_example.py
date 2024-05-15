import random
from uix_components import image_viewer
from uix.elements import file, row, button,div

buttonGroup= {
    "Zoom in": {
        "icon": "fa-search-plus",
        "icon_styles": {"font-size": "20px", "color": "var(--ait)"},
    },
    "Zoom out": {
        "icon": "fa-search-minus",
        "icon_styles": {"font-size": "20px", "color": "var(--ait)"},
    },
    "Home": {
        "icon": "fa-home",
        "icon_styles": {"font-size": "20px", "color": "var(--ait)"},
    },
    "Full screen": {
        "icon": "fa-expand",
        "icon_styles": {"font-size": "20px", "color": "var(--ait)"},
    },
    "Download": {
        "icon": "fa-download",
        "icon_styles": {"font-size": "20px", "color": "var(--ait)"},
    }
}

def on_button_pil_image_click(ctx, id, value):
    pil_image = create_image()
    iw = ctx.session.elements["iw1"]
    iw.value = pil_image


def on_upload(ctx, id, event, data, status):
    print("on_upload", id, event, data, status)
    if status == "done":
        iw = ctx.session.elements["iw1"]
        if event == "select":
            iw.value = data[0].url
        
def image_viewer_example():      
    with div() as main:
        with row():
            file(id="file1",accept="image/*",multiple=False,callback=on_upload).cls("center")
            button("Show PIL Image",id="show_pil_image").on("click",on_button_pil_image_click)
        image_viewer(id = "iw1", value="https://ai.ait.com.tr/wp-content/uploads/AIT_AI_LOGO.png",buttonGroup=buttonGroup).size(400,400)
    return main

from PIL import Image, ImageDraw, ImageFilter
def create_image():
    def random_color():
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def gradient_circle(draw, center, radius, color1, color2):
        for i in range(radius, 0, -1):
            color = (
                int(color1[0] + (color2[0] - color1[0]) * i / radius),
                int(color1[1] + (color2[1] - color1[1]) * i / radius),
                int(color1[2] + (color2[2] - color1[2]) * i / radius)
            )
            draw.ellipse((center[0] - i, center[1] - i, center[0] + i, center[1] + i), fill=color)

    img_size = 400
    image = Image.new("RGB", (img_size, img_size), "white")
    draw = ImageDraw.Draw(image)

    # Draw a grid of gradient circles
    spacing = 80  # Space between centers of circles
    radius = 40
    for x in range(spacing, img_size, spacing):
        for y in range(spacing, img_size, spacing):
            gradient_circle(draw, (x, y), radius, random_color(), random_color())

    # Apply a slight blur to smooth out the gradients
    image = image.filter(ImageFilter.GaussianBlur(2))
    return image

title = "Image Viewer"
description = """
## image_viewer(id: str, value: str, buttonGroup: dict, zoom: bool, size: tuple)
1. Verilen resmi gösteren bir image viewer oluşturur.

| attr                  | desc                                                                |
| :-------------------- | :------------------------------------------------                   |
| id                    | image_viewer elementinin id'si                                      |
| value                 | image_viewer elementinin göstereceği image url'si veya Image objesi |
| buttonGroup           | image_viewer elementinin sağ üst köşesindeki buton grubu            |
| zoom                  | image_viewer elementinin zoom yapılmasını sağlar.                   |
| size                  | image_viewer elementinin boyutu. (width, height)                    |
"""