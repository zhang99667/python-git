def multiple_table():

    # 九九乘法表
    i = 1
    j = 1
    result = 0

    while i <= 9:

        j = 1
        while j <= i:
            result = i * j
            print("%d * %d = %d" % (i, j, (i * j)), end="")
            print("\t", end="")
            j += 1

        print("")
        i += 1
