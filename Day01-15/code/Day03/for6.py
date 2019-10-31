'''
@Descripttion: 打印各种三角形图案
@version: 0.1
@Author: 沈洁
@Date: 2019-10-14 15:34:55
@LastEditors: 沈洁
@LastEditTime: 2019-10-14 16:07:32
'''
row = int(input('请输入行数：'))
for x in range(row):
    for _ in range(x + 1):
        print('*', end='')
    print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for j in range(row - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        print('*', end='')
    print()
