for item in range(100, 1000, 1):
    bai = item // 100
    shi = item % 100 // 10
    ge = item % 10
    if (bai ** 3 + shi ** 3 + ge ** 3) == item:
        print(item)
