from random import randint

face = randint(1, 6)
if face == 1:
    result = '帅帅调皮'
elif face == 2:
    result = '帅帅跳舞'
elif face == 3:
    result = "帅帅吵闹"
elif face == 4:
    result = '帅帅锻炼'
elif face == 5:
    result = '帅帅开车'
print(result)
