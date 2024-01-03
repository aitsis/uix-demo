from uix.elements import label
from uix.elements._label import title, description, sample as code

def label_example():
    main = label("This Text is a Label!").style("font-size","20px")
    return main