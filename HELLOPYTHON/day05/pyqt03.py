import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("pyqt03.ui")[0]

class App(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # 객체자신.버튼변수이름.클릭시.연결해라.( 실행할 함수 )
        self.pb.clicked.connect(self.btnClick)
    
    def btnClick(self):
        
        print( 'btnClick' )
        
        # leA, leB, leC, pb
        
        a = int( self.leA.text() )
        b = int( self.leB.text() )
        
        self.leC.setText( str( a * b ) )
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = App()
    myWindow.show()
    app.exec_()