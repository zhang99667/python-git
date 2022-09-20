import random

# 1.从控制台输入要出的拳 -- 石头(1) / 剪刀(2) / 布(3)
player = int(input("输入要出的拳 -- 石头(1) / 剪刀(2) / 布(3)："))

# 2.电脑随机出拳 -- 先假定电脑只会出石头，完成整体代码功能
computer = random.randint(1,3)

# 3.比较胜负
print("玩家选择的拳头是 %d - 电脑出的拳是 %d" % (player, computer))

if ((player == 1 and computer == 2) \
        or (player == 2 and computer == 1) \
        or (player == 3 and computer == 1)):

    print("你赢了！")
# 平局
elif player == computer:
    print("平局！")
# 其他情况就是电脑获胜
else:

    print("你输了！")
