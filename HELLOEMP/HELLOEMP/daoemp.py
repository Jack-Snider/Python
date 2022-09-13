
import pymysql
from pkg_resources._vendor.jaraco.functools import except_

class DaoEmp:
    
    def __init__( self ):
        
        self.con = pymysql.connect(
            host="localhost",
            user="root",
            password="python",
            db = 'python',
            charset="utf8",
            port = 3305 )
        
        self.cur = self.con.cursor( pymysql.cursors.DictCursor )
        
    def mylist( self ):
        sql = 'SELECT e_id,e_name,sex,addr FROM EMP'
        self.cur.execute( sql )
        
        mlist = self.cur.fetchall()
        print("mlist",mlist)
        
        return mlist
        
    def myname( self, e_id ):
        sql = f"SELECT e_id, e_name, sex,addr FROM EMP WHERE E_ID = { e_id }"
    
        self.cur.execute( sql )
        mylist = self.cur.fetchall()
        
        return mylist[0]
        
    def myinsert( self, e_id, e_name, sex, addr ):
        
        sql=f"""
        insert into emp (e_id,e_name,sex,addr)
        values ('{e_id}', '{e_name}', '{sex}', '{addr}')
        """
        
        cnt = 0
        try:
            cnt = self.cur.execute( sql )
            self.con.commit()
            print( '< 저장이 성공적으로 완료되었습니다. >' )
        except :
            cnt= 0
            print( '< 저장에 실패하셨습니다. >' )

        return cnt
        
    def myone(self , e_id ):
        
        sql=f"""
           SELECT e_id,e_name,sex,addr
           FROM emp
           where
               e_id =  '{e_id}'
        """
        
        self.cur.execute(sql)
        
        mylist = self.cur.fetchall()
        return mylist[0]
    
    def myupdate( self , e_id, e_name, sex, addr ):
        
        sql = f"""
            UPDATE EMP
            SET
                E_NAME = { e_name },
                SEX = { sex },
                ADDR = { addr }
            WHERE
                E_ID = { e_id }
        """ 
        
        cnt = self.cur.execute( sql )
        
        
        self.con.commit()
    
        return cnt
    
    def mydelete( self,e_id ):
        
        sql = f"""delete from emp where e_id='{e_id}' """
      
        cnt = self.cur.execute(sql)
        
        self.con.commit()
    
        return cnt
    
    
    
    def __del__( self ):
        
        self.cur.close()
        self.con.close()
        
        
if __name__ == '__main__':
    de = DaoEmp()
    lst = de.mylist()
    print(lst)