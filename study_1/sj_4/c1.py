# 正则表达式：是一个特殊的字符序列，一个字符串是否与我们设定的的字符序列，相匹配
# 快速检索文本、实现一些替换文本的操作
# 1.检查一串数字是否是电话号码
# 2.检测一个字符串是否符合email
# 3.把一个文本里指定的单词替换为另外一个单词
# JSON（XML）

a = 'C|C++|Java|C#|Python|Javascript'
if a.index('Python') > -1:
    print("'Python' in a")
else:
    print("'Python' not in a")
