# 枚举的数值可以时字符串
#from enum import Enum


# 强制要求必须时数字,限制为整型，
# 如果要限制数值不能相同装饰器unique
from enum import IntEnum,unique

@unique
#class VIP(Enum):
class VIP(IntEnum):
    YELLOW = 1
    # GREEN = 'sts'
    GREEN = 1
    BLACK = 3
    RED = 4
    
# 23种设计模式，单例模式
