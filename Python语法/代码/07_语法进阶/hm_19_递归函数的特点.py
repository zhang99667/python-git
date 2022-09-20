def sum_number(num):

    # 递归出口，没有出口会出现死循环
    if num == 0:
        return
    print(num)

    # 自己调用自己
    sum_number(num - 1)

sum_number(996)