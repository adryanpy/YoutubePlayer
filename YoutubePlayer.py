from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from pygame import mixer
from playsound import playsound
from Search import Search
from Youtube import YouTube
from ui import main
import sys
import os

search = Search()
youtube = YouTube("")
music = []

class Config(object):
    def __init__(self):
        self.index = 0
        self.action = True

mixer.init()
config = Config()

app = QApplication(sys.argv)

main_window = main.Ui_player()

def addLink():
    if not main_window.linkAdd.text() == "":
        status, data = youtube.get_url_information(main_window.linkAdd.text())
        if status:
            if data['type'] == "video":
                music.append(data['video'])
                main_window.comboBox.insertItem(music.index(data['video']), data['video']['title'])
            else:
                for video in data['videos']:
                    music.append(video)
                    main_window.comboBox.insertItem(music.index(video), video['title'])

def next():
    config.index+=1
    config.action = True
    if config.index == len(music):
        config.index = 0
    play()

def back():
    config.index-=1
    config.action = True
    if config.index < 0:
        config.index = 0
    play()

def play():
    if config.action:
        main_window.actionButton.setText("Pause")
        youtube.get_video(music[config.index]['video_id'])
        main_window.videoTitle.setText(music[config.index]['title'])
        mixer.music.load('playing.wav')
        mixer.music.play()
    else:
        main_window.actionButton.setText("Play")
        mixer.music.pause()
    
    config.action = not config.action
    pass

main_window.addButton.clicked.connect(addLink)
main_window.actionButton.clicked.connect(play)
main_window.nextButton.clicked.connect(next)
main_window.backButton.clicked.connect(back)

main_window.player.show()

app.exec_()