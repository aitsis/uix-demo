from uix.elements import col
from uix_components import basic_prompt

def prompt_example():
    with col() as content:
        basic_prompt("", id = "myPrompt")
    return content

title="Prompt"

description = '''
    Prompt example shows how to create a prompt component.
'''