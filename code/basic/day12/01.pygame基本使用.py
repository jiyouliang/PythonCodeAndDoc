import pygame

# 初始化pygame，让计算机硬件做准备
pygame.init()
# 创建一个窗口对象，并指定宽和高
pygame.display.set_mode([320, 480])
# 先导入磁盘的图片资源文件，返回一个图片对象
image = pygame.image.load("res/app.ico")
# 将图片对象设置为窗口图标
pygame.display.set_icon(image)
# 设置窗口标题
pygame.display.set_caption("飞机大战1.0")
input()