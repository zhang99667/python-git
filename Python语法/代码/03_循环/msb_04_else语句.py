# else 和 for 搭配使用
for item in range(3):
    pwd = input("输入密码:")

    # else 和 if 搭配使用
    if pwd == "8888":
        print("密码正确")
        break;
    else:
        print("密码错误")
else:
    print("对不起，三次密码均输入错误。")

# else 和 while 搭配使用
a = 0
while a < 3:
    pwd = input("输入密码:")

    # else 和 if 搭配使用
    if pwd == "8888":
        print("密码正确")
        break;
    else:
        print("密码错误")
    a += 1
else:
    print("对不起，三次密码均输入错误。")
