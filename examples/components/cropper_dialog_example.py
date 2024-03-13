from uix_components._cropper_dialog._cropper_dialog import title, description, sample as code
from uix_components._cropper_dialog._cropper_dialog import cropper_dialog
from uix_components._input_image._input_image import input_image
from uix.elements import button, col

file_url = ""

def crop_done(ctx, id, value):
    options = {"url" : value, "id" : None}
    ctx.elements["input-image-crop"].setImage(options)
    ctx.elements["cropper_dialog"].image_url = value
    ctx.elements["cropper_dialog"].hide()

def upload_done(ctx, id, value):
    global file_url
    file_url = ctx.elements["input-image-crop"].file_url
    ctx.elements["cropper_dialog"].image_url = file_url

def cropper_dialog_example():
    global file_url
    cropper_dialog(id="cropper_dialog", callback = crop_done, image_url = file_url)
    with col(id="cropper-col").cls("border").style("width","40%").style( "height","30%"):
        input_image(id="input-image-crop", callback=upload_done).style("height","500px")
        button("Crop", id="crop-button").on("click", lambda ctx, id, value: ctx.elements["cropper_dialog"].show())


           