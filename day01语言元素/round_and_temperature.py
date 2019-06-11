# coding=utf-8
# 华氏温度转摄氏温度F=1.8c+32
import math
F = float(input('F = '))
f = (F - 32) / 1.8
print("%.1f华氏温度 = %.1f摄氏温度" % (F, f))

# 输入半径计算圆的周长和面积
r = int(input('r = '))
s = r**2 * 3.14
c = 2 * r * 3.14
print('面积=%.2f' % s)
print('周长=%.2f' % c)

# 示例：
radius = float(input('请输入圆的半径: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)
