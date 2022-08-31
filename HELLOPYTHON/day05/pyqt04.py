import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

form_class = uic.loadUiType("pyqt04.ui")[0]

class App(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # 객체자신.버튼변수이름.클릭시.연결해라.( 실행할 함수 )
        self.pb.clicked.connect(self.btnClick)
    
    def btnClick(self):
        
        lotto = set()
        
        while len( lotto ) != 6:
            
            n = random.randrange( 1, 45 + 1 )
            
            lotto.add( n )
        
        
        lotto = list( lotto )
        
        print( lotto )
        
        self.le1.setText( str( lotto[0] ) )
        self.le2_2.setText( str( lotto[1] ) )
        self.le3.setText( str( lotto[2] ) )
        self.le4.setText( str( lotto[3] ) )
        self.le5.setText( str( lotto[4] ) )
        self.le6.setText( str( lotto[5] ) )
            
            
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = App()
    myWindow.show()
    app.exec_()