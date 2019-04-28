# 类最基本的作用：封装
# 类变量、实例变量
class Student():
    # 类变量
    name = '沈洁'
    age = 0
    
    # 构造函数
    # 目的是生成不同的对象
    def __init__(self, name, age):
        # 初始化对象的属性
        # self.name定义实例变量
        self.name = name
        self.age = age
        # print('student')


    def do_homework(self):
        print('homework')



student1 = Student('帅帅', 4)
student2 = Student('孙芳', 36)

print(student1.name, student1.age)
print(student2.name, student2.age)
