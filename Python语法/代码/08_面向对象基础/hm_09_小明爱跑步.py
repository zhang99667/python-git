class Person:

    def __init__(self, name, weight):
        self.name = name;
        self.weight = weight;

    def __str__(self):
        return self.name, self.weight, "kg"

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
