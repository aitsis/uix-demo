from uix_components import basic_datalist
from uix_components._basic_datalist._basic_datalist import title, description, sample as code
def basic_datalist_example():
    options = ["BMW","AUDI","MERCEDES"]
    return basic_datalist(name="Car List", id = "datalist", options = options, 
                          callback = lambda ctx, id, value: print(f"Datalist {id} changed to: {value}"))