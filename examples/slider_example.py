from uix.elements import slider, input
from uix.elements._slider import title, description, sample as code

def on_slider_change(ctx, id, value):
    print("Slider değeri değişti")
    ctx.elements[id].value = value
    ctx.elements["myInput"].value = value
    print("Yeni değer: ", ctx.elements[id].value)

def input_changed(ctx, id, value):
    ctx.elements[id].value = value
    ctx.elements["mySlider"].value = value
    print("Yeni değer: ", ctx.elements[id].value)

def slider_example():
    main = slider(id="mySlider", min=0, max=100, value=50, step="5").style("width", "400px").on("change", on_slider_change)
    input(type="number", id="myInput", value=main.value).on("change", input_changed)
    return main