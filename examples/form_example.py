from uix.elements import form, div, button, label, input, grid, col
from uix.elements._form import title, description, sample as code

def comp1():
    with form(id="myForm") as form1:
        form1.cls("border")
        with grid("",columns="1fr 4fr") as grid1:
            grid1.style("gap","10px")
            grid1.style("padding","10px")
            grid1.style("width","300px")
            with col().style("font-size","20px"):
                label("Name", usefor="name")
                label("Email", usefor="email").style("margin-top","10px")
            with col():
                input("", id="name",  placeholder="Enter your name")
                input("", id="email",  placeholder="Enter your email").style("margin-top","10px")
        
            button("Submit").style("margin-top","10px")
       
        
def form_example():
    with div("") as main:
        comp1()
    return main


    
