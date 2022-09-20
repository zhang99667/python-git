"""任务2：模拟用户登录"""

for i in range(1, 4):
    username = input("username:")
    pwd = input("password:")
    if username == "admin" and pwd=="8888":
        print("登陆成功")
        break
    else:
        print("用户名和密码错误")
        if i<3:
            print("您还有%d次"%(3-i))
        else:
            print("没有机会了")

