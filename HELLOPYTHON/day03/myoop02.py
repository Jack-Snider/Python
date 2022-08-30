"""
    
    클래스 다중 상속
    

"""

# 이재용 클래스
class LeeJY:
    
    # 생성자로 재산 설정 ( 5조 )
    def __init__(self):
        self.money = 10
        
    # 폰 팔아서 돈 벌기    
    def phonepari(self):
        self.money += 5

# 바이든 클래스    
class Byden:
    
    # 전쟁하고 있는 수
    def __init__(self):
        self.cnt_war = 1 
        
    # 법큐 하나 날릴때마다 전쟁 증가        
    def bubkyu(self, cnt):
        self.cnt_war += cnt    
        
# 위의 둘의 속성을 전부 상속받는 형준
class HyungJ( LeeJY, Byden ):
    
    def __init__(self):
        
        LeeJY.__init__(self)
        Byden.__init__(self)
        

hyung = HyungJ()

print( f'hyung.money = { hyung.money }' )

hyung.phonepari()

print( f'Money after phonepari...' )
print( f'hyung.money = { hyung.money }' )

print( f'hyung.cnt_war = { hyung.cnt_war }' )
hyung.bubkyu( 2 )
print( f'After bubkyu with parameter 2...' )
print( f'hyung.cnt_war = { hyung.cnt_war }' )
    
        
    
    