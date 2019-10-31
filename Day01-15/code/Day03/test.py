'''
@Descripttion: 
@version: 0.1
@Author: 沈洁
@Date: 2019-10-14 12:33:24
@LastEditors: 沈洁
@LastEditTime: 2019-10-14 16:06:50
'''

row = int(input('请输入行数: '))
for i in range(row):
    for j in range(row - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        print('*', end='')
    print()
