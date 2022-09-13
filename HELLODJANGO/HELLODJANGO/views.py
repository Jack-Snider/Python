from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from HELLODJANGO import daoemp
from HELLODJANGO.daoemp import DaoEmp
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
    
    de = DaoEmp()
    list = de.mylist()
    
    txt =""
    
    for e in list:
        e_id=e['e_id']
        e_name=e['e_name']
        sex=e['sex']
        addr=e['addr']
        
        txt +="{},{},{},{}<br/>".format(e['e_id'],e['e_name'],e['sex'],e['addr'])
        
    return HttpResponse( txt )


def forward( request ):
    a = '홍길동'
    b = [ '전우치','신사임당','대장금' ]
    
   
    
    mylist = [
        
        { 'e_id' : '1',' e_name':'1', 'sex':'1' , 'addr':'1' },
        { 'e_id' : '2',' e_name':'2', 'sex':'2' , 'addr':'2' },
        { 'e_id' : '3',' e_name':'3', 'sex':'3' , 'addr':'3' }
        ]
    
    data = {
        'a' : a,
        'b' : b,
        'data': mylist,
        }
    
    # 장고에는 forward == redner
    return render( request, 'emp.html' , data)

def emp( request ):
    de = daoemp()
    lst = de.mylist()
    
    data = {
        'list':lst
    }
    
    return render( request, 'emp.html' , data)
    


    
    
   
