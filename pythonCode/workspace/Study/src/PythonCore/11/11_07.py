#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2015年4月10日

@author: fangyue
'''

'11.7.2 内建函数apply()、filter()、map()、reduce()  p419'

from random import randint
def odd(n):
    return n % 2
allNums = []
for eachNum in range(9):
    allNums.append(randint(1, 99))
print filter(odd, allNums)



print map(lambda x, y: x + y, [1,3,5], [2,4,6])
print map(lambda x, y: (x+y, x-y), [1,3,5], [2,4,6])

print map(None, [1,3,5], [2,4,6])
print zip([1,3,5], [2,4,6])

print 'the total is:', reduce((lambda x,y: x+y), range(5))


#p426 11.7.3 偏函数应用
from operator import add, mul
from functools import partial
add1 = partial(add, 1) # add1(x) == add(1, x)
mul100 = partial(mul, 100) # mul100(x) == mul(100, x)
print add1(10)
print mul100(20)


#简单GUI类的例子
from functools import partial
import Tkinter
root = Tkinter.Tk()
MyButton = partial(Tkinter.Button, root,fg='white', bg='blue')
b1 = MyButton(text='Button 1')                   
b2 = MyButton(text='Button 2')                  
qb = MyButton(text='QUIT', bg='red', command=root.quit)                  
b1.pack()                   
b2.pack()
qb.pack(fill=Tkinter.X, expand=True)
root.title('PFAs!')
root.mainloop()                   

