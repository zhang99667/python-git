# key 不允许重复，重复会覆盖掉
person = {"name": "张三", "name": "李四"}
print(person)

# value 可以重复
person = {"name": "张三", "nick": "张三"}
print(person)

# 字典中的元素是无序的，不能像列表一样随意插入元素
lst = [10, 20, 30]
lst.insert(1, 100)
print(lst)

# 字典也可以根据需要动态地伸缩
# 字典会浪费较大的内存，是一种使用空间换时间的数据结构