"""任务1：记录用户登录日志"""
import time

LOG_FILE_NAME = "LOG.TXT"


def login():
    user_name = input("输入用户名：")
    pwd = input("输入密码：")
    if user_name == "123" and pwd == "123":
        print("登陆成功")
        write_info(user_name)  # 记录日志
    else:
        print("登陆失败，账号或密码错误!")


# 读取日志
def read_info():
    try:
        with open(LOG_FILE_NAME, "r") as file:
            while True:
                line = file.readline()
                if line == "":
                    break
                else:
                    print(line)
    except FileNotFoundError:
        print("未找到日志文件")


# 写入日志
def write_info(user_name, ):
    with open(LOG_FILE_NAME, "a") as file:
        str = "用户名:%s,登陆时间:%s" % (user_name, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        file.write(str)


if __name__ == '__main__':
    print("1登陆，2查看日志，其他退出")
    while True:
        choose = input("请选择：")
        if choose == "1":
            login()
        elif choose == "2":
            read_info()
        else:
            break
