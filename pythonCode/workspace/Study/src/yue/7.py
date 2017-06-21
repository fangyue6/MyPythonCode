listinfo=[]
print type(listinfo)

listinfo=['milo',30,'male']
t=("milo",30,'male')
print t[0]
print listinfo[0]
print t[0:2]
print listinfo[0:2]

t3=('abc')
l3=['abc']
print type(t3)
print type(l3)

print "*"*40
listinfo[1]=45
print listinfo
print id(listinfo)
listinfo[1]=48
print listinfo
print id(listinfo)

print "append()*******************"
listinfo.append("aaaaa")
print listinfo

print "remove()*******************"
listinfo.remove(48)
print listinfo

print "help()*******************"
help(list.append)
help(list.remove)
help(len)

print "del()*********************"
del(listinfo[1])
print listinfo


