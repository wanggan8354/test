'''
Created on 2018年4月10日

@author: gan
'''
# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
import os
print(os.name)
# 获取某个环境变量的值
print(os.environ.get('PATH'))
# 查看当前目录的绝对路径
print(os.path.abspath('.'))
# 新目录的完整路径表示出来
print(os.path.join('/Users/michael', 'testdir'))
# 路径拆分为两部分，后一部分总是最后级别的目录或文件名
print(os.path.split('/Users/michael/testdir/file.txt'))
# 得到文件扩展名
print(os.path.splitext('/Users/michael/testdir/file.txt'))
# 列出当前目录下的所有的.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
