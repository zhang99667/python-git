import pygame

hero_rect=pygame.Rect(100,500,120,125)

print("英雄的原点",hero_rect.x,hero_rect.y)
print("英雄的尺寸",hero_rect.width,hero_rect.height)
# size 属性会返回矩形区域的（宽，高）元组
print("尺寸",hero_rect.size)