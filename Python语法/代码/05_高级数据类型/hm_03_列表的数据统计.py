name_list=["张三","李四","王五","张三","王小二"]

# len(length长度)函数可以统计列表中元素的总数
print(len(name_list))

# count方法可以统计列表中某一个数据出现的次数
count = name_list.count("张三")
print("张三出现了%d次" % count)

# 从列表中删除第一次出现的数据，如果数据不存在，程序会报销
name_list.remove("张三")

print(name_list)
