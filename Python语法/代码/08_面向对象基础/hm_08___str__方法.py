class Cat:

    def __init__(self, new_name):
        self.name = new_name

        print("%s 来了" % self.name)

    # 当一个 对象被从内存中销毁前 ，会自动调用`__del__`方法
    def __del__(self):
        print("%s 我去了" % self.name)

    def __str__(self):
        # 必须返回一个字符串
        return "我是小猫[%s]" % self.name


tom = Cat("Tom")
print(tom)
print("*" * 20, "已销毁", "*" * 20)
