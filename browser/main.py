from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class MyWebBrowser(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MyWebBrowser, self).__init__(*args, **kwargs)

        self.window = QWidget()
        self.window.setWindowTitle("Odyssey Web Browser")
