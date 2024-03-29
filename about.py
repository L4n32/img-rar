from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow):
        AboutWindow.setObjectName("AboutWindow")
        AboutWindow.setEnabled(True)
        AboutWindow.setFixedSize(281, 96)
        AboutWindow.setAutoFillBackground(False)

        if os.path.isfile("icon.ico"):
            AboutWindow.setWindowIcon(QtGui.QIcon('icon.ico'))

        self.centralwidget = QtWidgets.QWidget(AboutWindow)
        self.centralwidget.setObjectName("centralwidget")

        font = QtGui.QFont()
        font.setPointSize(14)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 61, 21))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setOpenExternalLinks(True)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 81, 21))
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 261, 31))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        AboutWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AboutWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 281, 21))
        self.menubar.setObjectName("menubar")
        AboutWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AboutWindow)
        self.statusbar.setObjectName("statusbar")
        AboutWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AboutWindow)
        QtCore.QMetaObject.connectSlotsByName(AboutWindow)

    def retranslateUi(self, AboutWindow):
        _translate = QtCore.QCoreApplication.translate
        AboutWindow.setWindowTitle(_translate("AboutWindow", "About"))
        self.label_2.setText(_translate("AboutWindow", "<a href='https://github.com/L4n32/img-rar'>Source</a>"))
        self.label.setText(_translate("AboutWindow", "IMG-RAR"))
        self.label_3.setText(_translate("AboutWindow", "Copyright © 2023-2024 L4n32"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AboutWindow = QtWidgets.QMainWindow()
    Ui_AboutWindow().setupUi(AboutWindow)
    AboutWindow.show()
    sys.exit(app.exec_())
