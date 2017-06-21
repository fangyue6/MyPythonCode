#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from flask import Flask, request, render_template,session
import User
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('phone/index.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/retur/<name>')
def retur(name):
    path='phone/%s'%name
    print path
    return render_template(path)
    
@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    #session['name']=username
    msg="1"
    result=User.check(username, password)
    if result==1:
        return render_template('signin-ok.html', username=username)
    msg=" PassWord Error" if result==-1 else "User name does not exist"  
    return render_template('index.html', message=msg, username=username)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
