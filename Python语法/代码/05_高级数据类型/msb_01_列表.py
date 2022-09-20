a = 10  # 变量存储的是一个对象的引用
"""创建列表的第一种方式，使用方括号"""
lst = ["hello", "world", 98, "hello"]  # 列表对象
# 获取索引为0和-3的元素
print(lst[0], lst[-3])
# 返回列表索引，若列表中有相同元素只返回第一个元素的索引
print(lst.index("hello"))
# 返回列表索引，从 1 开始到 4（不包括 4 ）
print(lst.index("hello", 1, 4))

"""创建列表的第二种方式，使用list()"""
lst2 = list(["hello", "world", 98])  # 列表对象

for ls in lst:
    print(id(ls))
    print(type(ls))
    print(ls)

print(type(lst2))
