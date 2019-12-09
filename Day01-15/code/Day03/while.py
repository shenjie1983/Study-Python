'''
@Descripttion:
@version: 0.1
@Author: 沈洁
@Date: 2019-11-27 09:17:23
@LastEditors: 沈洁
@LastEditTime: 2019-11-27 09:28:55
'''
import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入猜测的数：'))
    if number < answer:
        print('放大胆，你猜的太小了')
    elif number > answer:
        print('你胆子太大了，悠着点')
    else:
        print('祝贺你，猜对了')
        break

print('你一共猜了%d次' % counter)
if counter < 3:
    print('你是神算子')
elif counter > 7:
    print('你智商欠缺')
else:
    print()
