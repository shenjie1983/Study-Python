'''
@Descripttion:掷骰子决定做什么事情
@version: 0.1
@Author: 沈洁
@Date: 2019-08-16 11:24:02
@LastEditors: 沈洁
@LastEditTime: 2019-10-12 10:38:00
'''

from random import randint

face = randint(1, 6)
if face == 1:
    result = '帅帅调皮'
elif face == 2:
    result = '帅帅跳舞'
elif face == 3:
    result = "帅帅吵闹"
elif face == 4:
    result = '帅帅锻炼'
elif face == 5:
    result = '帅帅开车'
print(result)
