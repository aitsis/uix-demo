from uix.elements import input, button, border, div, row, col
#from uix.elements._input import title, description, sample as code

def input_example():
    with col("").style("height","min-content"):
        input("", placeholder="Kullanıcı Adı", required=True).style("margin-bottom","10px")
        input("",type="password", placeholder="Şifre").style("margin-bottom","10px")
        input("",type="number", placeholder="Sayı").style("margin-bottom","10px")
        input("2024-01-01T00:00",type="datetime-local", placeholder="Tarih ve Saat").style("margin-bottom","10px")
        input("",type="date").style("margin-bottom","10px")
        input("",type="time").style("margin-bottom","10px")      
    
    def on_change(ctx, id, value):
        if value!= "":
            ctx.elements["submitButton"].attrs.pop("disabled", None)
            ctx.elements["submitButton"].update()
            
        else:
            ctx.elements["submitButton"].attrs["disabled"] = True
            ctx.elements["submitButton"].update()
            
           

    with border("").style("padding","20px").style("width","100%"):
        input(id="userName", placeholder="Kullanıcı Adı", required=True).on("input",on_change)
        with row("").style("display","flex").style("justify-content","space-between"):
            div("Zorunlu alanlar doldurulmalıdır.").style("font-size","10px")
            button("Gönder", id="submitButton", type="submit", disabled = True)



    