'''
@Descripttion: 
@version: 0.1
@Author: 沈洁
@Date: 2019-12-26 22:25:05
@LastEditors  : 沈洁
@LastEditTime : 2019-12-26 22:26:30
'''

num = int(input('num='))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num*10+num % 10
    num //= 10
print(reversed_num)
