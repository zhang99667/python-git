# 全局变量
num = 10


def demo1():
    # 希望修改全局变量的值
    # 在python中，是不允许直接修改全局变量的值
    # 如果使用赋值语句，会在函数内部，定义一个局部变量
    print("demo1 ==> ", num)

demo1()

def demo2():

    print("demo2 ==> ", num)

demo2()
