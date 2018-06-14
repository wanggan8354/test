'''
Created on 2018年2月12日

@author: gan
'''
# def f(x):
#     return x * x
# L = []
# for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
#     L.append(f(n))
# print(L)
import functools

# 全体素数
# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n
# def _not_divisible(n):
#     return lambda x: x % n > 0
# def primes():
#     yield 2
#     it = _odd_iter() # 初始序列
#     while True:
#         n = next(it) # 返回序列的第一个数
#         yield n
#         it = filter(_not_divisible(n), it) # 构造新序列
# # 打印1000以内的素数:
# for n in primes():
#     if n < 100:
#         print(n)
#     else:
#         break

# list1 = [36, 5, -12, 9, -21]
# print(sorted(list1, key=abs))

# f = lambda x : x * x
# print(f(4))
# 
# def build(x, y):
#     return lambda: x*x + y*y
# print(build(3, 4)())
# print(build.__name__)

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s:' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log('execute')
def gg():
    print('wang')
gg()