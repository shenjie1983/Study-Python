from enum import Enum
# import Enum

class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

class Common():
    YELLOW = 1

print(VIP.YELLOW)
# 可以通过value属性获取标签的数值，name获取标签的名字
print(VIP.GREEN.value)
print(VIP.GREEN.name)
print(VIP['GREEN'])

# 枚举类型、枚举的名字、枚举的值

# 可以便利操作
for v in VIP:
    print(v)