from uix.elements import image

def size_example():
    image_url = "https://ai.ait.com.tr/wp-content/uploads/AIT_AI_LOGO.png"
    main = image(image_url).size(300,"auto")
    return main

title = "Size"

description = '''
# size(width,height)

1. Elementin boyutunu belirler.

    | attr          | desc                                              |
    | :------------ | :------------------------------------------------ |
    | width         | Elementin genişliğini belirler. int ya da str değer kabul eder. int değer girilirse px cinsinden değer alır. |
    | height        | Elementin yüksekliğini belirler. int ya da str değer kabul eder. int değer girilirse px cinsinden değer alır. |
'''

code = '''
def size_example():
    image_url = "https://ai.ait.com.tr/wp-content/uploads/AIT_AI_LOGO.png"
    example = image(image_url).size(300,"auto") # width = 300px, height = auto
    return example
'''