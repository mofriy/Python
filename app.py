import sys
import PyQt5.QtWidgets as qw
import time
import requests
from PyQt5.QtCore import pyqtSlot
 

class MainWindow(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
 
 
    def initUI(self):
        self.resize(250, 250)
        self.move(300, 300)
        self.setWindowTitle('Sync')
 
        self.go1Btn = qw.QPushButton('1', self)
        self.go1Btn.move(50, 50)
        self.go1Btn.clicked.connect(self.firstOperation)

        self.go2Btn = qw.QPushButton('2', self)
        self.go2Btn.move(90, 75)
        self.go2Btn.clicked.connect(self.secondOperation)

        self.go3Btn = qw.QPushButton('3', self)
        self.go3Btn.move(130, 100)
        self.go3Btn.clicked.connect(self.thirdOperation)

        self.goPentagonBtn = qw.QPushButton('BZLOMATb Pentagon', self)
        self.goPentagonBtn.move(50, 150)
        self.goPentagonBtn.clicked.connect(self.pentagonOperation)

        self.quitBtn = qw.QPushButton('Quit', self)
        self.quitBtn.move(170, 200)
        self.quitBtn.clicked.connect(self.close)
 
 
    @pyqtSlot(bool)
    def firstOperation(self, evt):
        print(1)

    @pyqtSlot(bool)
    def secondOperation(self, evt):
        print(2, 2)
    
    @pyqtSlot(bool)
    def thirdOperation(self, evt):
        print(3, 3, 3)

    @pyqtSlot(bool)
    def pentagonOperation(self, evt):
        for i in range(10):
            print('.', end=' ')
            time.sleep(1)
        link = requests.get('https://www.whitehouse.gov/')
        print('Oops, there are', len(link.content), 'bytes')
        
        s = "I can't 'VZLOMATb' this, b-baka!"
        for i in s:
            print(i, end = '')
            time.sleep(0.05)
        print()
        

if __name__ == '__main__':
    app = qw.QApplication(sys.argv)
    w = MainWindow()
    w.show()

    sys.exit(app.exec_())
