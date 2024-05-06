from uix_components._input_image._input_image import input_image
from uix.elements import image
import uix

uix.html.add_script("drag_drop_elm", script=
"""               
event_handlers['drag_drop_elm'] = function (id, value, eventName) {
    const dropArea = document.getElementById(value.dropAreaId);

    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        dropArea.addEventListener(eventName, preventDefaults, false);
        document.body.addEventListener(eventName, preventDefaults, false);
    });

    ['dragenter', 'dragover'].forEach(eventName => {
        dropArea.addEventListener(eventName, highlight, false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
        dropArea.addEventListener(eventName, unhighlight, false);
    });

    dropArea.addEventListener('drop', handleDrop, false);

    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    };

    function highlight(e) {
        dropArea.style.border = "2px dashed #333";
    };

    function unhighlight(e) {
        dropArea.style.border = "2px dashed #ccc";
    };

    function handleDrop(e) {
        const dt = e.dataTransfer;
        const isFromBrowser = dt.getData("fromBrowser") || false;
        const imageSrc = dt.getData('src') || '';
        const files = isFromBrowser && imageSrc !== '' ? [new File([imageSrc], "temp_filename.png", { type: "image/png" })] : Array.from(dt.files);

        const fileInfos = files.map(file => ({
            name: file.name,
            size: file.size,
            type: file.type,
            lastModified: file.lastModified,
            url: isFromBrowser ? imageSrc : URL.createObjectURL(file)
        }));
        clientEmit(value.inputId, fileInfos, 'change');
    };

    // Sadece img suruklemek icin START
    const drag_image = (e) => {
        const dt = e.dataTransfer;
        dt.setData("src", e.target.src);
        dt.setData("fromBrowser", true);
    };
    window.drag_image = drag_image;
    // Sadece img suruklemek icin END
};
""", beforeMain=False)

class drag_drop(uix.Element):
    def __init__(self, id=None):
        super().__init__(id=id)
        self.cls("example")
        with self:
            img = image(id= "drag_img", value="https://picsum.photos/seed/picsum8/200/200").style("margin-right: 1rem;")
            img.get_client_handler_str = lambda event_name: self.get_client_handler_str(event_name)
            img.on("dragstart", lambda ctx, id, value: print(value, id , ctx))
            #img.attrs["draggable"] = "false" # default is true 
            
            self.dropArea = input_image(id=f"{self.id}-input-image-ashjdasd", callback=self.imageUploadDone)
            self.dropArea.style("width:300px; height:300px; border: 2px dashed #ccc; border-radius: 10px; padding: 5px;")    
    # sayfadaki img elementini surukleme islemi basladiginda calisir
    # bu fonksiyonu img elementine ekleyebiliriz
    def get_client_handler_str(self, event_name):
        print(event_name)
        if event_name in ["dragstart"]:
            return f" on{event_name}='window.drag_image(event)'"
        else:
            return super().get_client_handler_str(event_name)
    
    def init(self):
          print(f"init for {self.id}")
          self.session.queue_for_send(
              self.id,
              {
                  'dropAreaId': self.dropArea.id,
                  'inputId': self.dropArea.file.id,
               },
               "drag_drop_elm")

    def imageUploadDone(self, ctx, id, value):
        print(value, 'imageUploadDone')

def drag_drop_input_image_example():
    return drag_drop()
    


title = "Drag and Drop Input Image"

description = '''
## drag_drop_input_image_example()
1. input_image elementi kullanılarak bir input alanı oluşturulur.
2. Image sürüklenirken dragstart eventi ile img elementi sürüklenirken çalışacak fonksiyon belirlenir.
3. Bu fonksiyon ile sadece img elementi sürüklenirken çalışacak fonksiyon belirlenir.
4. Bu fonksiyon ile sürüklenen img elementinin src'si dataTransfer objesine eklenir.
5. Bu sayede sürüklenen img elementinin src'si drop eventinde alınabilir.
6. Drop eventinde sürüklenen img elementinin src'si alınır ve input_image elementine gönderilir.
7. input_image elementi ile sürüklenen img elementi gösterilir.
'''

code = '''
from uix_components._input_image._input_image import input_image
from uix.elements import image
import uix

uix.html.add_script("drag_drop_elm", script=
"""               
event_handlers['drag_drop_elm'] = function (id, value, eventName) {
    const dropArea = document.getElementById(value.dropAreaId);

    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        dropArea.addEventListener(eventName, preventDefaults, false);
        document.body.addEventListener(eventName, preventDefaults, false);
    });

    ['dragenter', 'dragover'].forEach(eventName => {
        dropArea.addEventListener(eventName, highlight, false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
        dropArea.addEventListener(eventName, unhighlight, false);
    });

    dropArea.addEventListener('drop', handleDrop, false);

    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    };

    function highlight(e) {
        dropArea.style.border = "2px dashed #333";
    };

    function unhighlight(e) {
        dropArea.style.border = "2px dashed #ccc";
    };

    function handleDrop(e) {
        const dt = e.dataTransfer;
        const isFromBrowser = dt.getData("fromBrowser") || false;
        const imageSrc = dt.getData('src') || '';
        const files = isFromBrowser && imageSrc !== '' ? [new File([imageSrc], "temp_filename.png", { type: "image/png" })] : Array.from(dt.files);

        const fileInfos = files.map(file => ({
            name: file.name,
            size: file.size,
            type: file.type,
            lastModified: file.lastModified,
            url: isFromBrowser ? imageSrc : URL.createObjectURL(file)
        }));
        clientEmit(value.inputId, fileInfos, 'change');
    };

    // Sadece img suruklemek icin START
    const drag_image = (e) => {
        const dt = e.dataTransfer;
        dt.setData("src", e.target.src);
        dt.setData("fromBrowser", true);
    };
    window.drag_image = drag_image;
    // Sadece img suruklemek icin END
};
""", beforeMain=False)

class drag_drop(uix.Element):
    def __init__(self, id=None):
        super().__init__(id=id)
        self.cls("example")
        with self:
            img = image(id= "drag_img", value="https://picsum.photos/seed/picsum8/200/200").style("margin-right: 1rem;")
            img.get_client_handler_str = lambda event_name: self.get_client_handler_str(event_name)
            img.on("dragstart", lambda ctx, id, value: print(value, id , ctx))
            #img.attrs["draggable"] = "false" # default is true 
            
            self.dropArea = input_image(id=f"{self.id}-input-image-ashjdasd", callback=self.imageUploadDone)
            self.dropArea.style("width:300px; height:300px; border: 2px dashed #ccc; border-radius: 10px; padding: 5px;")    
    # sayfadaki img elementini surukleme islemi basladiginda calisir
    # bu fonksiyonu img elementine ekleyebiliriz
    def get_client_handler_str(self, event_name):
        print(event_name)
        if event_name in ["dragstart"]:
            return f" on{event_name}='window.drag_image(event)'"
        else:
            return super().get_client_handler_str(event_name)
    
    def init(self):
          print(f"init for {self.id}")
          self.session.queue_for_send(
              self.id,
              {
                  'dropAreaId': self.dropArea.id,
                  'inputId': self.dropArea.file.id,
               },
               "drag_drop_elm")

    def imageUploadDone(self, ctx, id, value):
        print(value, 'imageUploadDone')

def drag_drop_input_image_example():
    return drag_drop()
'''
