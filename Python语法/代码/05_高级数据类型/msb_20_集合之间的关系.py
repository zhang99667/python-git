s1 = {10, 20, 30, 40}
s2 = {20, 30, 40, 10}

"""判断两个集合是否相等，两种判断方式"""
print(s1 == s2)  # True 因为集合是无序的，所以只看元素是否相等
print(s1 != s2)  # False

"""判断一个集合是否是另一个集合的子集"""
s1 = {10, 20, 30, 40, 50, 60}
s2 = {10, 20, 30, 40}
s3 = {10, 20, 90}

print(s2.issubset(s1))  # True  -> s2 是 s1 的子集
print(s3.issubset(s1))  # False -> s3 是 s1 的子集

"""判断一个集合是否是另一个集合的超集"""
print(s1.issuperset(s2))  # True
print(s1.issuperset(s3))  # False

"""两个集合是否含有交集"""
print(s2.isdisjoint(s3))  # False -> 有交集为 False
s4 = {100, 200, 300}
print(s2.isdisjoint(s4))  # True -> 无交集为 True
