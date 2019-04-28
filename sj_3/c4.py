class Student():
    # 类变量
    # 一个班级里所有学生的总数
    sum1 = 0
    # 实例方法内部访问类变量
    def __init__(self, name, age):
        # 初始化对象的属性
        # self.name定义实例变量
        self.name = name
        self.age = age
        self.__class__.sum1 += 1
        print('当前班级学生总数为:' + str(self.__class__.sum1))

    # 特征、行为
    # 实例方法
    # self的意义在于：python默认传递进来的，可以代表当前对象的一个参数
    def do_homework(self):
        print('homework')

    # 定义类方法
    # 使用装饰器修饰
    # 要操作一个和对象无关的变量，最正确的方式还是使用类方法
    # 主要用来操作和类相关的变量，上面的sum1非常适合放在类方法中运行
    # cls可以更改为其他名字，和构造函数的self一样
    #
    # cls的意义在于：python默认传递进来的，可以代表调用类方法的这个类
    # Student.plus_sum(),cls就代表Student这个类
    @classmethod
    def plus_sum(cls):
        cls.sum1 += 1
        print(cls.sum1)

    # 静态方法
    @staticmethod
    def add(x, y):
        # 访问类变量
        print(Student.sum1)
        print('This is a static method') 

student1 = Student('浩南1', 31)
# 对象调用类方法,不建议使用
student1.plus_sum()

# 类调用类方法
# Student.plus_sum()


# 对象调用类方法
student1.add(1,2)
# 类调用静态方法
Student.add(1,2)

# student2 = Student('浩南2', 32)
# Student.plus_sum()
# student3 = Student('浩南3', 33)
# Student.plus_sum()

# print(Student.sum1)
