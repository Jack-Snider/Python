class Academy:
    
    # 생성자
    def __init__( self ):
        print( 'Constructor' )
        self.cnt_student = 0
        
    # 소멸자 ( 메모리를 해제하는 역할을 함, 자바에서 GC의 역할 )
    # 프로그램이 끝나는 시점에 __del__()함수가 실행됨.        
    def __del__( self ):    
        print( 'Destroyer' )
        
    # Java에서 toString같은 느낌. 객체를 출력했을때 출력될 문자열    
    def __str__( self ):
        return 'self.cnt_student : ' + str( self.cnt_student )
    
        
    def openClass( self ):
        self.cnt_student += 20
    

if __name__ == '__main__':
    
    a = Academy()
    a.openClass()
    print( a )

    
