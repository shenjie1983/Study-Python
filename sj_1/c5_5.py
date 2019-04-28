"""

import t.c5_1 as x
print(x.a)

"""

# 引用c5_1模块import * 方式受到__all__影响，b被阻止，终止程序，报错未执行
# *引用尽可能不用
from t.c5_1 import *

# 引用c5_1模块中a、b、c、d四个元素
# from t.c5_1 import (a, b, c, d)

print(a)
print(b)
print(c)
print(d)
