class Women:

    def __init__(self, name):
        self.name = name;
        self.__age = 18

    def __secret(self):
        # 在对象的方法内部，是可以访问对象的私有属性的
        print("%s 的年龄是 %d" % (self.name, self.__age))


XiaoFang = Women("小芳")

# 伪私有属性 在外界不能够被直接访问
print(XiaoFang._Women__age)
# 伪私有方法 同样不允许在外界直接访问
XiaoFang._Women__secret()