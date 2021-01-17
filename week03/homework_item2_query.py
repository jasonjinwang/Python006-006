#!/usr/bin/python3 
import pymysql
 
db = pymysql.connect(host="127.0.0.1",
                     user="root",
                     password="abc!123",
                     db="testdb")
 
try:

    # %s是占位符
    with db.cursor() as cursor:
        sql = '''SELECT account_id, account_name, account_age, account_birth, account_sex, account_education FROM accountorm'''
        cursor.execute(sql)
        accounts = cursor.fetchall() # fetchone()， 取出匹配的
        for acct in accounts: 
            print(acct)
    db.commit()

except Exception as e:
    print(f"insert error {e}")

finally: 
    # 关闭数据库连接
    db.close()
    print(cursor.rowcount)

