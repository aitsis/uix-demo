from uix.elements import details, div, text # type: ignore
from uix.elements._details import title, description, sample as code

def details_example():
    with div("",) as details_example:
        with details(""):
            text("Details Content")
    return details_example