from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

# 자바에서 디스패치역할
def hello( request ):
    #return render( request, 'hello.html' )
    return HttpResponse( 'Hello Jack Snider!' )
