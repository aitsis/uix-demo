from uix_components import basic_datalist
from uix_components._basic_datalist._basic_datalist import title, description, sample as code
def basic_datalist_example():
    options = ["BMW","AUDI","MERCEDES"]
    options_dict = [
        {"id": "1", "value": "OPEL"}, 
        {"id": "2", "value": "FORD"}, 
        {"id": "3", "value": "VOLKSWAGEN"}]
    return basic_datalist(name="Car List", id = "datalist", options = options, 
                          callback = lambda ctx, id, value: print(f"Datalist {id} changed to: {value}"))