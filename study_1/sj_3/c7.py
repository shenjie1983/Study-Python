# 成员可见性
# 使用私有函数来阻止访问

class Student():
    sum1 = 0
    # 学生考试的分数，不希望在外部能够修改
    # 不提倡在对象的外部对成员直接赋值，通过方法进行判断控制赋值，保护数据
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__score = 0
        self.__class__.sum1 += 1

    def making(self, score):
        if score < 0:
            # score = 0
            return '不能够给别人打负分'
        self.__score = score
        print(self.name + '本次考试分数为' + str(self.__score))

    def do_homework(self):
        self.do_english_homework()
        print('homework')

    def do_english_homework(self):
        print()


student1 = Student('浩南1', 31)
student2 = Student('浩南2', 32)

result = student1.making(59)
# 强行赋值，不会更改私有的__score
student1.__score = -1

print(student1.__dict__)
# {'name': '浩南1', 'age': 31, '_Student__score': 59, '__score': -1}
# print(student1.__score)

# print(student2.__score)报错
# print(student2._Student__scroe)
print(student2.__dict__)
# {'name': '浩南2', 'age': 32, '_Student__score': 0}

# print(result)
# 外部能够修改直接修改分数，危险


