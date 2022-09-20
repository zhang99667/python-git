# 生成列表的公式

lst = [i for i in range(1, 10)]  # [1,10) 左闭右开
print(lst)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]


lst = [i * 2 for i in range(1, 6)]  # [1,6) 左闭右开
print(lst)  # [2, 4, 6, 8]

lst = [i**2 for i in range(1, 10)]  # [1,10) 左闭右开
print(lst)  # [1, 4, 9, 16, 25, 36, 49, 64, 81]
