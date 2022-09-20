def sum_number(num):
    # 1. 出口
    if num == 1:
        return 1

    # 累加求和
    return num + sum_number(num - 1)


print(sum_number(100))
