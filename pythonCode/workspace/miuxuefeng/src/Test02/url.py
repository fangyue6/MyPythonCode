#!/usr/bin/env python
# -*- coding: utf-8 -*-
from web import get, post,view,ctx,interceptor
from models import User, Blog, Comment
from Error import APIError,APIValueError
from apis import api
import hashlib  
import re
import time
#@view('test_users.html')
#@get('/')
#def test_users():
#    users = User.find_all()
#    return dict(users=users)

@view('blogs.html')
@get('/')
def index():
    print '*#'*20
    print 'blogs ,I am here'
    print '*#'*20
    blogs = Blog.find_all()
    # ���ҵ�½�û�:
    user = User.find_first('where email=?', 'test01@example.com')
    return dict(blogs=blogs, user=user)

@view('register.html')
@get('/register')
def register():
    print '*#'*20
    print 'register,I am here'
    print '*#'*20
    blogs = Blog.find_all()
    print "blogs = Blog.find_all()****************"
    # ���ҵ�½�û�:
    user = User.find_first('where email=?', 'test01@example.com')
    print '''user = User.find_first('where email=?', 'test01@example.com')****************'''
    return dict(blogs=blogs, user=user)
    print 'return dict(blogs=blogs, user=user)****************' 
 
@api
@get('/api/users')
def api_get_users():
    print '*#'*20
    print 'api_get_users,I am here'
    print '*#'*20
    users = User.find_by('order by created_at desc')
    # 把用户的口令隐藏掉:
    for u in users:
        u.password = '******'
    return dict(users=users)

_RE_EMAIL=re.compile(r'^[a-z]([a-z0-9]*[-_]?[a-z0-9]+)*@([a-z0-9]*[-_]?[a-z0-9]+)+[\.][a-z]{2,3}([\.][a-z]{2})?$/i')
_RE_MD5 = re.compile(r'^[0-9a-f]{32}$')

@api
@post('/api/users')
def register_user():
    i = ctx.request.input(name='', email='', password='')
    name = i.name.strip()
    email = i.email.strip().lower()
    password = i.password
    if not name:
        raise APIValueError('name')
    if not email or not _RE_EMAIL.match(email):
        raise APIValueError('email')
    if not password or not _RE_MD5.match(password):
        raise APIValueError('password')
    user = User.find_first('where email=?', email)
    if user:
        raise APIError('register:failed', 'email', 'Email is already in use.')
    user = User(name=name, email=email, password=password, image='http://www.gravatar.com/avatar/%s?d=mm&s=120' % hashlib.md5(email).hexdigest())
    user.insert()
    return user

@api
@post('/api/authenticate')
def authenticate():
    print '*#'*20
    print 'authenticate,I am here'
    print '*#'*20
    i = ctx.request.input()
    email = i.email.strip().lower()
    password = i.password
    user = User.find_first('where email=?', email)
    if user is None:
        raise APIError('auth:failed', 'email', 'Invalid email.')
    elif user.password != password:
        raise APIError('auth:failed', 'password', 'Invalid password.')
    max_age = 604800
    cookie = make_signed_cookie(user.id, user.password, max_age)
    ctx.response.set_cookie(_COOKIE_NAME, cookie, max_age=max_age)
    user.password = '******'
    return user

# 计算加密cookie:
def make_signed_cookie(id, password, max_age):
    expires = str(int(time.time() + max_age))
    L = [id, expires, hashlib.md5('%s-%s-%s-%s' % (id, password, expires, _COOKIE_KEY)).hexdigest()]
    return '-'.join(L)

@interceptor('/')
def user_interceptor(next):
    user = None
    cookie = ctx.request.cookies.get(_COOKIE_NAME)
    if cookie:
        user = parse_signed_cookie(cookie)
    ctx.request.user = user
    return next()

# 解密cookie:
def parse_signed_cookie(cookie_str):
    try:
        L = cookie_str.split('-')
        if len(L) != 3:
            return None
        id, expires, md5 = L
        if int(expires) < time.time():
            return None
        user = User.get(id)
        if user is None:
            return None
        if md5 != hashlib.md5('%s-%s-%s-%s' % (id, user.password, expires, _COOKIE_KEY)).hexdigest():
            return None
        return user
    except:
        return None
