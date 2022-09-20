"""任务3：猜数游戏"""
import random

number=random.randint(1,100)
for i in range(1,11):
    num_str=int(input("请输入数字："))
    if num_str<number:
        print("小了")
    elif num_str>number:
        print("大了")
    else:
        print("猜对了")
        break
print("你猜了%d次"%i)
if i<3:
    print("真聪明")
elif i<=7:
    print("good")
else :
    print("xueix")