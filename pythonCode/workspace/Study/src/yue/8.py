t=['name','age','gender']
t2=['milo',30,'male']
print zip(t,t2)

dic={0:0,1:1,2:2}
print dic[0]

dic1={'name':'milo','age':25,'gender':'male'}
print dic1
print dic1['name']

name='fang'
dic2={1:123,name:'milo','x':456}
print dic2[name]
print dic2

a='ss'
dic3={a:'aaa','b':'bbb'}
print dic3

for k in dic1:
	print dic1[k]


dic1['tel']='123456789'
print dic1

del(dic1['tel'])
print dic1

print dic1.pop('name')
print dic1

print dic.get(3)
print dic.get(3,'error')

dic1={'a':123,'b':456,4:444}
print dic1.keys()
print dic1.values()


