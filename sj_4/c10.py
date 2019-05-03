# sub函数（一）
import re

lanuage = 'PythonC#JavaC#PHPC#'
# count值为一，只能替换1此
r = re.sub('C#', 'GO', lanuage, 1)
# lanuage.replace('C#', 'GO')
# 使用replace并没有替换，是因为字符串是不可变的。需要新生成一个字符串
lanuage = lanuage.replace('C#', 'GO')
print(lanuage)
print(r)