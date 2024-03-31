from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

from settings import Settings

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.settings = Settings()
        
        self.setWindowTitle(self.settings.main_window_label)
        self.setGeometry(*self.settings.main_window_geometry)
        self.initUI()


    def initUI(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())        