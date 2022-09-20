"""任务3：商品价格大竞猜"""
import random

price = random.randint(1000, 1500)
print("今日竞猜的商品是小米扫地机器人：价格在[1000-15000]")
guess = int(input("输入竞猜价格："))
if guess == price:
    print("猜对了")
elif guess > price:
    print("大了")
elif guess < price:
    print("小了")
