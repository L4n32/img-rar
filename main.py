__author__ = "Hummingbird Studio™"
__copyright__ = "Copyright © 2023-2024 L4n32"
__version__ = "1.0"

from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import filedialog
from about import Ui_AboutWindow
import os

class Ui_MainWindow(object):
    def About_window(self):
        self.window_about = QtWidgets.QMainWindow()
        self.ui = Ui_AboutWindow().setupUi(self.window_about)
        self.window_about.show()
    def open_rar(self):
        global rar
        filepath = filedialog.askopenfilename(filetypes=[("RAR files", '*.rar'),
            ("ZIP files", '*.zip'), ("7z files", '*.7z'), ("ARJ files", '*.arj'), 
            ("CAB files", '*.cab'), ("TAR files", '*.tar'), ("LZH files", '*.lzh'),
            ("LZ files", '*.lz'), ("GZip files", '*.gzip'), ("TAR files", '*.tar'), 
            ("UUE files", '*.uue'), ("ISO files", '*.iso'), ("BZIP2 files", '*.BZIP2'), 
            ("BZIP2 files", '*.bzip2'), ("XZ files", '*.xz'), ("Z files", '*.z'), 
            ("BZ2 files", '*.bz2'), ("GZ files", '*.gz'), 
            ("ZIPX files", '*.zipx'), ("ZST files", '*.zst'), 
            ("001 files", '*.001'), ("All files", "*")], title="Choose file name")
        if filepath != "":
            with open(filepath, "r") as file:
                rar = filepath.replace('/', '\\')
                print(rar)

    def open_img(self):
        global img
        filepath = filedialog.askopenfilename(filetypes=[("JPG files", '*.jpg'), 
            ("PNG files", '*.png'), ("GIF files", '*.gif'),("TIFF files", '*.tiff'), 
            ("BMP files", '*.bmp'), ("SVG files (File error)", '*.svg'), 
            ("WEBP files", '*.webp'), ("AI files", '*.ai'), ("CDR files", '*.cdr'), 
            ("HEIF files", '*.heif'), ("AVIF files", '*.avif'), ("ICO files", '*.ico'), 
            ("ICNS files", '*.icns'), ("All files", "*")], title="Choose file name")
        if filepath != "":
            with open(filepath, "r") as file:
                img = filepath.replace('/', '\\')
                print(img)

    def save_file(self):
        filepath = filedialog.asksaveasfilename(initialfile='output.jpg', 
            filetypes=[("JPG files", '*.jpg'), ("PNG files", '*.png'), 
            ("GIF files", '*.gif'), ("TIFF files", '*.tiff'), ("BMP files", '*.bmp'), 
            ("PSD files", '*.psd'), ("SVG files (File error)", '*.svg'), 
            ("WEBP files", '*.webp'), ("AI files", '*.ai'), ("CDR files", '*.cdr'), 
            ("HEIF files", '*.heif'), ("AVIF files", '*.avif'), ("ICO files", '*.ico'), 
            ("ICNS files", '*.icns'), ("All files", "*"),], title="Choose file name")
        if filepath != "":
            with open(filepath, "w") as file:
                output = filepath.replace('/', '\\')
                img.encode()
                rar.encode()
                output.encode()
        os.system(f"type {img} {rar} > {output}")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setFixedSize(240, 72)

        if os.path.isfile("icon.ico"):
            MainWindow.setWindowIcon(QtGui.QIcon('icon.ico'))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        font = QtGui.QFont()
        font.setPointSize(14)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 81, 51))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.open_rar())

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 0, 81, 51))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.open_img())

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 0, 81, 51))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda: self.save_file())

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        MainWindow.setMenuBar(self.menubar)

        MenuFile = self.menubar.addMenu("File")
        SubmenuFile_Archive = MenuFile.addAction("Archive...")
        SubmenuFile_Archive.triggered.connect(lambda: self.open_rar())
        SubmenuFile_Image = MenuFile.addAction("Image...")
        SubmenuFile_Image.triggered.connect(lambda: self.open_img())
        SubmenuFile_Save = MenuFile.addAction("Save...")
        SubmenuFile_Save.triggered.connect(lambda: self.save_file())
        MenuFile.addSeparator()
        SubmenuFile_Exit = MenuFile.addAction("Exit")
        SubmenuFile_Exit.triggered.connect(lambda: sys.exit())

        MenuHelp = self.menubar.addMenu("Help")
        SubmenuHelp_About = MenuHelp.addAction("About")
        SubmenuHelp_About.triggered.connect(lambda: self.About_window())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "img-rar"))
        self.pushButton.setText(_translate("MainWindow", "Archive"))
        self.pushButton_2.setText(_translate("MainWindow", "Image"))
        self.pushButton_3.setText(_translate("MainWindow", "Save"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    Ui_MainWindow().setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
