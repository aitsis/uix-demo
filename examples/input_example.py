from uix.elements import input, button, border, div, row, col
from uix.elements._input import title, description, sample as code

def input_example():
    with col("").style("width","min-content").style("gap","10px"):
        input("", placeholder="Kullanıcı Adı", required=True)
        input("",type="password", placeholder="Şifre")
        input("",type="number", placeholder="Sayı")
        input("2024-01-01T00:00",type="datetime-local", placeholder="Tarih ve Saat")
        input("",type="date")
        input("",type="time")    
    
    def on_change(ctx, id, value):
        if value!= "":
            ctx.elements["submitButton"].attrs.pop("disabled", None)
            ctx.elements["submitButton"].update()
            
        else:
            ctx.elements["submitButton"].attrs["disabled"] = True
            ctx.elements["submitButton"].update()
                    
    with border("").style("padding","20px"):
        input(id="userName", placeholder="Kullanıcı Adı", required=True).on("input",on_change)
        with row(""):
            div("Zorunlu alanlar doldurulmalıdır.").style("font-size","10px")
            button("Gönder", id="submitButton", type="submit", disabled = True)



    