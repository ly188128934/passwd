#将生成的密码保存到数据库
import MySQLdb

db = MySQLdb.connect(host,UserWarning,password,dbname,charset='utf8')

cursor = db.cursor()

# 执行sql
cursor.execute("sql")

#获取数据
data = cursor.fetchone()


db.close()