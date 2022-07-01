import sys
import os

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

#preparing external files
qssFile = open("style.qss", "r")
stringsFile = open("strings.txt", "r")
strings = stringsFile.readlines()

#button functions
def checkForUpdates():
    os.system("gnome-terminal -e 'bash -c \"sudo dnf update\" '")

#def downloadApps():
    #os.system(lorem ipsum)

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Welcome to NuggetOS")

        self.setFixedSize(QSize(700, 500))

        #Main Title saying "Welcome to NuggetOS!"
        self.title1 = QLabel(strings[0], self) #defining the line where the title lies in the "strings.txt" file
        self.title1.setObjectName("title1")
        self.title1.move(25, 30)
        self.title1.resize(900, 150)

        #Subtitle Text
        self.subtitle1 = QLabel(strings[1], self)
        self.subtitle1.setObjectName("subtitle1")
        self.subtitle1.move(30, 110)
        self.subtitle1.resize(650, 50)

        #button1 for checking for updates
        self.button1 = QPushButton('', self)
        self.button1.setIcon(QIcon('updates.png'))
        self.button1.move(35, 150)
        self.button1.resize(312, 100)
        self.button1.setObjectName("button1")
        self.button1.setIconSize(QSize(600, 128))
        self.button1.clicked.connect(checkForUpdates)

        #button2 for downloading apps
        self.button2 = QPushButton('', self)
        self.button2.setIcon(QIcon('appstore.png'))
        self.button2.move(350, 150)
        self.button2.resize(312, 100)
        self.button2.setObjectName("button2")
        self.button2.setIconSize(QSize(600, 128))
        #self.button2.clicked.connect(downloadApps)

        #button2 for downloading apps
        self.button3 = QPushButton('', self)
        self.button3.setIcon(QIcon('appstore.png'))
        self.button3.move(35, 251)
        self.button3.resize(312, 100)
        self.button3.setObjectName("button3")
        self.button3.setIconSize(QSize(600, 128))
        #self.button3.clicked.connect(downloadApps)
        



app = QApplication(sys.argv)
app.setStyleSheet(qssFile.read())

window = MainWindow()
window.show()

app.exec()
