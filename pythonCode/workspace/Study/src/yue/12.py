#!/sur/bin/python

for x in "hello":
	print x

print "***************************************" 
s="hello"
for x in range(len(s)):
	print s[x]

print "***************************************" 
l=[1,2,3,'a','b']
t=(7,8,9,'x','y')
for x in l:
	if x >=2:
		print x

		
print "***************************************"
d={1:111,2:222,3:333,'4_':'444'}
for x in d:
	print d[x]

print d.items()

for k,v in d.items():
	print k
	print v















