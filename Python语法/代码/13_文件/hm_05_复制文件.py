# 1. 打开
file_read = open("README.md","r")
file_write = open("README[副本].md","w")

# 2. 读写
file_write.write(file_read.read())

# 3. 关闭
file_read.close()
file_write.close()