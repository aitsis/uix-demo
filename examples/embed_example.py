from uix.elements import embed
from uix.elements._embed import title, description, sample as code

def embed_example():
    embed("https://ai.ait.com.tr/wp-content/uploads/AI_main-video-with-prompt-.mp4", id="myEmbed", type="video/webm", width="300", height="200")
    embed("https://aitools.ait.com.tr/AIT_AI_LOGO.png", type="image/png", width="200", height="100")