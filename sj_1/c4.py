a = [1, 2, 3, 4, 5, 6, 7, 8]
# 打印出中相间隔的

for i in range(0, len(a), 2):
    print(a[i], end=' | ')

b = a[0:len(a):2]

print(b)

# 会写代码，非常容易
# 高性能、封装性（可复用）、抽象