# Student为类的名称（类名）由一个或多个单词组成，每个单词的首字母大写，其余小写
class Student:
    native_place = "吉林"  # 直接写在类里的变量，称为类属性

    # 初始化方法
    def __init__(self, name, age):
        # self.name 称为实体属性，进行了一个赋值的操作，将全局变量的name的值赋给一个实体属性
        self.name = name
        self.age = age

    # 实例方法【类里定义的方法称为方法】
    def eat(self):
        print("学生在吃饭...")

    # 静态方法
    @staticmethod
    def method():
        print("静态方法")

    # 类方法
    @classmethod
    def cm(cls):
        print("类方法")


# 在类之外定义的方法称为函数
def drink():
    print("喝水...")
