from uix.elements import text
from uix_components import toggle_checkbox

def toggle_checkbox_example():
    def on_change(ctx, id, value):
        ctx.elements["toggle-checkbox-example"].value = value

    toggle_checkbox(
        input_id="toogle-example",
        input_name="toogle-example",
        label_usefor="toogle-example",
        toggle_on="Checked",
        toggle_off="Unchecked",
        onChange= on_change)
    text("",id="toggle-checkbox-example")

title="Toggle Checkbox Example"

description = '''
    Toggle Checkbox example shows how to create a toggle checkbox component.
'''

code = """
from uix_components import toggle_checkbox

def toggle_checkbox_example():
    def on_change(ctx, id, value):
        ctx.elements["toggle-checkbox-example"].value = value

    toggle_checkbox(
        input_id="toogle-example",
        input_name="toogle-example",
        label_usefor="toogle-example",
        toggle_on="Checked",
        toggle_off="Unchecked",
        onChange= on_change)
    text("",id="toggle-checkbox-example")
"""
