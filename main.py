import sys
import random

print(sys.version)

if 5 > 2 or 4 > 1:
    print('OK')

x = str('3')
print(x)
print(type(x))

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
x = 5
y = 10
print(x + y)
x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()

print("Python is " + x)

print()
