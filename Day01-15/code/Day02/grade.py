'''
@Descripttion: 百分制成绩转等级制成绩
@version: 0.1
@Author: 沈洁
@Date: 2019-10-12 10:28:25
@LastEditors: 沈洁
@LastEditTime: 2019-10-12 10:36:01
'''
score = float(input('请输入成绩：'))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('对应的等级是：', grade)
