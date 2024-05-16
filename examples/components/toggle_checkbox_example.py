from uix_components import toggle_checkbox
from uix.elements import text

def on_change(ctx, id, value):
    ctx.elements["toggle-checkbox-example"].value = value

def toggle_checkbox_example():
    toggle_checkbox(
        input_id="toogle-example",
        input_name="toogle-example",
        label_usefor="toogle-example",
        toggle_on="Checked",
        toggle_off="Unchecked",
        onChange= on_change)
    text("",id="toggle-checkbox-example")

title="Toggle Checkbox"
description = '''
    Toggle Checkbox example shows how to create a toggle checkbox component.
'''
