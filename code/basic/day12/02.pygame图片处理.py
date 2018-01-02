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

# 3、在窗口指定位置绘制图片
# 绘制背景图片对象，到窗口上的指定位置
window.blit(bg_image, (0, 0))
window.blit(plane_image, ((WINDOW_WIDTH - 120) / 2, (WINDOW_HEIGHT - 78) / 2))

# 4、不管做了什么操作，最后刷新一下画面，重新加载。
pygame.display.update()
input()
