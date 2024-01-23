import uix
from uix_components import address_form
from uix_components._address_form._address_form import title, description, sample as code

def address_form_example():
    root = address_form(id="deneme")
    return root