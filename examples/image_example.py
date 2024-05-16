from uix.elements import image, col, text

def image_example():
    image_url = "https://ai.ait.com.tr/wp-content/uploads/AIT_AI_LOGO.png"
    pil_image = create_image()
    with col().style("align-items: center;") as main:
        text("Static Image")
        main = image(image_url).cls("image")
        text("PIL Image")
        main = image(pil_image).cls("image")    
    return main


from PIL import Image, ImageDraw, ImageFilter
def create_image():
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
            gradient_circle(draw, (x, y), radius, (255, 0, 0), (255, 255, 0))

    # Apply a slight blur to smooth out the gradients
    image = image.filter(ImageFilter.GaussianBlur(2))
    return image

title = "Image"
description = '''
## image(value,id = None)
1. Html'deki img elementine karşılık gelir. Sayfada görüntülenmesi istenen resimler için kullanılır.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Image elementinin id'si                          |
| value         | Image elementinin src'si                       |
'''