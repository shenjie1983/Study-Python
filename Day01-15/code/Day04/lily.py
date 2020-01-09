'''
@Descripttion: 找出100~999之间的所有水仙花数
@version: 0.1
@Author: 沈洁
@Date: 2019-12-26 22:14:20
@LastEditors  : 沈洁
@LastEditTime : 2019-12-26 22:21:47
'''
for num in range(100, 999):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)
