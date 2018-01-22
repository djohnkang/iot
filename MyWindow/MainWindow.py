import sys
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self, left=100, top=100, width=640, height=480):
        super().__init__()
        self.title = 'PyQt5 status bar example - pythonspot.com'
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.status('Message in statusbar.')
        self.show()


    def status(self, msg):
        self.statusBar().showMessage(msg)

    def messageBox(self, title='', msg=''):
        return QMessageBox.question(self,
                title, msg,
                QMessageBox.Yes | QMessageBox.No)

if __name__ =='__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())