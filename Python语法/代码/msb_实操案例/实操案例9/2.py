"""任务2：格式化输出商品的名称和单价"""
lst = [
    ["01", "电风扇", "美的", "500"],
    ["02", "洗衣机", "TCL", "1000"],
    ["03", "微波炉", "老板", "400"]
]


def show():
    print("编号\t名称\t\t品牌\t\t单价")
    for item in lst:
        for i in item:
            print(i, end=" \t\t")
        print()


show()

print("-" * 25, "格式化", "-" * 25)
for item in lst:
    item[0] = "000" + item[0]
    item[3] = item[3] + "¥"

show()
