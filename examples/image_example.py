from uix.elements import image # type: ignore
from uix.elements._image import title, description, sample as code

def image_example():
    image_url = "https://ai.ait.com.tr/wp-content/uploads/AIT_AI_LOGO.png"
    main = image(image_url).cls("image")
    return main