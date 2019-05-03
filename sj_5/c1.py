# 类型
# 腾讯各种砖——1、绿钻、黄钻、红钻、黑钻等，通常存储数据，可读性弱
# python提供枚举

# 导入引用枚举类
from enum import Enum

# 枚举定义的标识，建议使用大写
class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

print(VIP.YELLOW)
