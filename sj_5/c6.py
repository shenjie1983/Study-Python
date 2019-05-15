from enum import Enum
# import Enum

class VIP(Enum):
    # 连接数据库时，建议使用数值，
    # 而不是使用字符串存储标签
    YELLOW = 1
    # 别名
    YELLOW_ALIAS = 1
    GREEN = 2
    BLACK = 3
    RED = 4

class Common():
    YELLOW = 1

print(VIP.YELLOW)

# 数据库查到具体数字，如何对应枚举类型
# 数据库取到数据a
a = 1
print(VIP(a))

# if a == VIP.YELLOW:
# if a == 1:
#     print

# 直接for in 不会打印出别名
# for v in VIP.__members__.items():
# for v in VIP.__members__:
#     print(v)