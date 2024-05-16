from uix.elements import page, header, main, footer, text,div

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


title = "Page"
description = '''
## page(value,id)
1. Page elementi. İçi boş bir ana div oluşturur. Sıfırdan bir sayfa oluşturmak için kullanılabilir. İçerisine elemanlar eklenerek kullanılır.

| attr          | desc                                           |
| :------------ | :----------------------------------------------|
| id            | Page elementinin id'si                         |
| value         | Page elementinin içeriği                       |
'''