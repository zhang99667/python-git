class Cat:
    """这一个猫类"""

    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫爱喝水")


# 创建猫对象
tom = Cat()
tom.drink()
tom.eat()
print("tom的内存地址", tom)

# 在创建一个猫对象
lazy_cat = Cat()
lazy_cat.eat()
lazy_cat.drink()
print("lazy_cat的内存地址", lazy_cat)
