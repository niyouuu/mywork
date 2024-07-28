from login import *
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

class Loginwindow(QMainWindow):
  def __init__ (self):
   super().__init__()
   self.ui = Ui_MainWindow()
   self.ui.setupUi(self)
   self.setWindowFlag(QtCore.Qt.FranelessWindowHint)
   self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
   self.show()

if __name__ =='__main__':
   app = QApplication(sys.argv)
   # win = LoginWindow()
   sys.exit(app.exec_())