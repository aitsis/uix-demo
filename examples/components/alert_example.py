from uix.elements import button, row
from uix_components import basic_alert
from uix_components._basic_alert._basic_alert import title, description, sample as code 

def alert_example():
    with row() as content:
        alertSuccess = basic_alert("", id = "myAlert", type="success")
        alertWarning = basic_alert("", id = "myAlertWarning", type="warning")
        alertDanger = basic_alert("", id = "myAlertDanger", type="danger")
        alertInfo = basic_alert("", id = "myAlertInfo", type="info")
        button("Show Alert Danger").on("click", lambda ctx, id, value: alertDanger.open("alert-danger", "selam")).cls("alert-danger")
        button("Show Alert Warning").on("click", lambda ctx, id, value: alertWarning.open("alert-warning", "selam")).cls("alert-warning")
        button("Show Alert Info").on("click", lambda ctx, id, value: alertInfo.open("alert-info", "selam")).cls("alert-info")
        button("Show Alert Success").on("click", lambda ctx, id, value: alertSuccess.open("alert-success", "selam")).cls("alert-success")
    
    return content
