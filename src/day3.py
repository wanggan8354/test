'''
Created on 2018年2月11日

@author: gan
'''
# import math
# def move(x, y, step, angle):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny
# print(move(100, 100, 60, math.pi/6))
# from _collections_abc import Iterable

# def calc(*numbers):
#     sum1 = 0
#     for n in numbers:
#         sum1 = sum1 + n * n
#     return sum1
# nums = [1,2,3,4]
# print(calc(*nums))

# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)
# person('Michael', 30)
# person('Bob', 35, city='Beijing')
# extra = {'city': 'Beijing', 'job': 'Engineer'}
# person('Jack', 24, **extra)

# def f1(a, b, c=0, *args, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
# f1(1, 2)
# f1(1, 2, 3, 'a', 'b')
# f1(1, 2, 3, 'a', 'b', x=99)
# f1(1, 2, d=99, ext=None)
# 
# args = (1, 2, 3, 4)
# kw = {'d': 99, 'x': '#'}
# f1(*args, **kw)
# args = (1, 2, 3)
# kw = {'d': 88, 'x': '#'}
# f1(*args, **kw)

# def fact(n):
#     if n==1:
#         return 1
#     return n * fact(n - 1)
# print(fact(100))

# print(isinstance('abc', Iterable))
# print(isinstance([1,2,3], Iterable))
# print(isinstance(123, Iterable))

# for i, value in enumerate(['a', 'b', 'c']):
#     print(i, value)
    
# print([x * x for x in range(1, 11) if x % 2 == 0])
# print([m + n for m in 'ABC' for n in 'adc'])

# def fib(max1):
#     n, a, b = 0, 0, 1
#     while n < max1:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
# fib(5)

def fib1(max2):
    n, a, b = 0, 0, 1
    while n < max2:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
fib1(6)
    
