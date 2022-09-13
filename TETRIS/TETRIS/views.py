'''
Created on 2022. 9. 13.

@author: PC-04
'''
from django.shortcuts import render

def tetris( request ):
    
    # tetris01.html
    # tetris02.html
    return render( request, 'tetris03.html' )