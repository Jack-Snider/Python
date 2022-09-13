'''
Created on 2022. 9. 7.

@author: PC-04
'''

from django.shortcuts import render
from django.http.response import JsonResponse
from SPA_EMP.daoemp import DaoEmp
from conda.base.context import context


de = DaoEmp()

def emp_deelete_ajax( request ):
    
    e_id = request.POST[ "e_id" ]
    
    de = DaoEmp()
    cnt = de.mydelete( e_id )
    
    context = {
        'cnt' : cnt
    }
    
    return JsonResponse( context );

def emp_update_ajax( request ):
    
    e_id = request.POST[ "e_id" ]
    e_name = request.POST[ "e_name" ]
    sex = request.POST[ "sex" ]
    addr = request.POST[ "addr" ]
    
    de = DaoEmp()
    cnt = de.myupdate( e_id, e_name, sex, addr )
    context = {
            'cnt' : cnt
    }

    return JsonResponse( context )

def emp_insert_ajax( request ):
    
    e_id = request.POST[ "e_id" ]
    e_name = request.POST[ "e_name" ]
    sex = request.POST[ "sex" ]
    addr = request.POST[ "addr" ]
    
    de= DaoEmp()
    cnt = de.myinsert( e_id, e_name, sex, addr )
    context = {
        'cnt' : cnt
    }


    return JsonResponse( cnt )

def emp_detail_ajax( request ):

    e_id = request.GET.get( 'e_id','000' )
    de = DaoEmp()
    emp = de.myone( e_id )
    context = {
        'emp' : emp
    }
    
    return JsonResponse( context )
    
    
def emp( request ):
     
    #return render( request, 'emp.html' )
    lst = de.mylist()
    
    data = {
        'list':lst
    }
    
    print(lst)
    
    # json 타입으로 ajax한테 다시 넘겨준다.  
    return JsonResponse( data )

def emp_list_ajax( request ):
    
    lst = de.mylist()
    
    data = {
        'list':lst
    }
    
    print(lst)
    
    # json 타입으로 ajax한테 다시 넘겨준다.  
    return JsonResponse( data )



def test2( request ):
    
    return render( request, 'test2.html' )

def test3( request ):
    
    return render( request, 'test3.html' )

def test4( request ):
    
    return render( request, 'test4.html' )

def test6( request ):
    
    return render( request, 'jqtest6.html' )