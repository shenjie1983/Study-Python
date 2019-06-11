"""
条件控制    循环控制    分支
if else     for while
选择性问题
"""

# 情绪 mood
# mood = True
MOOD = False

if MOOD:
    print("mood go to left")
else:
    print("mood go to right")


#if else条件判断
A = 1
B = 2
C = 3
D = []

# if d: 判断空，如果为空往下执行
if A or B + 1 == C:
    print("go to left")
else:
    print("go to right")

X = input()

if X:
    print("x go to left")
else:
    print("x go to right")
