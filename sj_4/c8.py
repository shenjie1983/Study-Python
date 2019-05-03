# 组
# 小括号（）中字符是且
# 中括号[]中字符是或
import re
a = 'PythonPythonPythonPythonPython'


r = re.findall('(Python){3}', a)
print(r)
