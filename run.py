import assistant
from ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTime, QTimer, QDate
from PyQt5.uic import loadUiType
import os
import sys
import webbrowser as web


class MainThread(QThread):

    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        assistant.assisrun()


startExe = MainThread()


class Gui_start(QMainWindow):

    def __init__(self):
        super().__init__()
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)
        self.gui.mic.clicked.connect(self.start)
        self.gui.exit.clicked.connect(self.close)
        self.gui.git.clicked.connect(self.chrome_app)

    def chrome_app(self):
        web.open("https://github.com/ayushsaini12/DenTheAssistant")

    def start(self):
        startExe.start()


GuiApp = QApplication(sys.argv)
assistantui = Gui_start()
assistantui.show()
exit(GuiApp.exec_())
