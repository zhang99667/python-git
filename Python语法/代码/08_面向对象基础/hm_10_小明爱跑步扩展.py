class Person:

    def __init__(self, name, weight):
        self.name = name;
        self.weight = weight;

    def __str__(self):
        return "我是 %s 体重 %dkg" % (self.name, self.weight)

    def run(self):
        print(self.name, "跑步...")
        self.weight -= 0.5

    def eat(self):
        print(self.name, "吃东西...")
        self.weight += 1


xiaoMing = Person("小明", 75.0)
print(xiaoMing.__str__())
xiaoMing.eat()
xiaoMing.run()
print(xiaoMing.__str__())

# 小美

xiaoMei = Person("小美", 45)
xiaoMei.eat()
xiaoMing.run()
print(xiaoMei)
