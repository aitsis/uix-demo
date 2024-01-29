
import uix
from uix.elements import container, canvas, text, border, row
WIDTH = 500
HEIGHT = 500
SCALE = 1
BRUSH_SIZE = 3
def on_mouse_move(ctx, id, value):
    if(value["buttons"] == 1):
        ctx.session.send(id,{"x":value["offsetX"]*SCALE,"y":value["offsetY"]*SCALE,"brush_size":BRUSH_SIZE},"test-canvas")
        ctx.elements["events1"].value = str(value)

def on_key_down(ctx, id, value):
    if(value["key"] == "ArrowUp"):
        global BRUSH_SIZE
        BRUSH_SIZE += 1
    if(value["key"] == "ArrowDown"):
        BRUSH_SIZE -= 1
    ctx.elements["events1"].value = str(value)

script = """
    event_handlers["test-canvas"] = function(id,value,event_name) {
    const canvas = document.getElementById(id);
    const ctx = canvas.getContext("2d");
    ctx.fillStyle = "#FF0000";
    ctx.beginPath();
    ctx.arc(value.x, value.y, value.brush_size, 0, 2 * Math.PI);
    ctx.fill();
    }
"""

uix.html.add_script("test-canvas", script, beforeMain=False)

def events_example():
    with container()as main:
        text("Mouse and Keyboard Events - Yukarı Ok = Brush + 1, Aşağı Ok = Brush -1")
        with border(id="border1"):
            canvas1 = canvas(width=WIDTH*SCALE,height=HEIGHT*SCALE).on("mousemove",on_mouse_move).on("mousedown",on_mouse_move)
            canvas1.size(WIDTH,HEIGHT).on("keydown",on_key_down).attr("tabindex",0)
        text("",id="events1").size("100%",150)
    return main
