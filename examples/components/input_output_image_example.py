import uix
from uix.elements import col, button,row
from uix_components import input_image
from uix_components import output_image



def run(ctx, id, value):
    input_img=ctx.elements["input_image_test"]
    output_img = ctx.elements["output_image_test"]
    url=input_img.file_url
    output_img.set_image(ctx=ctx, value=url)

def input_output_image_example():
    with col():
        with row() as input_output_image_test:
            with col(id="imagine-input-col").cls("border").style("width","50%"):
                input_img=input_image(id="input_image_test", viewer="fabric").style("height","500px")
            
            with col(id="imagine-input-col").cls("border").style("width","50%"):
                output_image(id="output_image_test", setinputImage=input_img.setImage, viewer="fabric").style("height","500px")

        button("Run",id="run").cls("btn btn-primary").on("click", run)
    return input_output_image_test