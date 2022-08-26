"""
    Writer : Jack Snider
    Date : 2022-08-26
    About : Rock, Scissors, Paper
"""
import random
from sqlalchemy.dialects import oracle


# return 0 : user wins, return 1 : computer wins
def play( user, computer ):
    
    if ( user == 1 and computer == 2 ) or ( user == 2 and computer == 3 ) or ( user == 3 and computer == 1 ):
        # 사용자가 지는 상황
        return 0
    elif ( user == 1 and computer == 3 ) or ( user == 2 and computer == 1 ) or ( user == 3 and computer == 2 ):
        # 사용자가 이기는 상황
        return 1
    else:
        # 무승부
        return 2
    
    

lst = [ '가위','바위','보' ]

user = int( input( '1. 가위 2. 바위. 3. 보 => ' ) )
computer = int( random.random() * 3 )
print( f'computer : { lst[ computer - 1 ] }' )

if play( user, computer ) == 0:
    print( '컴퓨터가 이겼습니다.' )
elif play( user, computer ) == 1:
    print( '사용자가 이겼습니다.' )
else:
    print( '무승부입니다.' )


