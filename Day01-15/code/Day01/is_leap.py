'''
@Descripttion:输入年份 如果是闰年输出True 否则输出False
leap:闰年 
@version: 0.1
@Author: 沈洁
@Date: 2019-06-12 11:20:07
@LastEditors: 沈洁
@LastEditTime: 2019-10-12 10:39:48
'''


year = int(input('输入年份:'))
is_leap = (year % 4 == 0 and year % 100 != 0 or
           year % 400 == 0)
print(is_leap)
