"""
    
    파이썬 Class 연습

"""

class Animal:
    
    def __init__( self ):
        self.flagMove = True
        
    def die( self ):
        self.flagMove = False
    

class Human( Animal ):
    
    def __init__( self ):
        super().__init__()
        
        self.skill_tool = 0
        
        
    def momstouch( self, stroke ):
        self.skill_tool += stroke



human = Human() # Human 클래스 객체 생성

print( human.flagMove ) # flagMove는 Human클래스가 상속받은 부모클래스 Animal의 필드
print( human.skill_tool ) # skill_tool은 Human클래스의 필드

human.die() # 부모클래스인 Animal클래스의 function

human.momstouch( 10 )

print( human.flagMove )
print( human.skill_tool )



