# 把函数作为参数传递（二）
# for循环实现

# 找出字符串中所有数字，大于等于6的替换成9，小于6的替换为0
# 使用for循环的方式编写

# def s(x1):
#     for x in x1:
#         if x.isdigit() == True:
#             if int(x) >= 6:
#                 x = 9
#             else:
#                 x = 0
#         else:
#             x = x
#         print(x,end = '')

# x1 = 'A8C3721D86'
# x2 = s(x1)
# print(x2, end='')



x1 = 'A8C3721D86'
for x in x1:
    # print(x.isdigit())
    if x.isdigit() == True:
        if int(x) >= 6:
            x = 9
        else:
            x = 0
    else:
        x = x
    print(x, end='')

