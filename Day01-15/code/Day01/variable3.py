'''
@Descripttion:格式化输出 
@version: 0.1
@Author: 沈洁
@Date: 2019-09-17 16:21:59
@LastEditors: 沈洁
@LastEditTime: 2019-10-12 10:41:47
'''
a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))
