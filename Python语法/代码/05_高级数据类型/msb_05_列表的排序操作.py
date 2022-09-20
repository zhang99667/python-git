lst = [20, 40, 10, 98, 54]

print("排序前的列表", lst)

# 开始排序，调用列表对象的sort方法，默认升序排序
lst.sort()
print("排序后列表：", lst)

# 通过指定关键字参数，将列表中的元素进行降序排序
# reverse=False -> 升序
# reverse=True -> 降序
lst.sort(reverse=True)
print(lst)

print("=========使用内置函数sorted()对列表进行排序，将产生一个新的列表对象===========")
lst = [20, 40, 10, 98, 54]

# 开始排序
new_list = sorted(lst)
print("原列表：", lst, " id：", id(lst))
print("排序后的列表：", new_list, " id：", id(new_list))
