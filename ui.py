
import resorce
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        MainWindow.setMinimumSize(QtCore.QSize(400, 400))
        MainWindow.setMaximumSize(QtCore.QSize(400, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 400, 400))
        self.frame.setMinimumSize(QtCore.QSize(400, 400))
        self.frame.setMaximumSize(QtCore.QSize(400, 400))
        self.frame.setStyleSheet("QFrame {background-color: rgb(7,24,73);}\n"
                                 "\n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.git = QtWidgets.QPushButton(self.frame)
        self.git.setGeometry(QtCore.QRect(10, 10, 61, 61))
        self.git.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.git.setStyleSheet("QPushButton {background-color: rgb(18,144,144);\n"
                               "border-radius:30px;}\n"
                               "")
        self.git.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/git.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.git.setIcon(icon)
        self.git.setIconSize(QtCore.QSize(40, 40))
        self.git.setObjectName("git")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(30, 280, 341, 101))
        self.frame_2.setStyleSheet("QFrame {background-color: rgb(19, 36, 85);\n"
                                   "border-radius:10px;}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.mic = QtWidgets.QPushButton(self.frame_2)
        self.mic.setGeometry(QtCore.QRect(130, 20, 91, 71))
        self.mic.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mic.setStyleSheet("QPushButton\n"
                               "{background-color: qlineargradient(spread:pad, x1:0.979211, y1:0.977, x2:0.00526316, y2:0.994, stop:0 rgba(66, 216, 255, 255), stop:0.689474 rgba(119, 172, 254, 255));\n"
                               "border-radius:30px;}\n"
                               "QPushButton::hover{ background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(147, 231, 101, 255), stop:1 rgba(51, 214, 205, 255));\n"
                               " color: rgb(255, 255, 255);}\n"
                               "")
        self.mic.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/micro.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mic.setIcon(icon1)
        self.mic.setIconSize(QtCore.QSize(45, 45))
        self.mic.setObjectName("mic")
        self.exit = QtWidgets.QPushButton(self.frame)
        self.exit.setGeometry(QtCore.QRect(330, 20, 61, 51))
        self.exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit.setStyleSheet("QPushButton\n"
                                "{background-color: qlineargradient(spread:pad, x1:0.979211, y1:0.977, x2:0.00526316, y2:0.994, stop:0 rgba(66, 216, 255, 255), stop:0.689474 rgba(119, 172, 254, 255));\n"
                                "border-radius:25px;}\n"
                                "QPushButton::hover{ background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(147, 231, 101, 255), stop:1 rgba(51, 214, 205, 255));\n"
                                " color: rgb(255, 255, 255);}\n"
                                "")
        self.exit.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/exit.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit.setIcon(icon2)
        self.exit.setIconSize(QtCore.QSize(32, 32))
        self.exit.setObjectName("exit")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(110, 100, 181, 141))
        self.pushButton.setStyleSheet("QPushButton{background-color: rgb(7,24,73);\n"
                                      "border-radius:25px;\n"
                                      "}")
        self.pushButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/Den.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setIconSize(QtCore.QSize(300, 300))
        self.pushButton.setObjectName("pushButton")
        self.frame_2.raise_()
        self.git.raise_()
        self.exit.raise_()
        self.pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
