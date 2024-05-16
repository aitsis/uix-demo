from uix.elements import summary, details, label

def summary_example():
    with details() as summary_example:
        summary(value="Details main title")
        label(value="Details Content")
    return summary_example

title = "Summary"
description = '''
## summary(value,id = None)
1. Summary elementi. Details elementinin açıklama başlığı olarak kullanılan bir elementtir.

| attr          | desc                                             |
| :------------ | :------------------------------------------------|
| id            | Summary elementinin id'si                        |
| value         | Summary elementinin içeriği                      |
'''