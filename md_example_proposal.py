import uix
from uix_components import image_viewer, basic_alert, basic_select
from uix.elements import button, image, col, row, md, textarea, select, option,label

options = [
    {"id":"0","isSelect":False, "value":"Select an example ","example":
     """
Select an example from the dropdown to see the preview here or write your own markdown text in the textarea.
     """},
    {"id":"1","isSelect":False, "value":"Header","example":
     """
# h1 Heading 8-)
## h2 Heading
### h3 Heading
#### h4 Heading
##### h5 Heading
###### h6 Heading
     """},
    {"id":"2","isSelect":False, "value":"Table","example":
     """
| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |

     """},
    {"id":"3","isSelect":False, "value":"Code","example":
     """
```python
print("Hello World!")
```
     """},
]

message = "Select an example from the dropdown to see the preview here or write your own markdown text in the textarea."

def on_change(ctx, id, value):    
    ctx.elements["preview"].value = value

def on_options_change(ctx, id, value):
    ctx.elements["text"].value = options[int(value)]["example"]
    ctx.elements["preview"].value = options[int(value)]["example"]


def main():
        with col():
            with row().size(None, "60px"):
                 basic_select(id = "mySelect",options = options, callback=on_options_change)
    
            textarea(id = "text", value=options[0]["example"]).on("input", on_change).size("100%", "100%")        
            md(id = "preview", value=options[0]["example"]).size("100%", "100%").style("overflow: auto")
        
uix.start(ui=main, config={'debug': True,'port': 5001})