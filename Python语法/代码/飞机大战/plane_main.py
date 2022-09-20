import pygame.display
import plane_sprites

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 游戏刷新率
FRAME_PER_SEC = 60
# 敌机的事件定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 子弹事件定时器常量
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化...")

        # 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建游戏时钟
        self.clock = pygame.time.Clock()
        # 创建精灵、精灵组【调用私有方法】
        self.__create_sprite()
        # 设置定时器事件 - 创建敌机 1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        # 设置定时器事件 - 创建子弹 0.3s
        pygame.time.set_timer(HERO_FIRE_EVENT, 300)

    # 开始游戏
    def start_game(self):
        print("游戏开始")

        while True:
            # 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 事件监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新/绘制精灵组
            self.__update_sprites()
            # 更新显示
            pygame.display.update()

    # 事件监听
    def __event_handler(self):
        for event in pygame.event.get():

            # 监听是否点击 'x'
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()

            # 监听定时器触发的创建敌机事件
            elif event.type == CREATE_ENEMY_EVENT:
                print("敌机起飞...")
                # 创建敌机精灵
                enemy = plane_sprites.Enemy()
                # 将敌机精灵添加到精灵组
                self.enemy_group.add(enemy)

            # 使用键盘提供的方法获取键盘按键 - 键盘元组
            keys_pressed = pygame.key.get_pressed()
            # 判断元祖中对应的按键索引值，监听是否按下方向键
            if keys_pressed[pygame.K_RIGHT]:
                self.hero.speed = 2
            elif keys_pressed[pygame.K_LEFT]:
                self.hero.speed = -2
            else:
                self.hero.speed = 0

            # 判断空格键是否按键，按下空格开火
            if keys_pressed[pygame.K_SPACE] and event.type==HERO_FIRE_EVENT:
                self.hero.fire()

    # 更新精灵组
    def __update_sprites(self):
        # 背景精灵组
        self.back_group.update()
        self.back_group.draw(self.screen)

        # 敌机精灵组
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        # 英雄精灵组
        self.hero_grop.update()
        self.hero_grop.draw(self.screen)

        # 英雄子弹精灵组
        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)

    # 精灵组与精灵的创建
    def __create_sprite(self):
        # 创建背景精灵和精灵组
        bg1 = plane_sprites.Background()
        bg2 = plane_sprites.Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄的精灵和精灵组
        self.hero = plane_sprites.Hero()
        self.hero_grop = pygame.sprite.Group(self.hero)


    # 检测碰撞
    def __check_collide(self):
        # 子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullet_group,self.enemy_group,True,True)
        # 敌机撞毁英雄
        enemies=pygame.sprite.groupcollide(self.enemy_group,self.hero_grop,True,True)
        # 判断列表是否有内容，如果有内容，说明两者发生碰撞
        if len(enemies)>0:
            # 让英雄牺牲
            self.hero.kill()
            # 结束游戏
            PlaneGame.__game_over()

    # 游戏结束 【既没有使用到类属性也没有使用到对象的属性】
    @staticmethod
    def __game_over():
        print("游戏结束...")
        pygame.quit()
        exit()


if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()
    # 开始游戏
    game.start_game()
