# 把函数作为参数传递（二）
# 一个重要的意义：开放接口
import re

# 找出字符串中所有数字，大于等于6的替换成9，小于6的替换为0
s = 'A8C3721D86'

def convert(value):
    matched = value.group()
    if int(matched) >= 6:
        return '9'
    else:
        return '0'

r = re.sub('\d', convert, s)
print(r)