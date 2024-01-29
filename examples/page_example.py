from uix.elements import page, header, main, footer, text,div
from uix.elements._page import title, description, sample as code

def page_example():
    with div().size("100%","60vh") as example_page:
        with page("") as page_:
            with header("") as header_:
                text("Header Example")
            with main("") as main_:
                text("Main Example")
            with footer("") as footer_:
                text("Footer Example")
    return example_page

