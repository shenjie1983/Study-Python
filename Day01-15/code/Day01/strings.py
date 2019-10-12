'''
@Descripttion:字符串的常用操作 
@version: 0.1
@Author: 沈洁
@Date: 2019-09-19 09:38:50
@LastEditors: 沈洁
@LastEditTime: 2019-10-12 10:41:02
'''

str1 = 'hello, world!'
print('字符串的长度是：', len(str1))
print('单词首字母大写：', str1.title())
str1 = str1.upper()
print(str1)
print('字符串是不是大写：', str1.isupper())
print('字符串是不是以hello开头', str1.startswith('hello'))
