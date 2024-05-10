from uix_components import credit_card
from uix_components._credit_card._credit_card import title, description, sample as code
from uix.elements import div

def credit_card_example():
    with div().size("100%","100%") as credit_card_example:
        credit_card("",id="credit_card_example")
    return credit_card_example