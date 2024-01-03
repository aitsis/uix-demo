from uix.elements import video, source
from uix.elements._source import title, description, sample as code
def video_and_source_example():
    with video('') as video_example:
        video_example.cls("video")
        source("https://ai.ait.com.tr/wp-content/uploads/AI_main-video-with-prompt-.mp4")
    
    return video_example