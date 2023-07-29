import pymysql

conn = pymysql.connect(
    host = "127.0.0.1",
    user = 'root',
    password = 'root',
    database = 'pythonmysql',
    port = 3306
)
# 做一个数据库链接的简单demo
cursor = conn.cursor()
cursor.execute("select 1")
data = cursor.fetchone()
print(data)
conn.close()