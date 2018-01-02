import pygame

pygame.init()  # 初始化pygame，让计算机硬件做准备
# 窗体宽高
WINDOW_WIDTH = 320
WINDOW_HEIGHT = 480
# 设置窗口大小，并返回窗体对象
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
# 加载背景图片资源文件，返回图片对象
bg_image = pygame.image.load("res/img_bg_level_1.jpg")
plane_image = pygame.image.load("res/hero2.png")

# 先创建矩形对象，通过移动矩形对象，再去按矩形对象的位置绘制图片

# 一、根据图片对象，创建矩形对象，矩形对象其实就是个四个元素的元组
# 矩形对象可以记录x 和 y轴坐标（默认0,0），以及图片的宽和高。
plane_rect = plane_image.get_rect()

# 二、移动矩形对象，x 和 y 轴坐标对应发生修改。
# 矩形对象按偏移量移动，偏移量基于当前坐标位置计算
plane_rect.move_ip((WINDOW_WIDTH - plane_rect[2]) / 2, (WINDOW_HEIGHT - plane_rect[3]) / 2)

# 3、在窗口指定位置绘制图片
# 绘制背景图片对象，到窗口上的指定位置
window.blit(bg_image, (plane_rect[0], plane_rect[1]))
# window.blit(plane_image, ((WINDOW_WIDTH - plane_rect[2]) / 2, (WINDOW_HEIGHT - plane_rect[3]) / 2))

# 4、不管做了什么操作，最后刷新一下画面，重新加载。
pygame.display.update()
input()
