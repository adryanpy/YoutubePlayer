from playsound import playsound
from Search import Search
from Youtube import YouTube
import os

search = Search()
youtube = YouTube("")

while True:
    keyword = str(input("Procurar música: "))
    lista = search.find(keyword)
    for item in lista:
        try:
            youtube.get_video(item)
            playsound("playing.mp3")
            os.system("rm playing.mp3")
            break;
        except Exception as e:
            pass