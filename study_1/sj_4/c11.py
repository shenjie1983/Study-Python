# sub函数（二）
# 把函数作为参数传递（一）
import re

def convert(value):
    # pass
    # value不是字符串，是一个字符串，print(value)运行结果：
    # <re.Match object; span=(6, 8), match='C#'>
    # <re.Match object; span=(12, 14), match='C#'>
    # <re.Match object; span=(17, 19), match='C#'>

    matched = value.group()
    return '!!' + matched + '!!'

# 将lanuage中C#替换为GO等
lanuage = 'PythonC#JavaC#PHPC#'
# count控制替换数量，数值为1，表示只能替换1次
# r = re.sub('C#', 'GO', lanuage, 1)

#函数做参数传入sub的第二个参数，作为替换成的字符串
r = re.sub('C#', convert, lanuage, 0)

print(r)

