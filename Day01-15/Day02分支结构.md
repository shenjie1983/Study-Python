<!-- TOC -->

- [**《Day02 分支结构》**](#day02-分支结构)
    - [代码知识点汇总及拓展](#代码知识点汇总及拓展)
        - [随机数*randint()函数*](#随机数randint函数)
        - [无限循环*while true*](#无限循环while-true)
        - [python字典内置方法*dict.get*](#python字典内置方法dictget)
        - [字符串*isdigit*方法](#字符串isdigit方法)
        - [print](#print)
        - [正则表达式错误](#正则表达式错误)
    - [遗留问题](#遗留问题)
        - [rolldice3中randint函数为什么使用n+1，而不使用n，有原因吗](#rolldice3中randint函数为什么使用n1而不使用n有原因吗)

<!-- /TOC -->

# **《Day02 分支结构》**

## 代码知识点汇总及拓展
---
### 随机数*randint()函数*
*random模块，randint()函数*  
random.randint(a,b)
函数返回数字 N ，N 为 a 到 b 之间的数字（a <= N <= b），包含 a 和 b。

---

### 无限循环*while true*
while true 经常在不知道循环次数的时候使用，并且需要在循环内使用break才会停止

---
### python字典内置方法*dict.get*
*dict.get(key, default = None)*  
返回指定键的值；如果值不在字典中，返回default值

---
### 字符串*isdigit*方法
str.isdigit()	检测字符串是否只由数字组成

---
### print
print('xxx', end='')	末尾不换行，空字符串

---
### 正则表达式错误
>Anomalous backslash in string: '\\D'. String constant might be missing an r prefix.

\在Python中用作转义符号，\s代表Python语法中的一个转义字符，然而转义字符表中并没有这样一个字符，因而报错。
要表示正则表达式中的\D，也就是一个\再加上一个s共两个字符，有两种方式，一是使用两个\将反斜杠本身转义，然后再接s，也就是\\D；二是在字符串前面加上一个r表示该按字面含义解释该字符串，不进行转义，即r'\D'。

---
## 遗留问题
### rolldice3中randint函数为什么使用n+1，而不使用n，有原因吗
应该没有特殊原因