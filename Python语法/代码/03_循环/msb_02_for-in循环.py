for item in 'Python':  # 第一次取出来的是 P，将 P 赋给 item 的值输出
    print(item)

# range() 产生一个整数序列，也是一个可迭代对象
for i in range(2, 10, 2):
    print(i)

# 如果不需要使用自定义变量，可以将自定义变量谢伟 ’_'
for _ in range(5):
    print("人生苦短，我用Python")

print("使用 for 循环，计算1到100之间的偶数和")
sum = 0  # 用于存储偶数和
for item in range(1, 101, 2):
    sum += item
print(sum)
