def showDan( dan ):

    print( f'=============== { dan }단 ===============' )    
    for idx in range( 1, 9 + 1 ):
        print( f'{ dan } x { idx } = { dan * idx }' )
    print( f'===================================')

showDan( 5 )