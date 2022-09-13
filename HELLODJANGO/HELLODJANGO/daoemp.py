
import pymysql

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
        sql = 'SELECT * FROM EMP'
        self.cur.execute( sql )
        
        mlist = self.cur.fetchall()
        
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
        
        cnt = self.cur.execute( sql )
    
    
        self.con.commit()

        return cnt
        
    
    def myupdate(self , e_id, e_name, sex, addr):
        self = f"""
            UPDATE EMP
            SET
                E_NAME = { e_name },
                SEX = { sex },
                ADDR = { addr }
            WHERE
                E_ID = { e_id }
        """ 
    
    def __del__( self ):
        self.cur.close()
        self.con.close()
        
        
if __name__ == '__main__':
    de = DaoEmp()
    lst = de.mylist()
    print(lst)