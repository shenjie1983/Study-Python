# group分组的概念

import re

s = 'life is short,i use python'

# r = re.search('life(.*)python', s)
# print(r.group(1))

r = re.findall('life(.*)python', s)
print(r)

# 扩展，另要查找两个python之间的信息
x = 'life is short,i use python,i love python'
# r1 = re.findall('life(.*)python(.*)python', x)
# print(r1)
r1 = re.search('life(.*)python(.*)python', x)
# print(r1.group(0))
# print(r1.group(1))
# print(r1.group(2))
# print(r1.group(0, 1, 2))
print(r1.groups())