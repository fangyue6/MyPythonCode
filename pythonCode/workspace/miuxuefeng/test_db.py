from models import User, Blog, Comment

import db

db.create_engine(user='root', password='123456', database='awesome')

u = User(name='Test01', email='test01@example.com', password='1234567890', image='about:blank')

u.insert()

print 'new user id:', u.id

u1 = User.find_first('where email=?', 'test01@example.com')
print 'find user\'s name:', u1.name

#u1.delete()

u2 = User.find_first('where email=?', 'test01@example.com')
print 'find user:', u2