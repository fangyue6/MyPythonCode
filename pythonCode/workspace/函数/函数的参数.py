def power(x):
    return x * x
#print '5*5=' , power(5)

def power(x, n=2):#default para
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
#print '5^3=' , power(5,3)

def calc(*numbers):#many parameter
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
#print calc(1,2,3)
#print calc()

def person(name, age, **kw):#key parameter
	return 'name:', name, 'age:', age, 'other:', kw
	
kw = {'city': 'Beijing', 'job': 'Engineer'}
print person('Jack', 24, city=kw['city'], job=kw['job'])
