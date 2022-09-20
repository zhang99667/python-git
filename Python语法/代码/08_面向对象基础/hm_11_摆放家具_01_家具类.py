class HouseItem:

    def __init__(self, name, area):
        self.name = name;  # 名字
        self.area = area;  # 占地面积

    def __str__(self):
        return "【%s】 占地 %.2f 平米" % (self.name, self.area)


# 1. 创建家具
bad = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
tale = HouseItem("餐桌", 1.5)
print(chest)
