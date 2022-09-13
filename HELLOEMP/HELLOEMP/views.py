'''
Created on 2022. 9. 6.

@author: PC-04
'''
from django.shortcuts import render
from HELLOEMP.daoemp import DaoEmp 

de = DaoEmp()

def emp_list( request ):
     
    lst = de.mylist()
    
    data = {
        'list':lst
    }
    print(lst)
    
    return render( request, 'emp_list.html', data )

def emp_add( request ):
    return render( request, 'emp_add.html' )

def emp_add_act( request ):
    
 
    
    e_id = request.POST[ 'e_id' ]
    e_name = request.POST[ 'e_name' ]
    sex = request.POST[ 'sex' ]
    addr = request.POST[ 'addr' ]
    
    print( f'e_id : { e_id } , e_name : { e_name }, sex : { sex }, addr : { addr }' )
    
    cnt = de.myinsert( e_id, e_name, sex, addr )
    
    attr = {
        'cnt':cnt
    }
    
    return render( request, 'emp_add_act.html', attr )
    
    
def emp_detail( request ):
    
    e_id = request.GET.get( 'e_id', '__' )
    
    emp = de.myone( e_id )
    attr = {
        'emp':emp
    }

    return render( request, 'emp_detail.html', attr )

def emp_mod( request ):
    
    e_id = request.GET.get( 'e_id', '__' )
    
    emp = de.myone( e_id )
    attr = {
        'emp':emp
    }

    return render( request, 'emp_mod.html', attr )

def emp_mod_act( request ):
    
 
    
    e_id = request.POST[ 'e_id' ]
    e_name = request.POST[ 'e_name' ]
    sex = request.POST[ 'sex' ]
    addr = request.POST[ 'addr' ]
    
    print( f'e_id : { e_id } , e_name : { e_name }, sex : { sex }, addr : { addr }' )
    
    cnt = de.myupdate( e_id, e_name, sex, addr )
    
    attr = {
        'cnt':cnt
    }
    
    return render( request, 'emp_mod_act.html', attr )


def emp_del_act( request ):
    
    e_id = request.POST[ 'e_id' ]
    
    cnt = de.mydelete( e_id )
    attr = {
        'cnt': cnt
    }

    return render( request, 'emp_del_act.html', attr )



