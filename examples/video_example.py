from uix.elements import video, source
from uix.elements._video import title, description, sample as code

def video_example():
    video_example = video("",src="https://ai.ait.com.tr/wp-content/uploads/AI_main-video-with-prompt-.mp4").cls("video")
    
    return video_example