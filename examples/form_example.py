from uix.elements import form, div, button, label

def comp1():
    with form(id="myForm", ) as form1:
        
        form1.style("width","400px")
        form1.style("border","1px #aaa solid")
        form1.style("padding","10px")
        form1.style("gap","10px")
        form1.style("border-radius","10px")
        with label("Name") as label1:
            label1.style("display","block")
            label1.style("font-size","20px")
            label1.style("margin-bottom","5px")
        with label("Email") as label2:
            label2.style("display","block")
            label2.style("font-size","20px")
            label2.style("margin-bottom","5px")
        
        button("Submit").style("width","100%")
        

def form_example():
    with div("") as main:
        comp1()
    return main


    
