# 计算0~100之间所有偶数的累计求和结果
# 开发步骤
#
# 编写循环确认要计算的数字
# 添加结果变量，在循环内部处理计算结果

i = 0
# 1> 定义一个记录最终结果的变量
result = 0
while i <= 100:
    # 判断变量1中的数值，是否是一个偶数
    if i % 2 == 0:
        result += i
    i += 1
print(result)
