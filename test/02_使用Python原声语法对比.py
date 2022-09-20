import numpy as np


def python_sum(n):
    """Python 实现两个数组的加法"""

    # 列表解析式

    a = [i ** 2 for i in range(n)]
    b = [i ** 3 for i in range(n)]
    c = []

    for i in range(n):
        c.append(a[i] + b[i])
    return c

print(python_sum(10))


def numpy_sum(n):
    """NumPy 实现数组的加法"""
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    return a + b

print(numpy_sum(10))
