# 内置函数zip()
# 用于将可迭代的对象作为参数，将对象中对应的元素打包成一个元组，然后返回由这些元组组成的列表

items = ["Fruits", "Books", "Others"]
prices = [98, 78, 85, 99]

# 以元素少的为基准生成字典
d = {item: price for item, price in zip(items, prices)}
print(d)
