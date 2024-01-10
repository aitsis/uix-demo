import uix

from uix.elements import file, div, image, col, row, progress,check, button

from uix.core.file import File 
def lineitem(value):
    div(value).style("padding","5px;")

def upload_file(ctx, id, value):
    print("upload_file",id)
    ctx.elements["file_123"].upload(id)
    

def line(file):
    with row(id=file.url).style("margin-top","10px").on("click", upload_file) as r:
        image(value=file.url).size(None,100)
        lineitem(file.name)
        lineitem(file.size)
        lineitem(file.type)
        progress(id = file.url+"_progress")
            

def list_files(ctx, files):
    with ctx.elements["files"]:
        for file in files:
            line(file)
    ctx.elements["files"].update()

def show_error(ctx, error):
    with ctx.elements["files"]:
        div(error).style("color","red")
    ctx.elements["files"].update()


def select_callback(ctx, id, data, status):
    if status == "done":
        list_files(ctx, data)
    else:
        show_error(ctx, data)

def upload_callback(ctx, id, data, status):
    if status == "done":
        print("upload done",len(data))
        #>>>>>>>>>>>>>>>>>>>
        # USE DATA HERE
        #<<<<<<<<<<<<<<<<<<<<
    elif status == "progress":
        ctx.elements[data["url"] + "_progress"].value = data["progress"]
    else:
        show_error(ctx, data)

def file_callback(ctx, id, event, data, status):
    if event == "select":
        select_callback(ctx, id, data, status)    
    elif event == "upload":
        upload_callback(ctx, id, data, status)


def file_example():
    multiple = False
    with div(id="root").style("max-height","80%").style("overflow","auto") as root:
        check(multiple, id="multiple", disabled = False).on("change", lambda ctx, id, value: ctx.elements["file_123"].set_attr("multiple",value))
        file(id="file_123", multiple=multiple,callback = file_callback, accept="image/png,image/jpeg,image/gif")
        div("Files:", id="files").style("margin-top","10px")
        button("toggle disable checkbox", id="disable_checkbox").on("click", lambda ctx, id, value: ctx.elements["multiple"].set_attr("disabled",not ctx.elements["multiple"].get_attr("disabled")))
    return root


         