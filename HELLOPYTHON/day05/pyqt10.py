import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

form_class = uic.loadUiType("pyqt10.ui")[0]

class App(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # 객체자신.버튼변수이름.클릭시.연결해라.( 실행할 함수 )
        self.pb.clicked.connect(self.btnClick)
    
    def btnClick(self):
        
        strike = 0
        ball = 0
        out = 0
        
        user = list( self.lemine.text() )
        print( user )
        user = list( map( int, user ) )
        print( user )
        com = []
        for _ in range( 3 ):
            com.append( random.randint( 0, 9 + 1 ) )
        
        print( com )
        
        for i in range( 0,len( user ) ):
            for j in range( 0,len( com ) ):
                if user[i] == com[i]:
                    strike += 1
                    break
                elif user[i] == com[j]:
                    print( f'{ user[i] }, { com[j] }' )
                    ball += 1
                    break
                else:
                    out += 1
                    break
        
        
        answer = f'사용자 : { user } \n'
        answer += f'컴퓨터 : { com } \n'
        answer += '\n'
        answer += f'{ strike } STRIKE \n{ ball } BALL \n{ out } OUT'
                
        print( f'사용자 : { user }' )
        print( f'컴퓨터 : { com }' )        
        print( f'결과 : { strike } STRIKE - { ball } BALL - { out } OUT' )
        
        self.textEdit.setText( answer )
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = App()
    myWindow.show()
    app.exec_()
    print( 'Hello world' )