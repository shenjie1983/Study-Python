# re模块下另外两个函数介绍
# match
# search

import re

s = '83C7D1D8E67'

r1 = re.match('\d', s)
print(r1.span())

r2 = re.search('\d', s)
print(r2.group())

# 推荐使用findall
r3 = re.findall('\d', s)
print(r3[1])
