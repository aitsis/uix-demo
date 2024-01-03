from uix.elements._textarea import textarea
from uix.elements._textarea import title, description, sample as code
from uix.elements._div import div

def textarea_example():
    main = textarea("","text", placeholder="Selam").on("input", on_change)
    div(id="test", value="Selam")
    return main

def on_change(ctx, id, value):
    print("Changed", id, value)
    ctx.elements["test"].value = value
    ctx.elements["test"].update()
