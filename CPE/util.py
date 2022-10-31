from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QHBoxLayout, QPushButton

import sys
import requests
import lxml
# from bs4 import BeautifulSoup

url = "https://cpe.cse.nsysu.edu.tw/cpe/test_data/problems"
f = requests.get(url)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.firstLabel = QLabel()
        self.firstLabel.setText("URL:")
        self.firstInput = QLineEdit()
        
        self.secondLabel = QLabel()
        self.secondLabel.setText("Path:")
        self.secondInput = QLineEdit()

        self.submit = QPushButton()
        self.submit.setText("Click to submit")
        self.submit.clicked.connect(self.processClick)

        mainLayout = QVBoxLayout()

        firstRow = QHBoxLayout()
        firstRow.addWidget(self.firstLabel)
        firstRow.addWidget(self.firstInput)

        secondRow = QHBoxLayout()
        secondRow.addWidget(self.secondLabel)
        secondRow.addWidget(self.secondInput)

        thirdRow = QHBoxLayout()
        thirdRow.addWidget(self.submit)

        mainLayout.addLayout(firstRow)
        mainLayout.addLayout(secondRow)
        mainLayout.addLayout(thirdRow)

        container = QWidget()
        container.setLayout(mainLayout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)
    
    def processClick(self):
        myLink = self.firstInput.text()
        print("Button is clicked")
        print("Link is: ", myLink)