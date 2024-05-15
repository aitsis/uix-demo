from uix_components import input_image
from uix.elements import col

def input_image_example():
    with col(id="imagine-input-col").cls("border").style("width","50%") as input_image_test:
        input_image(id="input_image").style("height","500px")
    return input_image_test

title = "Input Image"
description = """
## input_image(value=None, id=None, viewer="seadragon",callback=None)
1- Kullanıcıların resim yüklemesini ve görüntülemesini sağlar.

| attr                  | desc                                                      |
| :-------------------- | :------------------------------------------------------   |
| viewer                | Resim görüntüleyici tipi. Seadragon veya fabric olabilir. |
| callback              | Resim yüklendikten sonra çalıştırılacak fonksiyon.        |
"""