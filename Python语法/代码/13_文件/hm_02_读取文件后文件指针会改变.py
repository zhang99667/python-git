# 1. 打开文件
file = open("README.md")

# 2.读取
text = file.read()
print(text)

print("-" * 50)

# 再次读取
text = file.read()
print(text)

# 3. 关闭
file.close()
