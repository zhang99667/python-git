"""任务1：循环输出26个字母对应的ASCII码值"""
a = 97
for i in range(0, 26):
    print("%c --> %d" % ((i + a),(a+i)))
