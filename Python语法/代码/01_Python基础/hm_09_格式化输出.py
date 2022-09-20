# 定义字篷串变量 name ，输出我的名字叫小明，请多多关照！
name = "小明"
print("我的名字叫%s，请多关照！" % name)

# 定义整数变量 student_no,输出我的学号是 000001
student_no = 1
print("我的学号是%06d" % student_no)

# 定义小数price、weight、money,
# 输出苹果单价9.00元斤，购买了5.00斤，需要支付45.00元
price = 8.5
weight = 7.5
money = price * weight

print("苹果单价%.2f元斤，购买了%.2f序，需要支付%.2f元" % (price, weight, money))

# 定义一个小数scale,输出数据比例是10.00%
scale = 1
print("数据比例是%.2f%%" % (scale * 10))
