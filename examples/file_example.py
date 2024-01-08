
from uix.elements import div, col, border, file, image, container, dialog, button, row, check
from uix.app import files
import io
from PIL import Image
def on_file_upload_events(ctx,id,value):
    url = value["url"]
    status = value["status"]
    print("url = ",url," status = ",status)

    if status == "error":
        print("Error = ", value["error"])
    else:
        data = files[url]["data"]
        print("File size = ", len(data))
        image = Image.open(io.BytesIO(data))
        grayimage = image.convert("L")
        files[url] = None
        newurl = url[-14:]
        print("newurl = ",newurl)
        temp = io.BytesIO()
        grayimage.save(temp,format="png")
        files[newurl] = {"data":temp.getvalue(),"type":"image/png"}        
        #ctx.elements[url].value = "/download/"+newurl
        ctx.elements["dialog-image"].value = "/download/"+newurl

    

def on_click_image_upload(ctx,id,value):
    print("image upload Clicked image = ",value)
    elm = ctx.elements["myFile"]
    print("elm = ",elm)
    ctx.elements["myFile"].upload(value)

def on_click_image_show_dialog(ctx,id,value):
    print("Clicked image22 = ",value) 
    with ctx.elements["image-dialog"]:
        image(value,id = "dialog-image").style("width","100%").style("height","100%").on("click",lambda ctx,id,value: ctx.elements["image-dialog"].hide() )
        button("Upload File",id = "btn"+value).on("click",lambda ctx,id,value: ctx.elements["myFile"].upload(id[3:]))
    ctx.elements["image-dialog"].update()
    ctx.elements["image-dialog"].show()

def on_change(ctx,id,value):
    print("File = ",value," id = ",id)
    with ctx.elements["images"]:
        width = "300px"
        if len(value) > 1:
            width = "100px"
        for i in range(len(value)):
            (image(value[i],id=value[i]).style("margin-top","20px")
             .style("margin-left","5px").style("width",width).on("click",on_click_image_show_dialog))
    ctx.elements["images"].update()

def file_example():
    with container("") as main:
        with border(""):
            file("",id="myFile",multiple = True).on("change",on_change).on("file-upload",on_file_upload_events)
            check("multiple",id="multiple").on("change",lambda ctx,id,value: ctx.elements["myFile"].set_attr("multiple",value))
        div("",id = "images").style("max-height","600px").style("overflow","auto")
        dialog("","image-dialog")
    return main
