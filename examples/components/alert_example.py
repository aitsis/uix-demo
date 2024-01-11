import uix
import uix_components
from uix.elements import div, button, grid, col
from uix_components import basic_alert
from uix_components._basic_alert._basic_alert import title, description, sample as code 

def alert_example():
    with col() as content:
        alert = basic_alert("", id = "myAlert", type="success")
        button("Show Alert", id = "show_alert").on("click", lambda ctx, id, value: alert.open("alert-success", "selam"))
    return content
