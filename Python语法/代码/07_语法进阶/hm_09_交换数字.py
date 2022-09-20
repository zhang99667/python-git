a = 6
b = 100
print("交换前：a=%d b=%d" % (a, b))

# 解法1 - 使用其他变量
temp = b
b = a
a = temp

# 解法2 - 不适用跟其他变量
a = a + b
b = a - b
a = a - b

# 解法3 - Python 专有
# a, b = (b, a)

a, b = b, a
print("交换后：a=%d b=%d" % (a, b))
