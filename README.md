# Welcome to uix-demo

For run, before install requirements:
https://github.com/aitsis/uix.git
https://github.com/aitsis/uix-components.git

these examples you can type;
```batch
$ python uix_demo.py
```

for visiting examples Please select from left side menu

Example Code: (from hello_world example)

```python
from uix.elements import div

def hello_world_example():
    main = div("Hello World!").style("font-size","30px")
    return main
```
