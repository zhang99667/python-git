file = open("README.md")

while True:
    text = file.readline()

    # 判断是否读取到内容
    if not text:
        break

    # 每读取一行的末尾已经有了一个 '\n'
    print(text,end="")

file.close()