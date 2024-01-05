from uix.elements import file, div, image, col
from uix.elements._file import title, description, sample as code

def file1():
    with col().cls("border"):
        file("",id="myFile", accept=".png, .jpg")
        image("", id="img").style("margin-top","20px").style("width","300px").style("height","300px")
    
def file_example():
    with div("") as main:
        file1()
    return main



