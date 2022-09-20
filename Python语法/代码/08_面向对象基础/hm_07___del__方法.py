class Cat:

    def __init__(self, new_name):
        self.name = new_name

        print("%s 来了" % self.name)

    # 当一个 对象被从内存中销毁前 ，会自动调用`__del__`方法
    def __del__(self):
        print("%s 我去了" % self.name)


tom = Cat("Tom")
print(tom.name)
print("*" * 20, "已销毁", "*" * 20)
