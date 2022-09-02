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

e_id = '10'
e_name = '10'
sex = '5'
addr = '5'
sql = f'DELETE FROM EMP WHERE E_ID = { e_id }'

cnt = cur.execute( sql )

print( f'cnt : { cnt }' )

# 파이썬에선 commit()을 따로 안해주면 DB에 적용이 안된다. 그래서
# 커밋을 꼭 해줘야한다.
con.commit()

cur.close()
con.close()