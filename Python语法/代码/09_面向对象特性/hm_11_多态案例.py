class Dog(object):

    def __init__(self, name):
        self.name = name;

    def game(self):
        print("%s 蹦蹦跳跳的玩耍..." % self.name)


class XiaoTianQuan(Dog):

    # 重写父类的 game 方法
    def game(self):
        print("%s 飞到天上去玩耍..." % self.name)


class Person(object):

    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print(self.name, "和", dog.name, "快乐玩耍...")

        # 让狗玩耍
        dog.game()


# 1. 创建Dog对象
wangCai = XiaoTianQuan("哮天旺财")
# 2. 创建Person对象
xiaoMing = Person("小明")
# 3.调用 game_with_dog 方法
xiaoMing.game_with_dog(wangCai)