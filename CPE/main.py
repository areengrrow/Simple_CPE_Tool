from util import *
from PyQt5 import QtWidgets
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("CPE tool")
    app.setStyle('Fusion')
    myWindow = MainWindow()
    myWindow.show()

    sys.exit(app.exec())