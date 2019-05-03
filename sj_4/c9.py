import re
lanuage = 'PythonC#\nJavaPHP'

r = re.findall('c#.{1}', lanuage, re.I| re.S)
print(r)