import random

import pygame.sprite
from plane_main import SCREEN_RECT


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):
        # 调用父类初始化方法
        super().__init__()

        """定义对象的属性"""
        # 图像地址，直接加载到 image
        self.image = pygame.image.load(image_name)
        # 图像大小，获取图像大小
        self.rect = self.image.get_rect()
        # 速度
        self.speed = speed

    def update(self):
        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed

    # 对象被从内存中销毁前，会被自动调用
    def __del__(self):
        # kill 方法会自动调用 __del__
        print("销毁精灵...", self.rect)


class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):
        # 1. 调用父类方法实现精灵的创建(image/rect/speed)
        super().__init__("./images/background.png")
        # 判断是否为交替图像，如果是，需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 调用父类的方法实现滚动
        super().update()

        # 判断是否移除屏幕，如果图像移除屏幕，将图像设置到屏幕上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):
        # 调用父类的 super 方法创建精灵，同时指定图片
        super().__init__("./images/enemy1.png")
        # 初始化敌机速度 - 随机
        self.speed = random.randint(1, 3)
        # 初始化敌机初试位置 - 随机
        # 敌机垂直方向，应该从屏幕外出现
        self.rect.bottom = 0
        # 敌机水平方向，从 最左侧【0】 - 最右侧【SCREEN_RECT.width - self.rect.width】
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)

    def update(self):
        super().update()

        # 判断敌机是否飞出屏幕，如果飞出屏幕，需要从精灵组删除敌机
        if self.rect.top > SCREEN_RECT.height:
            self.kill()


class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self):
        # 子弹向上方飞行，需要速度为负值
        super().__init__("./images/bullet1.png", -2)

    def update(self):
        super().update()
        # 判断子弹是否飞出屏幕，如果飞出屏幕则销毁精灵
        if self.rect.bottom < 0:
            print(self.rect.bottom, SCREEN_RECT.height)
            self.kill()


class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):
        # 调用父类方法，设置 image 和 speed
        super().__init__("./images/me1.png", 0)
        # 设置英雄初试位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 50
        # 创建子弹精灵组
        self.bullet_group = pygame.sprite.Group()

    def update(self):
        # 英雄在水平移动
        self.rect.x += self.speed
        # 控制英雄在屏幕内，防止英雄移除屏幕
        if self.rect.left < SCREEN_RECT.left:
            self.rect.left = SCREEN_RECT.left
        if self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        print("fire...")
        # 创建子弹精灵，一次发射三枚子弹
        for i in (0, 1, 2):
            bullet = Bullet()
            # 设置精灵的位置
            bullet.rect.bottom = self.rect.y - i * 20
            bullet.rect.centerx = self.rect.centerx
            # 将子弹精灵添加到子弹精灵组
            self.bullet_group.add(bullet)
