'''
Created on 2018年4月20日

@author: gan
'''
# import threading
# import time
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1 
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)
#     
# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='loopthread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)

# 线程锁
import threading

balance = 0
def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

lock = threading.Lock()
def run_thread(n):
    for i in range(100000):
        print(i)
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()
            
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
        