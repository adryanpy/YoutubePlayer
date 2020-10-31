# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_player(object):
    def __init__(self):
        self.player = QtWidgets.QWidget()
        self.player.setObjectName("player")
        self.player.setWindowModality(QtCore.Qt.WindowModal)
        self.player.setEnabled(True)
        self.player.resize(395, 235)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.player.sizePolicy().hasHeightForWidth())
        self.player.setSizePolicy(sizePolicy)
        self.backButton = QtWidgets.QPushButton(self.player)
        self.backButton.setGeometry(QtCore.QRect(100, 40, 89, 25))
        self.backButton.setObjectName("backButton")
        self.nextButton = QtWidgets.QPushButton(self.player)
        self.nextButton.setGeometry(QtCore.QRect(300, 40, 89, 25))
        self.nextButton.setObjectName("nextButton")
        self.actionButton = QtWidgets.QPushButton(self.player)
        self.actionButton.setGeometry(QtCore.QRect(200, 40, 89, 25))
        self.actionButton.setObjectName("actionButton")
        self.videoTitle = QtWidgets.QLabel(self.player)
        self.videoTitle.setGeometry(QtCore.QRect(100, 10, 181, 17))
        self.videoTitle.setObjectName("videoTitle")
        self.thumbnail = QtWidgets.QGraphicsView(self.player)
        self.thumbnail.setGeometry(QtCore.QRect(10, 0, 81, 81))
        self.thumbnail.setObjectName("thumbnail")
        self.linkAdd = QtWidgets.QLineEdit(self.player)
        self.linkAdd.setGeometry(QtCore.QRect(90, 100, 191, 25))
        self.linkAdd.setObjectName("linkAdd")
        self.addButton = QtWidgets.QPushButton(self.player)
        self.addButton.setGeometry(QtCore.QRect(290, 100, 89, 25))
        self.addButton.setObjectName("addButton")
        self.label = QtWidgets.QLabel(self.player)
        self.label.setGeometry(QtCore.QRect(10, 100, 67, 21))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.player)
        self.comboBox.setGeometry(QtCore.QRect(90, 160, 191, 25))
        self.comboBox.setObjectName("comboBox")
        self.playButton = QtWidgets.QPushButton(self.player)
        self.playButton.setGeometry(QtCore.QRect(290, 160, 89, 21))
        self.playButton.setObjectName("playButton")
        self.removeButton = QtWidgets.QPushButton(self.player)
        self.removeButton.setGeometry(QtCore.QRect(290, 200, 89, 21))
        self.removeButton.setObjectName("removeButton")
        self.label_2 = QtWidgets.QLabel(self.player)
        self.label_2.setGeometry(QtCore.QRect(10, 160, 67, 21))
        self.label_2.setObjectName("label_2")

        QtCore.QMetaObject.connectSlotsByName(self.player)
        _translate = QtCore.QCoreApplication.translate
        self.player.setWindowTitle(_translate("self.player", "Youtube self.player"))
        self.backButton.setText(_translate("self.player", "Back"))
        self.nextButton.setText(_translate("self.player", "Next"))
        self.actionButton.setText(_translate("self.player", "Play"))
        self.videoTitle.setText(_translate("self.player", "Select the music..."))
        self.addButton.setText(_translate("self.player", "Add"))
        self.label.setText(_translate("self.player", "Link :"))
        self.playButton.setText(_translate("self.player", "Play"))
        self.removeButton.setText(_translate("self.player", "Remove"))
        self.label_2.setText(_translate("self.player", "Playlist:"))
