# 注意：在开发时，应该把模块中的所有全局变量
# 定义在所有函数上方，就可以保证所有的函数
# 都能够正常地访问到每一个全局变量了
gl_num = 10
# 再定义一个全局变量
gl_title = "黑马程序员"
# 再定义一个全局变量
gl_name = "小明"

def demo1():
    print(gl_num)
    print(gl_title)
    print(gl_name)

demo1()


