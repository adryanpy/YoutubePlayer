# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(391, 240)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(90, 40, 89, 25))
        self.backButton.setObjectName("backButton")
        self.thumbnail = QtWidgets.QGraphicsView(self.centralwidget)
        self.thumbnail.setGeometry(QtCore.QRect(0, 0, 81, 81))
        self.thumbnail.setObjectName("thumbnail")
        self.linkAdd = QtWidgets.QLineEdit(self.centralwidget)
        self.linkAdd.setGeometry(QtCore.QRect(90, 100, 191, 25))
        self.linkAdd.setObjectName("linkAdd")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 130, 381, 91))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 379, 89))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setGeometry(QtCore.QRect(0, 0, 381, 41))
        self.widget.setObjectName("widget")
        self.videoTitle_2 = QtWidgets.QLabel(self.widget)
        self.videoTitle_2.setGeometry(QtCore.QRect(0, 0, 291, 41))
        self.videoTitle_2.setObjectName("videoTitle_2")
        self.playButton = QtWidgets.QPushButton(self.widget)
        self.playButton.setGeometry(QtCore.QRect(290, 0, 89, 21))
        self.playButton.setObjectName("playButton")
        self.removeButton = QtWidgets.QPushButton(self.widget)
        self.removeButton.setGeometry(QtCore.QRect(290, 20, 89, 21))
        self.removeButton.setObjectName("removeButton")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(290, 40, 89, 25))
        self.nextButton.setObjectName("nextButton")
        self.videoTitle = QtWidgets.QLabel(self.centralwidget)
        self.videoTitle.setGeometry(QtCore.QRect(100, 10, 181, 17))
        self.videoTitle.setObjectName("videoTitle")
        self.actionButton = QtWidgets.QPushButton(self.centralwidget)
        self.actionButton.setGeometry(QtCore.QRect(190, 40, 89, 25))
        self.actionButton.setObjectName("actionButton")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(290, 100, 89, 25))
        self.addButton.setObjectName("addButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 100, 67, 21))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.videoTitle_2.setText(_translate("MainWindow", "Add music"))
        self.playButton.setText(_translate("MainWindow", "Play"))
        self.removeButton.setText(_translate("MainWindow", "Remove"))
        self.nextButton.setText(_translate("MainWindow", "Next"))
        self.videoTitle.setText(_translate("MainWindow", "Select the music..."))
        self.actionButton.setText(_translate("MainWindow", "Play"))
        self.addButton.setText(_translate("MainWindow", "Add"))
        self.label.setText(_translate("MainWindow", "Link :"))
