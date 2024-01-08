
import uix
from uix.elements import page, header, text, container, details, button, row
with container("") as main:
    with row("").style("height","100px"):
        text("Bu konuda araştırma yapmak istiyorsanız düğmeye basın")
        button("Araştırma")
    with details("Daha detaylı bilgi için düğmeye basın"):
            text("Araştırma yapmak için düğmeye basın ama bunun uzun bir metin olması gerekiyor. fklsdşkfşlsdk")




uix.start(ui = main, config={"debug":True})


# TODO
# width and height eklenecek

# eklenecek elementler
# meter
# progress
# main
# footer
# embed
# object ???

