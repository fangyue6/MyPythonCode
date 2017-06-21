#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2015年4月21日

@author: fangyue
'''

"""
create database test;
create table user(
id int primary key auto_increment,
username varchar(20),
password varchar(20)
);
"""
#MySQL-python
def insertIntoUser(id,username,password):
    import MySQLdb
    conn=MySQLdb.connect(user='root',passwd='123456',host='192.168.1.252')
    cur=conn.cursor()
    conn.select_db('test')
    sql='insert into user(id,username,password) value(%s,%s,%s)'
    result=cur.execute(sql,(id,username,password))
    conn.commit()
    cur.close()
    conn.close()
    return result


#sqls='insert into userinfo(name,year,gender) values(%s,%s,%s)'
#print cur.executemany(sqls,[('fangyue1','23','M'),('fangyue2','24','F')])#插入多条数据
#conn.commit()
#
#dele_sql='delete from userinfo where id=1'
#print cur.execute(dele_sql)
#conn.commit()
#
#update_sql="update userinfo set name=%s where id=%s"
#print cur.execute(update_sql,('boy',int(2)))
#conn.commit()
#
#cur.execute("select * from user") #查询到数量
#print cur.fetchmany(cur.execute("select * from user"))
def check(username,password):#0用户名不存在，-1密码错误，1验证成功 
    import MySQLdb
    returns=-2
    try:
        conn=MySQLdb.connect(user='root',passwd='123456',host='192.168.1.252')
        cur=conn.cursor()
        conn.select_db('test')
        
        sql="select * from user where username='%s'"%username
        sql1="select * from user where username='%s' AND password='%s'"%(username,password)
        result= cur.fetchmany(cur.execute(sql))
        lens= len(result)
        try:
            if lens==0:
                returns=0#用户名不存在
            else :
                 result= cur.fetchmany(cur.execute(sql1))
                 lens=len(result)
                 if lens==0:
                     returns= -1#密码错误
                 else :
                     returns= 1#验证成功
        except Exception,msg:
            print msg
        finally: 
            cur.close()
            conn.close()
    except Exception,msg:
        print msg
        returns=-2
    return returns
        
#print check('fangyue','123456')
#cur.close()
#conn.close()
#print insertIntoUser(2,'admin','admin')
#print check('admin','admin')


