import pymysql

con = pymysql.connect(
            host="localhost",
            user="root",
            password="python",
            db = 'python',
            charset="utf8",
            port = 3305 )

# 파이썬에서 커서는 자바에서의 Statement 역할을 한다.
cur = con.cursor()

sql = 'INSERT INTO emp( E_ID, E_NAME, SEX, ADDR ) VALUES ( 9, %s, %s, %s )'

# with는 open했다가 자동으로 close해줌
with con:
    with con.cursor() as cur:
        cur.execute( sql, ( '9','9','9' ) )
        con.commit()

