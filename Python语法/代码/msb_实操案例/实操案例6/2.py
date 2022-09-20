"""任务2：京东购物流程"""
lst=[]
for i in range(0,5):
    goods=input("输入商品")
    lst.append(goods)

for item in lst:
    print(item)

cart=[]
while True:
    id_str=input("输入商品编号:")
    for item in lst:
        if item.find(id_str)!=-1:
            cart.append(item)
            break
    if id_str=="q":
        break
print("购物车：")
# 倒序输出
for item in range(len(cart),-1,-1,-1):
    print(item)

