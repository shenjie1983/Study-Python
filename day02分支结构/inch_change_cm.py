"""
英寸和厘米互换
isalnum()必须是数字和字母的混合
isalpha()判断是否是字母，不区分大小写
isdigit()判断是否数字
"""

length = float(input("请输入长度："))
unit = input('请输入单位：')
if unit == 'in' or unit == '英寸':
    print('%.2f英寸=%.2f厘米' % (length, length * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%.2f厘米=%.2f英寸' % (length, length / 2.54))
else:
    print('请输入正确单位，例如：in、cm、英寸、厘米')
