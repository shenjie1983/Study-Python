from c9 import Human

# 建议一个模块建立一个类
# 继承
class Student(Human):
    def __init__(self, school, name, age):
        self.school = school
        Human.__init__(self, name, age)
        # 类调用方法必须要self,实在要调用，传入实力本身
        # Student.do_homework(student1)
        # 实列对象则不需要，调用的方法省略self，
        #

    def do_homework(self):
        print('homework')

student1 = Student('人民路小学', "小明", 18)
# print(student1.sum)
# print(Student.sum)
print(student1.name)
print(student1.age)
# student1.get_name()