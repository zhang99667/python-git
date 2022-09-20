# 1. 打开
file_read = open("README.md","r")
file_write = open("README[副本].md","w")

# 2. 读写
while True:
    # 读取一行内容
    text = file_read.readline()
    # 判断是否读取到内容
    if not text:
        break

    file_write.write()

# 3. 关闭
file_read.close()
file_write.close()