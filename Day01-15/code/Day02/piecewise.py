'''
@Descripttion: 分段函数求值
        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
@version: 0.1
@Author: 沈洁
@Date: 2019-08-16 11:24:02
@LastEditors: 沈洁
@LastEditTime: 2019-09-23 12:01:49
'''
"""
        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
        
"""
x = float(input('x='))
if x > 1:
    y = 3 * x - 5
elif -1 <= x and x <= 1:
    y = x + 2
else:
    y = 5 * x + 3
print('f(%.2f)=%.2f' % (x, y))
