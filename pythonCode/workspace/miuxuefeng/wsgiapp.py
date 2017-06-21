#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import logging; logging.basicConfig(level=logging.INFO)
import os

import db
from web import WSGIApplication, Jinja2TemplateEngine

from config import configs

print '#'*25
print configs
print '#'*25
print configs['db']
print '#'*25
# ��ʼ�����ݿ�:
db.create_engine(**configs['db'])


# ����datetime_filter��������t�������unicode�ַ���:
def datetime_filter(t):
    delta = int(time.time() - t)
    if delta < 60:
        return u'1 minutes ago'
    if delta < 3600:
        return u'%s minutes ago' % (delta // 60)
    if delta < 86400:
        return u'%s hours ago' % (delta // 3600)
    if delta < 604800:
        return u'%s days ago' % (delta // 86400)
    dt = datetime.fromtimestamp(t)
    return u'%syear%smonth%sdays' % (dt.year, dt.month, dt.day)

template_engine = Jinja2TemplateEngine(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))
# ��filter��ӵ�jinjia2��filter����Ϊdatetime��filter������һ����������:
template_engine.add_filter('datetime', datetime_filter)

#wsgi.template_engine = template_engine

# ����һ��WSGIApplication:
wsgi = WSGIApplication(os.path.dirname(os.path.abspath(__file__)))
# ��ʼ��jinja2ģ������:
#template_engine = Jinja2TemplateEngine(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))
wsgi.template_engine = template_engine

# ���ش���@get/@post��URL������:
import url
wsgi.add_module(url)

# ��9000�˿����������ز��Է�����:
if __name__ == '__main__':
    wsgi.run('0.0.0.0',9000)