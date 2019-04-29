from c9 import People
# 建议一个模块建立一个类
# 继承
class Student(People):
    sum1 = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__score = 0
        self.__class__.sum1 += 1

    def do_homework(self):
        print('homework')

