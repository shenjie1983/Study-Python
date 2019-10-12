'''
@Descripttion: 
@version: 0.1
@Author: 沈洁
@Date: 2019-09-23 12:34:57
@LastEditors: 沈洁
@LastEditTime: 2019-09-26 13:21:45
'''
import random
i = 1
a = random.randint(0, 100)
b = int(input("请输入0-100中的一个数字\n然后查看是否与电脑一样："))
while a != b:
    if a > b:
        print('您第%d次输入的数字小于电脑随机数字' % i)
        b = int(input('请您再次输入数字：'))
    else:
        print('您第%d次输入的数字大于电脑随机数字' % i)
        b = int(input('请再次输入数字：'))
    i += 1
else:
    print('恭喜帅帅，您第%d次输入的数字与电脑的随机数字%d一样' % (i, b))
