from urllib import parse
import youtube_dl
import urllib3
import json
import os
import re

URL_PARAMS = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

YOUTUBE_TOKEN = "AIzaSyC9LvSGiTi9y1P0WpkfQuDU03JoqOqs5-0"
YOUTUBE_API_URL = "https://youtube.googleapis.com/youtube/v3/"

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

    def get_video_details(self, video_id):
        http = urllib3.PoolManager()
        response = http.request("GET", YOUTUBE_API_URL+"videos?part=snippet&id="+str(video_id)+"&key="+str(YOUTUBE_TOKEN))
        video_details = {}

        if response.status == 200:
            data = response.data.decode()
            data = json.loads(data)
            for item in data["items"]:
                video_details = {
                        "video_id": item["id"],
                        "title": item["snippet"]["title"],
                        "thumbnail": item["snippet"]["thumbnails"]["high"],
                        "description": item["snippet"]["description"]
                    }

        return video_details

    def get_playlist_details(self, playlist_id):
        http = urllib3.PoolManager()
        response = http.request("GET", YOUTUBE_API_URL+"playlistItems?part=snippet&maxResults=10000&playlistId="+str(playlist_id)+"&key="+str(YOUTUBE_TOKEN))
        videos_details = []

        if response.status == 200:
            data = response.data.decode()
            data = json.loads(data)
            for item in data["items"]:
                videos_details.append(
                    {
                        "video_id": item["snippet"]["resourceId"]["videoId"],
                        "title": item["snippet"]["title"],
                        "thumbnail": item["snippet"]["thumbnails"]["high"],
                        "description": item["snippet"]["description"]
                    }
                )
        return videos_details

    def get_url_information(self, url):
        if re.match(URL_PARAMS, url) is not None:
            response = {}
            params = dict(parse.parse_qsl(parse.urlsplit(url).query))

            if "list" in params:
                response["type"] = "playlist"
                response["videos"] = self.get_playlist_details(params["list"])

            elif "v" in params:
                response["type"] = "video"
                response["video"] = self.get_video_details(params["v"])

            else:
                return False, {"message":"URL não apresenta um vídeo ou playlist válodos"}
            

            
            return True, response
            
        return False, {"message":"URL inválida"}