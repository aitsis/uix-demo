from uix.elements import video, source

def video_and_source_example():
    with video('') as video_example:
        video_example.cls("video")
        source("https://ai.ait.com.tr/wp-content/uploads/AI_main-video-with-prompt-.mp4")
    
    return video_example

title = "Source"
description = '''
## source(value,id,media,type)
1. Source elementi.

| attr          | desc                                              |
| :------------ | :------------------------------------------------ |
| id            | Source elementinin id'si                          |
| value         | Source elementinin src'si                       |
| media         | CSS'de normalde tanımlanacak herhangi bir geçerli medya sorgusunu kabul eder. |
| type          | Kaynak dosyanın MIME türü. Örneğin, video/mp4, video/webm veya video/ogg. |
'''