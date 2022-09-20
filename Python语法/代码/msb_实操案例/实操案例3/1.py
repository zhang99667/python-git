"""任务1：将指定的十进制数转换成二进制、八进制、十六进制"""
try:
    num = int(input("请输入一个十进制整数"))
except ValueError:
    print("请输入整数")
    exit()

print("%d二进制为" % num, bin(num))  # 二进制
print("%d八进制为" % num, oct(num))  # 八进制
print("%d十六进制为" % num, hex(num))  # 十六进制
