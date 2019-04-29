# 概括字符集
# \d \D [a-z] [A-Z] [0-9] [^0-9]
# \w 匹配包括下划线的任何单词字符。等价于'[A-Za-z0-9_]'。
# \W 等价于'[^A-Za-z0-9_]' 
# \s 空白字符、\S 非空字符
import re

s = 'python 11\t11java&678p\nh\rp'

r = re.findall('\W', s)

print(r)