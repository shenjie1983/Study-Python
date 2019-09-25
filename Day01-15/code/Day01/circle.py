'''
@Descripttion: 输入半径计算圆的周长和面积
@version: 0.1
@Author: 沈洁
@Date: 2019-09-04 16:46:09
'''
import math

radius = float(input('请输入圆的半径：'))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周长：%.2f 厘米' % perimeter)
print('面积: %.2f 平方厘米' % area)
print(math.pi)