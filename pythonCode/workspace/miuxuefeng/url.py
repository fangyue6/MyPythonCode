#!/usr/bin/env python
# -*- coding: utf-8 -*-
from web import get, view
from models import User, Blog, Comment

#@view('test_users.html')
#@get('/')
#def test_users():
#    users = User.find_all()
#    return dict(users=users)

@view('blogs.html')
@get('/')
def index():
    print '*#'*20
    print 'I am here'
    print '*#'*20
    blogs = Blog.find_all()
    # ≤È’“µ«¬Ω”√ªß:
    user = User.find_first('where email=?', 'test01@example.com')
    return dict(blogs=blogs, user=user)