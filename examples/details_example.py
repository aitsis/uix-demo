from uix.elements import details, text # type: ignore
from uix.elements._details import title, description, sample as code

def details_example():    
    with details(open=True) as details_example:
        text("Details Content")
    return details_example