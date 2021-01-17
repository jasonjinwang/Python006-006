#!/usr/bin/python3 
import pymysql
from datetime import datetime
 
db = pymysql.connect(host="127.0.0.1",
                     user="root",
                     password="abc!123",
                     db="testdb")
try:

    # %s是占位符
    with db.cursor() as cursor:
        sql = 'INSERT INTO accountorm (account_name, account_age, account_sex, account_education) VALUES (%s, %s,  %s, %s)'
        values = (
            ("张三", 32, "男", "本科"),
            ("李四", 33, "男", "专科"),
            ("赵六", 34, "女", "专科")
        )
        cursor.executemany(sql, values)
    db.commit()

except Exception as e:
    print(f"insert error {e}")

finally:
    # 关闭数据库连接
    db.close()
    print(cursor.rowcount)
