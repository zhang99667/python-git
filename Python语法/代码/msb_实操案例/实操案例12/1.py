"""计算○的面积和周长"""
import math


class Circle(object):
    def __init__(self, r):
        self.r = r

    @staticmethod
    def get_raea():
        return math.pi * math.pow(r, 2)

    @staticmethod
    def get_perimeter():
        return 2 * math.pi * r


if __name__ == '__main__':
    r = float(input("输入半径"))
    print("%.2f" % Circle.get_raea())
    print("%.2f" % Circle.get_perimeter())
