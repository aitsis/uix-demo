from uix.elements._check import check  # Assuming check is the class within _check module
from uix.elements._check import title, description, sample as code
from uix.elements._div import div

def check_example():
    main = check("", id="check_example").on("click", on_click)
    test = div("test", "test")
    return main

def on_click(ctx, id, value):
    print("Clicked", id, value)
    if value == False:
        ctx.elements["test"].value = "Unchecked!"
    else:
        ctx.elements["test"].value = "Checked!"
    ctx.elements["test"].update()