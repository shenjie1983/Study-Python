# 枚举之间比较

from enum import Enum

class VIP(Enum):
    YELLOW = 1
    # 别名
    YELLOW_ALIAS = 1
    GREEN = 2
    BLACK = 3
    RED = 4

class VIP1(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

# result = VIP.GREEN > VIP.BLACK 
# result = VIP.GREEN is  VIP1.GREEN 
result = VIP.GREEN == VIP.BLACK
print(result)