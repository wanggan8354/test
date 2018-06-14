'''
Created on 2018年4月11日

@author: gan
'''
import pickle
import json
from email.policy import default
# d = dict(name='Bob', age=20, score=100)
# # pickle模块来实现序列化
# print(pickle.dumps(d))

# f = open("E:/Program Files/wang.txt", 'ab')
# pickle.dump(d, f)
# f.close()

# f = open('E:/Program Files/wang.txt', 'rb')
# e = pickle.load(f)
# f.close()
# print(e)

# d = dict(name='Bob', age=20, score=8)
# print(json.dumps(d));

# json_str = '{"age":20, "score":88, "name":"wang"}'
# g = json.loads(json_str)
# print(g)

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
s = Student("gan", 24, 99)
# def student2dict(std):
#     return {
#         'name' : std.name,
#         'age' : std.age,
#         'score' : std.score
#     }
# print(json.dumps(s, default=student2dict))
print(json.dumps(s, default=lambda obj: obj.__dict__))