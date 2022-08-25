import random


arr4 =   [
            1,2,3,4,5,          6,7,8,9,10,
            11,12,13,14,15,     16,17,18,19,20,
            21,22,23,24,25,     26,27,28,29,30,
            31,32,33,34,35,     36,37,38,39,40,
            41,42,43,44,45
        ]
arr2 = []

while True:
    rnd = int( random.random() * 45 )
    
    if arr4[ rnd ] == -1:
        pass
    else:
        arr2.append(  arr4[ rnd ] )
        arr4[ rnd ] = -1
        
    if len( arr2 ) >= 6:
        break

print( arr2 )