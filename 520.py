import sys
from Ui_520 import *
from PyQt6.QtWidgets import QMainWindow,QApplication,QMessageBox
from PyQt6.QtGui import *
import webbrowser

class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent =None):
        super(MyMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.released.connect(self.OpenHTML)
    def OpenHTML(self):
        webbrowser.open("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec())