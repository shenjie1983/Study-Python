import re
qq = '10000001'

# ^ 从字符串首位开始匹配
# & 从字符串末尾开始匹配
# 匹配4到8位任意数字
# QQ是否符合4到8位
r = re.findall('^\d{4,8}', qq)
print(r)
