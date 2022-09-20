class HouseItem:

    def __init__(self, name, area):
        self.name = name  # 名字
        self.area = area  # 占地面积

    def __str__(self):
        return "【%s】 占地 %.2f 平米" % (self.name, self.area)


class House:

    def __init__(self, house_type, area):
        self.house_type = house_type  # 户型
        self.area = area  # 总面积
        # 剩余面积 -> 初始值等于总面积
        self.free_area = area
        self.item_list = []  # 家具名称列表

    def __str__(self):
        return ("户型：%s \n总面积：%.2f 【剩余：%.2f】 \n家具名称列表：%s"
                % (self.house_type, self.area, self.free_area, self.item_list))

    # 添加家具
    def add_item(self, item):
        print("要添加", item)
        if item.area > self.free_area:
            print("添加失败！%s 面积太大" % item.name)

            return

        # 将家具添加至房子中
        self.item_list.append(item.name)
        # 计算剩余面积
        self.free_area -= item.area


# 1. 创建家具
bad = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
tale = HouseItem("餐桌", 1.5)

# 2. 创建房子
myHouse = House("南北", 123)

# 3. 添加家具
myHouse.add_item(chest)
myHouse.add_item(bad)
myHouse.add_item(tale)

print(myHouse)
