import prettytable


# 显示座位
def show_ticket(row_num):
    table = prettytable.PrettyTable()
    table.field_names = ["行号", "座位1", "座位2", "座位3", "座位4", "座位5"]
    for i in range(row_num):
        lst = ["第%d行" % (i + 1), "有票", "有票", "有票", "有票", "有票"]
        table.add_row(lst)
    print(table)


# 订票
def order_ticket(row_num, row, col):
    table = prettytable.PrettyTable()
    table.field_names = ["行号", "座位1", "座位2", "座位3", "座位4", "座位5"]
    for i in range(row_num):
        if int(row) == (i + 1):
            lst = ["第%d行" % (i + 1), "有票", "有票", "有票", "有票", "有票"]
            lst[int(col)] = "已售"
            table.add_row(lst)
        else:
            lst = ["第%d行" % (i + 1), "有票", "有票", "有票", "有票", "有票"]
            table.add_row(lst)
    print(table)

if __name__ == '__main__':
    show_ticket(5)

    order_ticket(5,3,2)