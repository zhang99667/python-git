""" 1. 交集  【操作后，原集合不发生变化】 """
s1 = {10, 20, 30, 40}
s2 = {20, 30, 40, 50, 60}
# 方式一：
print(s1.intersection(s2))
# 方式二：
print(s1 & s2)

""" 2. 并集操作 【操作后，原集合不发生变化】 """
# 方式一：
print(s1.union(s2))
# 方式二：
print(s1 | s2)

""" 3. 差集操作 """
# A - B
print(s1.difference(s2))  # {10}
print(s1 - s2)
# B - A
print(s2.difference(s1))  # {50, 60}
print(s2 - s1)

""" 4. 对称差集 """
print(s1.symmetric_difference(s2)) # {50, 10, 60}
print(s1 ^ s2)
