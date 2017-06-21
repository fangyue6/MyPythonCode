#!/sur/bin/python
import time
d={1:111,2:222,3:333,'4_':'444'}
for k,v in d.items():
	print k
	print v
else:
	print "ending"
	
	
for x in range(1,11):
	print x
	if x==5:
		exit()
	if x==3:
		pass# daimazhuang
	if x==6:
		break
	#time.sleep(1)
else:
	print "ending"




