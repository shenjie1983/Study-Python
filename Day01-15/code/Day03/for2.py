'''
@Descripttion: 用for循环实现1~100之间的偶数求和
@version: 0.1
@Author: 沈洁
@Date: 2019-10-14 11:03:50
@LastEditors: 沈洁
@LastEditTime: 2019-10-14 11:05:08
'''
sum = 0
for x in range(2, 101, 2):
    sum += x
print(sum)
