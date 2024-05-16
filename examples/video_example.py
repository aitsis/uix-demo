from uix.elements import video

def video_example():
    video_example = video("",src="https://ai.ait.com.tr/wp-content/uploads/AI_main-video-with-prompt-.mp4").cls("video")
    return video_example

title = "Video"

description = """
## video(id,loop,autoplay,muted)
1. Html'de video elementine karşılık gelir. İçerisine source elementleri eklenerek kullanılır.

| attr          | desc                                             |
| :------------ | :------------------------------------------------|
| id            | Video elementinin id'si                          |
| loop          | Video elementinin sürekli oynatılması            |
| autoplay      | Video elementinin otomatik oynatılması           |
| muted         | Video elementinin sesinin kapatılması            |
"""