import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("pyqt07.ui")[0]

class App(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # 객체자신.버튼변수이름.클릭시.연결해라.( 실행할 함수 )
        self.pb.clicked.connect(self.btnClick)
    
    def btnClick(self):
        
        dan = int( self.le.text() )
        
        answer = ''
        
        for i in range( 1, 9 + 1 ):
            answer += f'{ dan } x { i } = { dan * i } \n'
        
        print( answer )
        
        self.te.setText( answer )
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = App()
    myWindow.show()
    app.exec_()