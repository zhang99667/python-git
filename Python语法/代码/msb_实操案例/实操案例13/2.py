"""任务2：请使用面向对象的思想，设计自定义类，描述出租车和家用轿车的信息。"""


class Car(object):
    def __init__(self, type, no):
        self.type = type
        self.no = no

    def start(self):
        pass

    def stop(self):
        pass


class Taxi(Car):
    def __init__(self, type, no, company):
        super().__init__(type, no)
        self.company = company

    def start(self):
        print("乘客您好")
        print("我是%s出租车公司的，我的车牌是%s，请问您去哪里" % (self.company, self.no))

    def stop(self):
        print("目的地到了，请您付款下车，欢迎再次乘坐")


class FaminlyCar(Car):
    def __init__(self, type, no, name):
        super().__init__(type,no)
        self.name = name

    def stop(self):
        print("目的地到了我们去玩吧")

    def start(self):
        print("我是%s我的骑车我做主" % self.name)


if __name__ == '__main__':
    taxi1 = Taxi("上海大众", "长城", "京A123")
    taxi1.start()
    taxi1.stop()

    familycar1 = FaminlyCar("上海大众", "长城","jack")
    familycar1.start()
    familycar1.stop()
