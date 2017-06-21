#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2015年4月9日

@author: fangyue
'''

"""
create database week;
create table userinfo(
id int primary key auto_increment,
name varchar(20),
year int,
gender varchar(5)
);
"""
#MySQL-python
import MySQLdb
conn=MySQLdb.connect(user='root',passwd='123456',host='120.27.43.71')
cur=conn.cursor()
conn.select_db('week')


sql='insert into userinfo(name,year,gender) value(%s,%s,%s)'
print cur.execute(sql,('fangyue','22','M'))
conn.commit()


sqls='insert into userinfo(name,year,gender) values(%s,%s,%s)'
print cur.executemany(sqls,[('fangyue1','23','M'),('fangyue2','24','F')])#插入多条数据
conn.commit()

dele_sql='delete from userinfo where id=1'
print cur.execute(dele_sql)
conn.commit()

update_sql="update userinfo set name=%s where id=%s"
print cur.execute(update_sql,('boy',int(2)))
conn.commit()

cur.execute("select * from userinfo") #查询到数量
print cur.fetchmany(cur.execute("select * from userinfo"))


cur.close()
conn.close()

