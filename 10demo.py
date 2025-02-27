# 10demo.py by shiv

print('hello again') # greetings

"""this is a 
multi line comment"""


# WHY SHOULD ADD LIBRARIES IN THE START OF PROGRAM

from math import ceil
print(ceil(4.4))


# SIMPLE MATHS

print('1.5e-2')
print(pow(2, 3))
print(abs(-3))
print(round(2.2233232332, 8))
print(3 % 2)


# IMORTING LIBRARIES

import math
print(math.ceil(3.2))
print(ceil(4.4))

print (math.log10(100000))
print(math.inf)
print(math.log(100000))
""" print(math.sqrt(-3)) leads to domain error"""


# NOT EXACT VALUE

print(1*0.1) 
print(1*0.3) 
print(0.1 + 0.2 == 0.3)


# VARIBLES

aa = 2
bb = 13
print(aa)
print(repr(aa)) 
print(type(aa))
c = 9
print(type(aa),type(bb), type(c))
print("hello", "world", "hi")
print("hello", "world", "hi", sep=',')
print("hello", "world", "hi")
print("hello", "world", "hi", end="haha")
print("hello\n", "world", "hi")


# FUCTIONS

def parameter_of_square(n):
	p = n*4
	return p
parameter_of_square(3) # doesnt save the result, need to use (3) again in print
print(parameter_of_square(3))


# PRACTICE

def temp_c(f):
	return (f-32)*(5/9)

print(temp_c(67))


def temp_f(cc):
	return (cc*(9/5)+32)

print(temp_f(25))



def is_even(x):
	if x / 2 == 1: return True
	return False

print(is_even(2))
print(is_even(3))

a=0.3
b=0.1*3
c = a == b

print(c)
print(type(c))



if a<b: print('a is smaller')
elif a>b : print('a is bigger')
else: print('a is equal')
"""if is keeping track of else even though 
they are not arranged in a block and part of a function"""

if a < b or a > b: print('all things being equal, a and b are not')
if a < b and a > b: print('you are living in a strange world')
if not False: print(True)

if a<b: print('a is s')
elif a>b: print('a is b')
else: print('a is b')

if a<b: print('a is s') # if is enough by itself if not in a function? 
if a>b: print('a is b')
if a==b: print('a is s')

print(abs(a - b)) # 5.551115123125783e-17
if abs(a - b) < 1e-9: print('close enough')

def silly(m, x, b):
	y = m * x + b

print(silly(2, 3, 4))




#PRACTICE2

def isinteger(v):
	if v % 1 == 0: print('Integer')
	else: print('Not an interger')

isinteger(3.4)
isinteger(3)