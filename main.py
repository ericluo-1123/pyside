import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append('..')
from normal import method # type: ignore

from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile, QIODevice, QDir
from ui.ui_test import Ui_MainWindow

import PySide6.QtCore

class HBMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

     # 將你的函數連接到按鈕點擊訊號上
        self.ui.pushButton.clicked.connect(self.say_hello)
        
    def say_hello(self):
        self.ui.pushButton.setText("Hello~~~")

if __name__ == '__main__':

    # Prints PySide6 version
    print(PySide6.__version__)

    # Prints the Qt version used to compile PySide6
    print(PySide6.QtCore.__version__)

    loader = QUiLoader()
    app = QApplication([])
    hb_window = HBMainWindow()
    hb_window.show()
    app.exec()