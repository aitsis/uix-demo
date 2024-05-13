from uix_components._basic_table._basic_table import title, description, sample as code
from uix_components import basic_table
from uix.elements import div

headers = ["Header 1", "Header 2", "Header 3"]
data = [
    ["Row 1", "Row 1", "Row 1"],
    ["Row 2", "Row 2", "Row 2"],
    ["Row 3", "Row 3", "Row 3"],
]
  
def basic_table_example():
    with div() as table_example:
        basic_table(id= "basic_table_example", headers=headers, data=data)
    return table_example