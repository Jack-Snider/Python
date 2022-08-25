import random

user = input( ' \'홀\' 아니면  \'짝\'  : ' )

computer = int( random.random() * 2 )

if computer == 1:
    computer = '홀'
else:
    computer = '짝'

print( f'컴퓨터 : { computer }' )
print( f'사용자 : { user }' )

if user == computer:
    print( '사용자 승리' )
else:
    print( '컴퓨터 승리' )
