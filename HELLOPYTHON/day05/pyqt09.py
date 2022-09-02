import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("pyqt09.ui")[0]

class App(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # 객체자신.버튼변수이름.클릭시.연결해라.( 실행할 함수 )
        self.pb.clicked.connect(self.btnClick)
    
    def btnClick(self):
        
        answer = ''
        
        first = int( self.le_first.text() )
        last = int( self.le_last.text() )
        
        for i in range( first, last + 1 ):
            for _ in range( 1, i + 1 ):
                print( '*' , end = '' )
                answer += '*'
        
            print()
            answer += '\n'
                
        self.te.setText( answer )    
                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = App()
    myWindow.show()
    app.exec_()