'''
@Descripttion: 
@version: 0.1
@Author: 沈洁
@Date: 2019-11-12 23:07:15
@LastEditors: 沈洁
@LastEditTime: 2019-11-12 23:12:13
'''
for i in range(1, 10):
    for j in range(1, i+1):
        print('%d*%d=%d' % (i, j, i*j), end='\t')
    print()
