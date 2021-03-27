import pymysql
def main():
    # 创建连接对象
    conn= pymysql.connect(host='localhost', port=3306, user='root', password='mysql', database='pyMysql', charset='utf8')
    # 创建游标
    cs1=conn.cursor()
    #  执行SQL语句
    count=cs1.execute('SELECT * FROM  Student ')
    print("查询 %d 条1 " % count)
    for i in range(count):
        #获取查询结果
        result=cs1.fetchone()
        #打印查询结果
        print("更新前结果")
        print(result)
    sql = "UPDATE Student SET AGE = 1111111111 "
    try:
        # 执行SQL语句
        cs1.execute(sql)
        # 提交到数据库执行
        conn.commit()
    except:
        # 发生错误时回滚
        conn.rollback()

    count = cs1.execute('SELECT * FROM  Student ')
    print("查询 %d 条 " % count)
    for i in range(count):
        # 获取查询结果
        result = cs1.fetchone()
        # 打印查询结果
        print("更新后结果")
        print(result)
    # 关闭对象
    cs1.close()
    conn.close()

if __name__=='__main__':
    main()




