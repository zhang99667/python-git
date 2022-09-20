class Cat:
    """这一个猫类"""

    def eat(self):
        # 哪一个对象调用的方法，self 就是哪一个对象的引用
        print("%s 小猫爱吃鱼" % self.name)

    def drink(self):
        print("%s 小猫爱喝水" % self.name)




# 创建猫对象
tom = Cat()

# 可以使用 .属性名，利用赋值语句就可以了
tom.name = "Tom"

tom.drink()
tom.eat()
print("tom的内存地址", tom)

# 在创建一个猫对象
lazy_cat = Cat()
lazy_cat.name = "大懒猫"

lazy_cat.eat()
lazy_cat.drink()
print("lazy_cat的内存地址", lazy_cat)
