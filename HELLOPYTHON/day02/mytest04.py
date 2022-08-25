import random

lotto = set()

while len( lotto ) != 6:
    
    number = random.randrange( 1, 45 + 1 )
    
    lotto.add( number )
    
lotto = list( lotto )
print( lotto )
    
