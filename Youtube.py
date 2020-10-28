import youtube_dl

class YouTube(object):
    """
    docstring
    """
    def __init__(self, url=""):
        self.url = url
        self.youtube_options = {
            'format' : 'bestaudio/best',
            'outtmpl': 'playing.webm',
            'postprocessors' : [{
                'key' : 'FFmpegExtractAudio',
                'preferredcodec' : 'mp3',
                'preferredquality' : '192'
            }]
        }

    def get_video(self, url):
        youtube = youtube_dl.YoutubeDL(self.youtube_options)
        youtube.download([url])