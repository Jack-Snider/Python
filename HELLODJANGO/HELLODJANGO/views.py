from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import pymysql

# Create your views here.

# 자바에서 디스패치역할
def hello( request ):
    #return render( request, 'hello.html' )
    return HttpResponse( 'Hello Jack Snider!' )

@csrf_exempt
def myparam( request ):
    
    # 끝에 000은 get방식으로 파라미터가 아에 없을때는 default로 000으로 하겠다는 뜻
    #p = request.GET.get( 'a' , '000')
    p = request.GET.get( 'a' , '000')
    return HttpResponse( f'param : { p }' )

def db( request ):
    
    con = pymysql.connect(
            host="localhost",
            user="root",
            password="python",
            db = 'python',
            charset="utf8",
            port = 3305 )
    
    # 파이썬에서 커서는 자바에서의 Statement 역할을 한다.
    cur = con.cursor()

    sql = 'SELECT * FROM emp'
    cur.execute( sql )
    rows = cur.fetchall()
    

    cur.close()
    con.close()
    
    return HttpResponse( f'{ rows }' )
    