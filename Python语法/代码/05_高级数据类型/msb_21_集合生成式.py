# 将 [] 修改为 {} 就是列表生成式
# 没有元组生成式，元组是不可变序列

"""列表生成式"""
lst = [i * i for i in range(6)]
print(lst)

"""集合生成式"""
s = {i * i for i in range(10)}
print(s) # 集合无序
