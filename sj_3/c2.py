# 类最基本的作用：封装
# 类变量、实例变量
class Student():
    # 类变量
    # 一个班级里所有学生的总数
    sum = 0
    # Student是一个类，是抽象，不是具体的；
    # 一个抽象的Student有name、age并不合适
    # name = '山鸡'
    # age = 0
    # 构造函数,特殊的实例方法
    # 目的是生成不同的对象
    # self的意义在于：python默认传递进来的，可以代表当前对象的一个参数
    def __init__(self, name, age):
        # 初始化对象的属性
        # self.name定义实例变量
        self.name = name
        self.age = age
        print(self.name)
        # 下面这个读取的是形参name
        # 可以将上面两行代码修改如下进行实验，报错
        # __init__(self, name, age):
        # self.name = name1
        print(name)
        # print('student')

    # 特征、行为
    # 实例方法
    def do_homework(self):
        print('homework')

# 实例方法和构造函数
# 1.调用的方式不一样
# 2.意义不一样
# 调用构造函数：对象=类()；意义在于：初始化类的特征
# 调用实例方法：对象.方法()；意义在于：描述类的特征、行为

# 调用构造函数：对象=类()
student1 = Student('浩南', 34)

# 调用实例方法：对象.方法()
student1.do_homework()

# print(student1.name, student1.age)
# print(student2.name, student2.age)
# print(Student.name)
