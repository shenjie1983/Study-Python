'''
@Descripttion:用while循环实现1~100之间的偶数求和 
@version: 0.1
@Author: 沈洁
@Date: 2019-12-14 13:39:57
@LastEditors  : 沈洁
@LastEditTime : 2019-12-24 23:25:22
'''
sum, num = 0, 2
while num <= 100:
    sum += num
    num += 2
print(sum)
