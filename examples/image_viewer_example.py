import uix

from uix.elements import container, file

from uix_components import image_viewer


def on_upload(ctx, id, event, data, status):
    print("on_upload", id, event, data, status)
    if status == "done":
        iw = ctx.session.elements["iw1"]
        if event == "select":
            iw.value = data[0].url
        
def image_viewer_example():      
    with container() as main: 
        file(id="file1",accept="image/*",multiple=False,callback=on_upload).cls("center")
        image_viewer(id = "iw1", value="https://ai.ait.com.tr/wp-content/uploads/AIT_AI_LOGO.png",hasButtons=True).size(600,720)
    return main
