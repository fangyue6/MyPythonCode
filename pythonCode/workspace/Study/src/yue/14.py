#!/usr/bin/python
i=0
while True:
	i+=1
	print i
	x = raw_input("please input ,q for quit:")
	if cmp('q',x)==0:
		exit()
	if x:
		continue