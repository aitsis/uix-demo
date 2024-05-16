from uix_components import credit_card
from uix.elements import div

def credit_card_example():
    with div().size("100%","100%") as credit_card_example:
        credit_card("",id="credit_card_example")
    return credit_card_example

title = "Credit Card"
description = """
## credit_card(value, id = None)
1- Kredi kartı bilgilerinin girilebileceği bir alan oluşturur.

| attr                  | desc                                              |
| :-------------------- | :------------------------------------------------ |
| id                    | credit_card elementinin id'si                         |
"""