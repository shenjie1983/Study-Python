# 枚举优势 不可变，防止相同值出现
# 传统方式1：字典
a = {'yellow':1, 'green':2}
a['yellow'] = 3
#传统方式2：类封装
class TypeDiamond():
    yellow = 1
    green = 2