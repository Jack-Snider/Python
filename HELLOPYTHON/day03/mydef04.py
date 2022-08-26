def allgugudan():
    
    for dan in range( 2, 9 + 1 ):
        print( f'================= { dan } =================' )
        for idx in range( 1, 9 + 1 ):
            print( f'{ dan } x { idx } = { dan * idx }' )
        
        print( '========================================' )
    
allgugudan()