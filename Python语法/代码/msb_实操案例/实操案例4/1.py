# 任务1：支付密码的验证

"""方法一"""
pwd=input("enter password:")
if pwd.isdigit():
    print("通过")
else :
    print("不通过")

"""方法二"""
print("支付合法" if pwd.isdigit() else "不通过")