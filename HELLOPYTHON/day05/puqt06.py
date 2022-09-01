import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("pyqt03.ui")[0]

class App(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.numbers = ''
        
        # 객체자신.버튼변수이름.클릭시.연결해라.( 실행할 함수 )
        self.pb1.clicked.connect(self.btnClick1)
        self.pb2.clicked.connect(self.btnClick2)
        self.pb3.clicked.connect(self.btnClick3)
        self.pb4.clicked.connect(self.btnClick4)
        self.pb5.clicked.connect(self.btnClick4)
        self.pb6.clicked.connect(self.btnClick6)
        self.pb7.clicked.connect(self.btnClick7)
        self.pb8.clicked.connect(self.btnClick8)
        self.pb9.clicked.connect(self.btnClick9)
        

    def btnClick1(self):
        self.le.setTest(   )
 
    def btnClick2(self):
        pass
    
    def btnClick3(self):
        pass
    
    def btnClick4(self):
        pass
    
    def btnClick5(self):
        pass
    
    def btnClick6(self):
        pass
    
    def btnClick18(self):
        pass
    
    def btnClick8(self):
        pass
        
        
        
        
     
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = App()
    myWindow.show()
    app.exec_()