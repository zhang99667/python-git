# Python语言提供的内置数据结构
# 与列表、字典一样都属于可变类型的序列
# 集合是没有value的字典【只有key，没有value】

"""集合的创建方式"""

""" 1. 使用花括号 """
# 集合和字典类似，集合中的 key 不能重复
# 字典中的 key 不能重复 value 可重复
s = {2, 3, 4, 5, 6, 7, 8, 9}
print("s：", s)

""" 2. 使用内置函数 set() """
s1 = set(range(6))
print("s1：", s1, "类型：", type(s1))

# 可以将列表转换成集合
s2 = set([1, 2, 3, 4, 5, 6])
print("s2：", s2, "类型：", type(s2))

# 将元组转换成集合
s3 = set((1, 2, 3, 4, 5, 65))
print("s3：", s3, "类型：", type(s3))

# 将字符串转换成集合
s4 = set("python")  # 集合当中的元素是无序的
print("s4：", s4, "类型：", type(s4))

s5 = set({12, 4, 34, 55, 66, 44, 4})
print("s5：", s5, "类型：", type(s5))

# 定义空集合
s6 = {}  # 这种方式默认为 dict 类型
print(type(s6))
# 应该使用 set() 方法创建空集合
s6 = set()
print(type(s6))
