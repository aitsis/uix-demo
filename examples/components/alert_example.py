from uix.elements import button, row
from uix_components import basic_alert
from uix_components._basic_alert._basic_alert import title, description, sample as code 

def alert_example():
    with row().style("gap","10px") as content:
        basic_alert_el = basic_alert("", id = "comp_alert")

        button("Show Alert Danger With Icon").on("click", lambda ctx, id, value: basic_alert_el.open("alert-danger", "selam", "fa-solid fa-circle-xmark")).cls("alert-danger")
        button("Show Alert Warning").on("click", lambda ctx, id, value: basic_alert_el.open("alert-warning", "selam")).cls("alert-warning")
        button("Show Alert Info").on("click", lambda ctx, id, value: basic_alert_el.open("alert-info", "selam merhaba ben umut savaşım çeliker")).cls("alert-info")
        button("Show Alert Success").on("click", lambda ctx, id, value: basic_alert_el.open("alert-success", "selam")).cls("alert-success")
    
    return content
