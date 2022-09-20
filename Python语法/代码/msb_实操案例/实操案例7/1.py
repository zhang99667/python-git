"""任务2：模拟12306火车票订票下单"""
dict_ticket = {
    "G1569": ["北京南-天津南", "18：05", "18：39", "00：34"],
    "G1567": ["北京南-天津南", "18：15", "18：49", "00：34"],
    "G8917": ["北京南-天津西", "18：20", "19：19", "00：59"],
    "G203": ["北京南-天津南", "18：35", "19：09", "00：34"]
}

print("车次\t\t出发站-到达站\t\t出发时间\t\t到达时间\t\t历时时长")
print("-" * 65)
for item in dict_ticket:
    print(item, end="\t\t")
    for i in dict_ticket[item]:
        print(i, end="\t\t")
    print()

train_no = input("请输入与要购买的车次:")
persons = input("请输入乘车人，多人请用逗号分割：")
try:
    s1 = "您已购买了%s车次" % train_no  # 车次信息
    s2 = dict_ticket[train_no][0] +" "+ dict_ticket[train_no][1] + "开"  # 时间地点信息
    s3 = "请%s尽快换取纸质车票。【铁路客服】" % persons
    print(s1, s2, s3)
except:
    print("输入的车次不存在")