'''
Created on 2018年4月3日

@author: gan
'''
import logging
def foo(s):
    n = int(s)
#     print('>>> n = %d' % n)
#     assert n != 0, 'n is zero'
    logging.info('n = %d' % n)
    return 10 / n

def main():
    foo('0')

main()