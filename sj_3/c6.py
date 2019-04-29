# 成员可见性
# 使用实例方法来操作敏感数据

class Student():
    sum1 = 0
    # 学生考试的分数，不希望在外部能够修改
    # 不提倡在对象的外部对成员直接赋值，通过方法进行判断控制赋值，保护数据
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.score = 0
        self.__class__.sum1 += 1

    def making(self, score):
        if score < 0:
            # score = 0
            return '不能够给别人打负分'
        self.score = score
        print(self.name + '本次考试分数为' + str(self.score))

    def do_homework(self):
        self.do_english_homework()
        print('homework')

    def do_english_homework(self):
        print()


    @classmethod
    def plus_sum(cls):
        cls.sum1 += 1
        print(cls.sum1)

    @staticmethod
    def add(x, y):
        print(Student.sum1)
        print('This is a static method') 

student1 = Student('浩南1', 31)
result = student1.making(-1)
print(result)
# 外部能够修改直接修改分数，危险
# student1.score = -1 

