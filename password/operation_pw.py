#/usr/bin/env python
#encoding:utf-8

#将生成的密码保存到数据库
import MySQLdb
import sys

#数据库配置
host='127.0.0.1'
username='root'
password='!QAZxsw2'
dbname='pwdmng'

#初始化连接
db = MySQLdb.connect(host,username,password,dbname,charset='utf8')
cursor = db.cursor()

def get_old_record(id):
    get_sql="select id,username,password,remark from %s.account_info where id='%s' " % (dbname,id)
    cursor.execute(get_sql)
    return cursor.fetchone()

def insert_new_record(username,password,expiry='365',pw_type='0',uses='null',address='null',remark='null'):
    insert_new_sql="insert into %s.account_info(username,password,expiry,pw_type,uses,address,remark) values('%s','%s','%s','%s','%s','%s','%s');" % (dbname,username,password,expiry,pw_type,uses,address,remark)
    try:
        cursor.execute(insert_new_sql)
        db.commit()
    except:
        db.rollback()

def insert_old_record(id,username,password,pw_type,remark='null'):
    insert_old_sql="insert into %s.pwd_history(id,username,password,pw_type,remark) values('%s','%s','%s','%s','%s');" % (dbname,id,username,password,pw_type,remark)
    try:
        cursor.execute(insert_old_sql)
        db.commit()
    except:
        db.rollback()

def back_old_record(id):
    data=get_old_record(id)
    insert_old_record(id=int(data[0]),username=data[1],password=data[2],pw_type=data[3],remark=data[4])

def update_record(id,field,value):
    change_sql="update %s.account_info set %s='%s' where id=%s" % (dbname,field,value,id)
    try:
        cursor.execute(change_sql)
        db.commit()
    except:
        db.rollback()

def change_record(id,field,value):
    back_old_record(id)
    update_record(id,field,value)

def delete_record(id):
    delete_sql="delete from %s.account_info where id='%s'" % (dbname,id)
    try:
        back_old_record(id)
        cursor.execute(delete_sql)
        db.commit()
    except:
        db.rollback()

if sys.argv[1] == 'insert':
    insert_new_record(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7],sys.argv[8])
elif sys.argv[1] == 'delete':
    delete_record(sys.argv[2])
elif sys.argv[1] == 'update':
    change_record(sys.argv[2],sys.argv[3],sys.argv[4])
else:
    print("only support insert or delete or update operation")

db.close()
