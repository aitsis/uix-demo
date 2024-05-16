from uix_components import basic_select
from uix.elements import col, md, textarea

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


def md_playground_example():
     with col():
          basic_select(id = "mySelect",options = options, callback=on_options_change).size("150px",None)
          textarea(id = "text", value=options[0]["example"]).on("input", on_change).size("100%", "300px")        
          md(id = "preview", value=options[0]["example"]).size("100%", "300px").style("overflow: auto")
     
title = "Markdown Playground"
description = """
## Markdown denemelerinizi burada yapabilirsiniz.
"""