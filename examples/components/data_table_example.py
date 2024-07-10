from uix_components import data_table, basic_dialog
from uix.elements import text,row,col, label,table, thead, tr, th, td,input,button

payload = {}
config = {
        "pageLength": 15,
        "layout": {
            "topStart": {
                "buttons": [
                    'colvis',
                    'copyHtml5',
                    'excelHtml5',
                    'csvHtml5',
                    'pdfHtml5',
                    'print'
                ]
               
            },
            "topEnd": {
                "search": {
                    "placeholder": 'Type search here'
                }
            },
            "bottomStart": {
                "pageLength": {
                    "menu": [ 15, 20, 50, 100 ]
                },
                "info": True,
               },
            "bottomEnd": {
                "paging": {
                    "numbers":3,
                }
            }
        },
    }

data = [
    {
        "name": "John",
        "surname": "Doe",
        "company": "Google",
        "phone": "1234567890",
        "isVerified": "True",
        "package": "Premium"


    },
    {
        "name": "Jane",
        "surname": "Doe",
        "company": "Facebook",
        "phone": "0987654321",
        "isVerified": "False",
        "package": "Free"
    },
    {
        "name": "Alice",
        "surname": "Smith",
        "company": "Apple",
        "phone": "1234567890",
        "isVerified": "True",
        "package": "Premium"
    },
    {
        "name": "Bob",
        "surname": "Smith",
        "company": "Microsoft",
        "phone": "0987654321",
        "isVerified": "False",
        "package": "Free"
    },
   
    ]
def data_table_example():
    basic_dialog(id = "myDialog",elements=[lambda: row(id="dialog-content")], close_on_outside = False).style("width: max-content; height: max-content; padding: 1rem;")
    with col().style("gap: 1rem;"):
        with col().style("gap: 1rem;"):
            label("Data Table Example 1").cls("point")
            text("Varsayılan ayarlarla oluşturulmuş örnek data table.")
            data_table(id="example-table", data=data)

        with col().style("gap: 1rem;"):
            label("Data Table Example 2").cls("point")
            text("Özel ayarlarla oluşturulmuş örnek data table.")
            data_table(id="example-table2", data=data, config=config)

        with col().style("gap: 1rem;"):
            label("Data Table Example 3").cls("point")
            text("Edit edilebilir data table örneği.")
            data_table(id="example-table3", data=data, callback=show_row_data ,dialog_id="myDialog")

def show_row_data(ctx, id, value):
    row_data = value["data"]
    columns = row_data.keys()
    with ctx.elements["dialog-content"]:
        with col().style("gap: 1rem;"):
            with table(""):
                with thead():
                    with tr():
                        for key in columns:
                            th(key)
                    with tr():
                        for key in columns:
                            with td():
                                input(row_data[key],id=key).on("change", lambda ctx, id, value: setter(ctx, id, value))
            
            button("Update").on("click", lambda ctx, id, value, index= value["index"]: update_row_data(ctx, id, value, index))
    
    ctx.elements["myDialog"].update()
    ctx.elements["myDialog"].show()

def setter(ctx, id, value):
    ctx.elements[id].value = value
    payload[id] = value
 
def update_row_data(ctx, id, value, index):
    for key in payload.keys():
        data[index][key] = payload[key]

    payload.clear()

    ctx.elements["example-table3"].update_table(data)
    
    

title = "Data Table"
description = """
## data_table(data=[], id=None, dialog_id=None, iconCls="fa fa-edit",callback=None,config=None)

1. Verileri datatable olarak gösterir. Arama, sıralama, sayfalama gibi özellikler sunar.
2. Verileri dict listesi olarak alır.
3. **Callback** parametresi verilirse, tablodaki her satır tıklanabilir olur ve tıklanıldığında bir dialog açılır. Bu dialogda satırdaki verileri gösterilir ve düzenlenebilir.
4. Eğer callback parametresi verilirse, açılacak olan **dialog_id** parametresi verilmelidir.
5. Eğer config parametresi verilirse, datatable için özel ayarlar yapılabilir verilmezse varsayılan ayarlar kullanılır.
7. Data tabledaki **update_table** fonksiyonuna yeni veri listesi verilerek tablo güncellenebilir.

"""