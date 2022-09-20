"""
请定义一个函数quadratic(a, b, c)，接收3个参数
返回一元二次方程 ax^2 + bx + c = ax
ax^2 + bx + c = 0 的两个解。
"""
import math


def quadratic(a, b, c):
    dt = b ** 2 - (4 * a * c)

    # dt < 0 无根
    if dt < 0:
        return -999,-999

    # dt > 0 两个不相等的实根
    elif dt > 0:
        x1 = ((-b) + math.sqrt(dt)) / (2 * a)
        x2 = ((-b) - math.sqrt(dt)) / (2 * a)

    # dt = 0 两个相等的实根
    else:
        x1 = x2 = (-b - math.sqrt(dt)) / (2 * a)
    return x1, x2


print(quadratic(1, -4, 3))
