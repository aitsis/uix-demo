from uix.elements import summary, details, label
from uix.elements._summary import title, description, sample as code

def summary_example():
    with details() as summary_example:
        summary(value="Details main title")
        label(value="Details Content")
    return summary_example


