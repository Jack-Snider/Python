import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

form_class = uic.loadUiType("pyqt05.ui")[0]

class App(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # 객체자신.버튼변수이름.클릭시.연결해라.( 실행할 함수 )
        self.pb.clicked.connect(self.btnClick)
        #self.lemine.returnPressed.connect( self.btnClick() )
    
    def btnClick(self):
        
        user = self.lemine.text()
        
        print( f'사용자 : { user }' )
        
        computer = [ '가위','바위','보' ]
        n = random.randint( 0 , 3 )
      
        com = computer[ n ]
      
        print( f'컴퓨터 : { com }' )
      
        result = ''
        if user == com:
            result = '무승부'
        elif user == '가위' and com == '바위':
            result = '컴퓨터 승'
        elif user == '가위' and com == '바위':
            result = '사용자 승'
        elif user == '바위' and com == '가위':
            result = '사용자 승'
        elif user == '바위' and com == '보':
            result = '컴퓨터 승'
        elif user == '보' and com == '가위':
            result = '컴퓨터 승'
        elif user == '보' and com == '바위':
            result = '사용자 승'
        
        # lblmine, lblcom, lblres
        # lemine, lecom, leres
        # pb
        
        print( f'결과 : { result }' )
        
        self.lecom.setText( com )
        self.leres.setText( result )
          
      
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = App()
    myWindow.show()
    app.exec_()
    
    
    