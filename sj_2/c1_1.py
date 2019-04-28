# 1.参数列表可以没有
# 2.return value None
# def funcname(parameter_list):
#     pass
# 1.实现两个数字的相加
# 2.打印输入的参数

# import sys
# sys.setrecursionlimit(1000)

def add(x, y):
    result = x + y
    return result

def print_code(code):
    print(code)
    return code

a =  add(1,2)
b = print_code('result')

print(a, b)
