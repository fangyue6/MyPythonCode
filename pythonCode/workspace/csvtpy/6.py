str1="ssss"


print "len()*****************************************\n"
a=len(str1)
print a

print "+ str1+str2*****************************************\n"
str2='aa'
print str1+str2

print "str2*5 -----------------"
print (str2+"-")*5

print "# "*40
iss='c' in str1
print iss

x='ss'
iss=x in str1
print iss

print "\n max()################################"
str2="abcdefghijklmnopqrstuvwxyz"
print max(str2)

print "\n cmp()#########################"
print cmp(str1,str2)

print "yuan zu  #############################################"
t=("milo",30,"male")
print t[0]
print t[1]
print t[2]


t1=()
t2=(2,)
type(t1)

print "name,age,gender=t   #####################"
name,age,gender=t
print name
print age
print gender

