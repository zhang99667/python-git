"""任务3：模拟手机通信录"""
phones = set()  # 空集合
for i in range(5):
    info = input("请输入第%d个联系人的姓名和手机号" % (i + 1))
    phones.add(info)

for item in phones:
    print(item)