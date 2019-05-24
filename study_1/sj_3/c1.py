# 类最基本的作用：封装
class Student():
    name = ''
    age = 0
# 在类中编写函数与模块中编写时不一样的，需要self
    def print_file(self):
        print('name:' + self.name)
        print('age:' + str(self.age))


student = Student()
student.print_file()
