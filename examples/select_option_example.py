from uix.elements import select, option
from uix.elements._select import title, description, sample as code

def select_option_example():
    with select("").style("margin","auto").style("display","block"):
        option("Option 1")
        option("Option 2").selected()
        option("Option 3")