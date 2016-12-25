import webbrowser
import video
class Movie(video.Video):
    def __init__(self, title, storyline, poster_image, trailer_youtube_url):
        video.Video.__init__(self, title, storyline)
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
