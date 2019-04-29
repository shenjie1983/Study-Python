import re
# 数量词
# * 匹配0次或者无线多次
# + 匹配1次或者无数多次
# ？匹配0次或者1次

s = 'python 11\t11java&678p\nh\rp'
# r = re.findall('[a-z][a-z]', s)
# 贪婪与非贪婪
# 贪婪：尽可能多匹配
sr1 = re.findall('[a-z]{3,6}', s)

#加？变为非贪婪,
sr2 = re.findall('[a-z]{3,6}?', s)
# print(sr1)

a = 'pytho0python1pythonn2'

ar1 = re.findall('python?', a)
ar2 = re.findall('python{1,2}', a)
ar3 = re.findall('python{1,2}?', a)
print(ar1,ar2,ar3)




