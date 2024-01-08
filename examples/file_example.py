
from uix.elements import div, col, border, file, image, container, dialog

def on_click_image(ctx,id,value):
    print("Clicked image = ",value) 
    with ctx.elements["image-dialog"]:
        image(value,id = "dialog-image").style("width","100%").style("height","100%").on("click",lambda ctx,id,value: ctx.elements["image-dialog"].hide() )
    ctx.elements["image-dialog"].update()
    ctx.elements["image-dialog"].show()

def on_change(ctx,id,value):
    print("File = ",value," id = ",id)
    with ctx.elements["images"]:
        for i in range(len(value)):
            (image(value[i],id=value[i]).style("margin-top","20px")
             .style("margin-left","5px").style("width","100px").style("height","100px").on("click",on_click_image))
    ctx.elements["images"].update()

def file_example():
    with container("") as main:
        file("",id="myFile",multiple = True).on("change",on_change)
        div("",id = "images").style("max-height","600px").style("overflow","auto")
        dialog("","image-dialog")
    return main
