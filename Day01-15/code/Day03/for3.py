'''
@Descripttion:输入非负整数n计算n的阶乘n！ 
@version: 0.1
@Author: 沈洁
@Date: 2019-10-14 11:05:20
@LastEditors: 沈洁
@LastEditTime: 2019-10-14 11:11:08
'''
n = int(input('n = '))
result = 1
for x in range(1, n + 1):
    result *= x
print('%d! = %d' % (n, result))
