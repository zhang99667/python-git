# 1.定义布尔型变量 has_ticket 表示是否有车票
has_ticket = True
# 2.定义整型变量 knife_length 表示刀的长度，单位：厘米
knife_length = 99
# 3.首先检查是否有车票，如果有，才允许进行安检
if has_ticket:
    print("车票检查通过，准备开始安检")
    # 4.安检时，需要检查刀的长度，判断是否超过20厘米
    # 如果超过20厘米，提示刀的长度，不允许上车
    if knife_length > 20:
        print("刀的长度太长了，有%d厘米长，不允许上车" % knife_length)
    # 如果不超过20厘米，安检通过
    else:
        print("安检通过")
# 5.如果没有车票，不允许进门
else:
    print("没有车票，不允许进门")
