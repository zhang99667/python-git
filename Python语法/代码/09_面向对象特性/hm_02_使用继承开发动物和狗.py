class Animal:

    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")

class Dog(Animal):

    def bark(self):
        print("叫")

#创建一个对象·狗对象
WangCai = Dog()
WangCai.eat()
WangCai.drink()
WangCai.run()
WangCai.sleep()

