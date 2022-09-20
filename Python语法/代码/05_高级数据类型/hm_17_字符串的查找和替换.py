hello_str = "hello world"
# 1. 判断是否以指定字符串开始
print(hello_str.startswith("hello"))  # True

# 2. 判断是否以指定字符串结束
print(hello_str.endswith("world"))  # True

# 3. 查找指定字符串
# index 同样可以查找指定的字符串在大字符串中的索引
print(hello_str.find("llo"))
print(hello_str.find("abc"))

# 4. 替换字符串
# replace 方法执行完成之后，会返回一个新的字符串
# 注意：不会修改原有字符串的内容
print(hello_str.replace("world", "python"))

print(hello_str)
