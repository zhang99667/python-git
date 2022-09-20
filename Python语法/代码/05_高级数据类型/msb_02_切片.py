lst = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# start = 1,stop = 6,step = 1
print(lst[1:6:1])

# 原列表id 和切片后的列表id不同
print("原列表Id%s" % (id(lst)), "\t切片ID%s" % (id(lst[1:6:1])))

# step 为空 -> 默认步长为1
print("step 为空 -> 默认步长为1：", lst[1:6])
# start为空 -> 默认0
print("start为空 -> 默认0：", lst[:8:1])
# stop为空 -> 默认8
print("stop为空 -> 默认8：", lst[5::1])

# step 为负数的情况
print("==========步长为负的情况===========")
print("原列表：", lst)
# 若 step 为 -1 会将 lst 进行逆置
print("步长为 -1 时：", lst[::-1])

# start=7 stop省略 stop=-1
print("start = 7 stop = 0 stop = -1：", lst[7::-1])  # [80, 70, 60, 50, 40, 30, 20, 10]
# start=7 stop=0 stop=-2
print("start = 7 stop = 0 stop = -2：", lst[7:0:-2])  # [80, 60, 40, 20]
