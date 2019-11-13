import pymysql.cursors

db = pymysql.Connect(host='39.105.193.153',port=9336,user='root',passwd='123456',db='financial',charset='utf8')
#db = pymysql.Connect(host = 'localhost',port = 3306,user = 'root',passwd = '123456',db = 'test',charset='utf8')
cursor = db.cursor()
# cursor.execute("drop table if exists user")
# sql = """CREATE TABLE IF NOT EXISTS `user` (
#       `id` int(11) NOT NULL AUTO_INCREMENT,
#       `name` varchar(255) NOT NULL,
#       `age` int(11) NOT NULL,
#       PRIMARY KEY (`id`)
#     ) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=0"""
#
# cursor.execute(sql)
# sql="""INSERT INTO `user` (`name`, `age`) VALUES
# ('test1', 1),
# ('test2', 2),
# ('test3', 3),
# ('test4', 4),
# ('test5', 5),
# ('test6', 6);"""
# try:
#    # 执行sql语句
#    cursor.execute(sql)
#    # 提交到数据库执行
#    db.commit()
# except:
#    # 如果发生错误则回滚
#    db.rollback()
# id=1
# sql="update user set age=100 where id='%s'" % (id)
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()
# id=2
# sql="delete from user where id='%s'" % (id)
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()
# cursor.execute("select * from user")
#
# results = cursor.fetchall()
#
# for row in results:
#     name = row[0]
#     age = row[1]
#     # print(type(row[1])) #打印变量类型 <class 'str'>
#
#     print("name=%s,age=%s" % \
#           (age, name))

cursor.close()
db.close()
