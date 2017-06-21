#!/usr/bin/python

def fun():
	return 0

if 1>2:
	print "ok"
else:
	print 'bad'
	
if fun():
	print "ok1"
	
	
	
x=int(raw_input("please input :"))
if x>=90:
	print "A"
elif x>=80:
	print "B"
elif x>=70:
	print "C"
elif x>=60:
	print "D"
else:
	print "E"