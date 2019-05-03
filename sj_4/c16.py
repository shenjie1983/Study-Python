# 反序列化

import json

json_str1 = '{"name":"qiyue", "age":18}'
json_str2 = '[{"name":"qiyue", "age":18, "flag":false}, {"name":"qiyue", "age":18, "flag":false}]'

# loads函数将json数据类型转化为python数据类型
# 反序列化
student1 = json.loads(json_str1)
print(type(student1))
print(student1)

student2 = json.loads(json_str2)
print(type(student2))
print(student2)