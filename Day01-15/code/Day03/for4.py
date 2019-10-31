'''
@Descripttion: 输入一个正整数判断它是不是素数
素数又叫质数(prime number),有无限个。质数定义为在大于1的自然数中,除了1和它本身以外不能被任何整数整除的数
为什么判断一个数是否为素数时只需开平方根就行了：因为如果它不是质数，那么它一定可以表示成两个数（除了1和它本身）相乘，这两个数必然有一个小于等于它的平方根。只要找到小于或等于的那个就行了
@version: 0.1
@Author: 沈洁
@Date: 2019-10-14 11:10:24
@LastEditors: 沈洁
@LastEditTime: 2019-10-14 11:57:04
'''
from math import sqrt

num = int(input('请输入一个大于1的正整数： '))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d是合数' % num)
