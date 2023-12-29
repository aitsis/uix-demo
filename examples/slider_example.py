from uix.elements import slider, label

def slider_example():
    main = slider(id="mySlider", min=0, max=100, value=50).style("width", "400px")
    return main