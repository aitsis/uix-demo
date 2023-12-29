from uix.elements import select, option

def select_option_example():
    with select(""):
        option("Option 1")
        option("Option 2").selected()
        option("Option 3")