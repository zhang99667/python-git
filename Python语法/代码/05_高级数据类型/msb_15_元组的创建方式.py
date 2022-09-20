"""元组的创建方式"""

"""第一种方式，使用()"""
t = ("python", "world", 98)
print("元组t的内容：", t)
print("元组t的类型：", type(t))

# 定义元组的小括号可以省略
t = "python", "world", 98
print("元组t的内容：", t)
print("元组t的类型：", type(t))

# 如果元组中只包含一个元素，类型为元素本身的类型
t1 = ("python")
print("元组中只有一个元素时，类型为元素本身的类型：", type(t1))
# 若只有一个元素时，可以使用逗号，放在末尾
t1 = ("python",)
print("元组中只有一个元素，使用逗号，放在末尾的类型：", type(t1))

"""第二种创建方式，使用内置函数 tuple()"""
t2 = tuple(("python", "world", 98))
print(t2)

# 空列表创建方式
lst = []
lst1 = list()

# 空字典创建方式
d = {}
d2 = dict()

# 空元组创建方式
t4 = ()
t5 = tuple()

print("空列表", lst, lst1)
print("空字典",d,d2)
print("空元组",t4,t5)
