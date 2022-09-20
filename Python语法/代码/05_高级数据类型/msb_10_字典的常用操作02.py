score = {"张三": 100, "王五": 98, "李四": 45}

# 获取所有的key
keys = score.keys()
print("keys = ", keys)  # dict_keys(['张三', '王五', '李四'])
print("keys的类型：", type(keys))  # <class 'dict_keys'>
# 将所有 key 组成的视图转换成列表
print("将所有 key 组成的视图转换成列表：", list(keys))

print()

# 获取所有的 value
values = score.values()
print("values = ", values)  # dict_values([100, 98, 45])
print("values的类型：", type(values))  # <class 'dict_values'>
print("将所有 value 组成的视图转换成列表：", list(values))

print()

# 获取所有的 key-value 对
items = score.items()
print("key-value = ", items)
print("key-value 的类型:", type(items))
# 转换成列表后的字典，以元组形式存储在列表中
print(list(items))
