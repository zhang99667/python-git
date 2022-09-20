"""判断三角形"""


def is_triangle(a, b, c):
    try:
        if a < 0 or b < 0 or c < 0:
            raise Exception("三边不能为负")
        if a + b > c and b + c > a and a + c > b:
            print("三边为", a, b, c)
        else:
            raise Exception("不能构成三角形")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    a = int(input("1："))
    b = int(input("2："))
    c = int(input("3："))
    is_triangle(a, b, c)
