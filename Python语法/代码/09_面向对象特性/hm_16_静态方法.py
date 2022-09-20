class Dog(object):

    # 不需要访问 Dog 类属性、对象属性。可以把他定义成静态方法
    @staticmethod
    def run():
        print("小狗要跑...")

# 通过类名.调用静态方法
Dog.run()
