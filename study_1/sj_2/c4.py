# 序列解包
# 元素的个数要相等
# a = 1
# b = 2
# c = 3

a, b, c = 1, 2, 3
d = 1, 2, 3

"""
a = 1
b = 1
c = 1
另一种写法
a = b = c = 1
print(a, b, c)
"""


""" 
a, b, c = [1, 2, 3]

d = 1, 2, 3
a, b, c = d
"""

print(type(d))