""" Mini计算器 """


def calc(a,b, op):
    if op == "+":
        return add(a,b)
    elif op == "*":
        return mul(a,b)
    elif op == "-":
        return sub(a,b)
    elif op == "/":
        if a == 0:
            return "除数不能为0"
        return div(a,b)


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


if __name__ == '__main__':
    a = int(input("第一个数:"))
    b = int(input("第二个数："))
    op = input("运算符：")
    print(calc(a, b, op))
