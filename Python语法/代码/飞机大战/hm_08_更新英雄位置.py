import pygame

pygame.init()

# 创建游戏窗口 480 * 700
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1> 加载图像数据
bg = pygame.image.load("./images/background.png")
# 2> blit 绘制图像
screen.blit(bg, (0, 0))

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 500))

# 可以在所欲绘制工作完成后，同意调用 update 方法
# 3> update 更新屏幕显示
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 1. 定义 rect 记录飞机的初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)

# 游戏循环 -> 意味着游戏的正式开始！
while True:
    # 设置时钟刷新率为屏幕刷新率
    clock.tick(60)

    # 2. 修改飞机的位置
    hero_rect.y -= 1

    # 3. 调用 blit 方法绘制图像
    screen.blit(bg,(0,0))
    screen.blit(hero,hero_rect)

    # 4. 更新屏幕显示
    pygame.display.update()

pygame.quit()
