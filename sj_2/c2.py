""" 
1.parameter_list参数列表可以没有
2.return value
3.如果没有return，则默认返回None

def funcname(parameter_list):
    pass

"""

# 1.实现两个数字的相加
# 2.打印输入的参数

# import sys
# sys.setrecursionlimit(1000)

# 必须参数，必须传递，否则报错
def add(x, y):
    # 形式参数，形参
    result = x + y
    return result

def print_code(code):
    print(code)
    # 注释return code 后返回None
    return code

a =  add(1,2) # 实际参数，实参
b = print_code('result')

print(a, b)
