from uix.elements import form, div, button, label, input, grid, col, textarea
from uix.elements._form import title, description, sample as code

def submit_form(ctx, id, value):
    print("Form submitted")
    form = {
        "name": ctx.elements["name"].value,
        "email": ctx.elements["email"].value
        }
    print(form)
    
def input_setter(ctx, id, value):
    ctx.elements[id].value = value
        
def form_example():
    with div("") as main:
        with form(id="myForm").cls("border").on("submit", submit_form):
            with grid("",columns="1fr 4fr") as grid1:
                grid1.style("gap","10px")
                grid1.style("padding","10px")
                grid1.style("width","300px")
                with col().style("font-size","20px"):
                    label("Name", usefor="name")
                    label("Email", usefor="email").style("margin-top","10px")
                with col():
                    input("", id="name",  placeholder="Enter your name").on("change", input_setter).style("margin-top","10px")
                    input("", id="email",  placeholder="Enter your email").on("change", input_setter).style("margin-top","10px")
            
                button("Submit", type="submit").style("margin-top","10px")
    return main


    
