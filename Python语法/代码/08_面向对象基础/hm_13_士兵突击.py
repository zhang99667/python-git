# 武器
class Gun:

    def __init__(self, model, bullet_count=0):
        self.model = model  # 枪的型号
        self.bullet_count = bullet_count  # 枪的子弹数量

    def __str__(self):
        return "【%s】 子弹：%d 发" % (self.model, self.bullet_count)

    def add_bullet(self, count):
        self.bullet_count += count
        print("子弹填充完毕")

    def shoot(self):
        # 1. 判断子弹数量
        if self.bullet_count <= 0:
            print("【%s】 没有子弹了，请装填子弹！" % self.model)
            return

        # 2. 发射子弹
        self.bullet_count -= 1

        # 3. 提示信息
        print("发射子弹【剩余子弹%d】" % self.bullet_count)


# 士兵：
class Soldier:

    def __init__(self, name, gun=None):
        self.name = name  # 姓名
        self.gun = gun  # 新兵没枪

    def fire(self):
        if self.gun is None:
            print("【%s】还没枪..." % self.name)
            return
        # 警示
        print("准备射击")

        # 射击
        self.gun.shoot()

# 创建武器
ak47 = Gun("ak47", 30)

# 创建士兵
s1 = Soldier("许三多")
# 给士兵发枪
s1.gun=ak47
# 让士兵射击
s1.fire()