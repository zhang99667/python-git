# 全局变量
num = 10


def demo1():
    # 希望修改全局变量的值 - 使用 global 声明一下变量即可
    # 在 python 中，是不允许直接修改全局变量的值
    # global 关键字会告诉解释器后面的变量是一个全局变量
    # 可以使用 debug 查看
    global num
    num = 99

    print("demo1 ==> ", num)


demo1()


def demo2():
    print("demo2 ==> ", num)


demo2()
