class Student():
    name = 'xiaoming'
    age = 0
    def __init__(self, name, age):
        # self.name = name
        # self.age = age
        name = name
        age = age

    def do_homework(self):
        print('homework')



student1 = Student('浩南', 34)

print(student1.__dict__)
print(Student.__dict__)

# print(student1.name)
# print(Student.name)
