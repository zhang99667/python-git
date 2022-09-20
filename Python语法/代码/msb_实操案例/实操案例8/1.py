coffee_name = ("蓝山", "卡布奇诺", "拿铁", "皇家咖啡", "女王咖啡", "美丽与哀愁")
print("welcome")
for index, item in enumerate(coffee_name):
    print(index + 1, item)

index=int(input("输入咖啡编号："))
if 0<=index<=len(coffee_name):
    print("您的咖啡%s到了"%coffee_name[index-1])