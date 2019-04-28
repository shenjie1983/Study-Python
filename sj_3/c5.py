class Student():
    sum1 = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__class__.sum1 += 1
        print('当前班级学生总数为:' + str(self.__class__.sum1))

    def do_homework(self):
        print('homework')

    @classmethod
    def plus_sum(cls):
        cls.sum1 += 1
        print(cls.sum1)

    # 静态方法
    # 不推荐使用静态方法
    @staticmethod
    def add(x, y):
        # 访问类变量
        print(Student.sum1)
        print('This is a static method') 

student1 = Student('浩南1', 31)

# 对象调用类方法
student1.add(1,2)
# 类调用静态方法
Student.add(1,2)


