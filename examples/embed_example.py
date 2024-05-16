from uix.elements import embed

def embed_example():
    embed("https://ai.ait.com.tr/wp-content/uploads/AI_main-video-with-prompt-.mp4", id="myEmbed", type="video/webm", width="300", height="200")
    embed("https://aitools.ait.com.tr/AIT_AI_LOGO.png", type="image/png", width="200", height="100")

title = "Embed"
description = '''
# embed(value,id,type,width,height)
1. Embed elementi. Html'deki embed elementine karşılık gelir.

| attr          | desc                                                        |
| :------------ | :------------------------------------------------           |
| id            | Embed elementinin id'si                                     |
| value         | Embed elementinin içeriği                                   |
| type          | Embed elementinin tipi(video/webm, image/png, default: None!|             
| width         | Embed elementinin genişliği                                 |
| height        | Embed elementinin yüksekliği                                |
'''