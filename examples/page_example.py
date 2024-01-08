from uix.elements import page, header, main, footer, text
from uix.elements._page import title, description, sample as code

def page_example():
    with page("") as page_:
        with header("") as header_:
            text("Header Example")
        with main("") as main_:
            text("Main Example")
        with footer("") as footer_:
            text("Footer Example")
    return page_

