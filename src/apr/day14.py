'''
Created on 2018年4月23日

@author: gan
'''
import re
# test = '010-12345'
# if re.match(r'\d{3}\-\d{3,8}$', test):
#     print('ok')
# else:
#     print('false')
#     
# print('a b  c'.split(' '))
# print(re.split(r'\s+', 'a b  c'))
# print(re.split(r'[\s\,]+', 'a,b, c  d'))
# print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))
# 
# m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
# print(m.group(0))
# print(m.group(1))
# print(m.group(2))

# 加个?就可以让\d+采用非贪婪匹配
n = re.match(r'^(\d+?)(0*)$', '102300').groups()
print(n)

# 预编译该正则表达式
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
g = re_telephone.match('010-12345678').groups()
print(g)
