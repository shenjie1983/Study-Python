import re


a = 'C|C++|Java|C#|Python|Javascript'

# re.findall('正则表达式', a)
r = re.findall('Python', a)
if len(r) > 0:
    print('字符串中包含Python')
