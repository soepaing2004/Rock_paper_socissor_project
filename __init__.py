print(1,2,3,4,sep=' ')

x=5
y=10
print('the value of x {},the value of y {}'.format(x,y)) #str.format

#lambda function
#def add(a):
    #return a+a
add=lambda a: a+a
x=add(5)
print(x)

#filter function
#def a(y):
    #return y%2==0

x=[1,2,3,4,5,6,7,8,9]
#y=[]
#for i in x:
#    if i%2==0:
#        y.append(i)
#print(y)
print(list(filter(lambda i:i%2==0,x)))

#random function
import random as r
print(r.randint(0,40))

#special variable
from example import *    #if you want to use all function from a python file use *
something()