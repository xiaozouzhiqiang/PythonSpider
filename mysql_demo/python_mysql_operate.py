import pymysql

def mysql_insert_info(cursor_2,uname,a,passwd):
    sql = """
    insert into usertable (id,username,age,password) values (null,%s,%s,%s)
    """
    cursor_2.execute(sql,(uname,a,passwd))
    conn.commit()

def mysql_select(cursor_3):
    sql = """
    select * from usertable
    """
    cursor_3.execute(sql)
    # while True:
    #     results = cursor_3.fetchone()
    #     if results:
    #         print(results)
    #     else:
    #         break
    results = cursor_3.fetchall()
    for result in results:
        print(result)
    # results = cursor_3.fetchmany(2)
    # print(results)

def mysql_delect(cursor_4):
    sql="""
    DELETE FROM `usertable` WHERE id=2
    """
    cursor_4.execute(sql)
    conn.commit()

def mysql_updata(cursor_5):
    sql = """
    UPDATE usertable set username='zouzhiqiang' WHERE id=3
    """
    cursor_5.execute(sql)
    conn.commit()

if __name__ == '__main__':
    conn = pymysql.connect(
        host="localhost",
        user='root',
        password='root',
        database='pythonmysql',
        port=3306
    )
    # username = 'heihei'
    # age = 25
    # password = 'zouzhiqiang'
    cursor = conn.cursor()
    # 向数据库中插入一条数据
    # mysql_insert_info(cursor,username,age,password)
    # 查找数据库中的数据
    # mysql_select(cursor)
    # 删除数据库中的数据
    # mysql_delect(cursor)
    # 更新数据库中的数据
    mysql_updata(cursor)
    conn.close() #关闭链接