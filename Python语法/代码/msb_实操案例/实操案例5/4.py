"""任务4：计算100-999之间的水仙花数"""
import math

for num in range(100, 1000):
    bai = num // 100
    shi = num % 100 // 10
    ge = num % 100 % 10
    if math.pow(bai, 3) + math.pow(shi, 3) + math.pow(ge, 3) == num:
        print(num)
