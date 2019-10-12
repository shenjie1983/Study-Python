'''
@Descripttion:运算符的使用 
@version: 0.1
@Author: 沈洁
@Date: 2019-06-12 11:20:07
@LastEditors: 沈洁
@LastEditTime: 2019-10-12 10:40:38
'''
# a = int(input('a='))
# b = int(input('b='))
# print('%d+%d=%d' % (a, b, a + b))
# print('% d/ %d = %.2f') % (a, b, a / b)

# c = 10.0
# d = 3
# print(c/d)
# print(type(c))


a1 = 100
a2 = 12.345
a3 = 1 + 5j
a4 = 'shuaibaoe'
a5 = True
print(type(a1), type(a2), type(a3), type(a4), type(a5))

flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag1
print("flag1 = ", flag1)
print("flag2 = ", flag2)
print("flag3 = ", flag3)
print("flag4 = ", flag4)
print("flag5 = ", flag5)
