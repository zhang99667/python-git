# 父类 A
class A:

    def demo(self):
        print("A -- demo 方法")

    def test(self):
        print("A -- test 方法")

# 父类 B
class B:

    def demo(self):
        print("B -- demo 方法")

    def test(self):
        print("B -- test 方法")

class C(A, B):
    """多继承可以让子类对象，同时具有多个父类的属性和方法"""
    pass

# 创建子类对象
c = C()
c.test()
c.demo()

print(C.__mro__)