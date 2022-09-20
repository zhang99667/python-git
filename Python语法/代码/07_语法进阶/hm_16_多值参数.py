# 参数名前增加一个 * 可以接收 元组
# 参数名前增加两个 * 可以接收 字典

def demo(num,*nums,**person):

    print(num)
    print(nums)
    print(person)

# demo(1)
demo(1,2,3,4,5,name="小明")