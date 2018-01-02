# 显示器类
class Display(object):

    def show(self):
        print("显示器打开")

    def showsize(self):
        print("显示器大小")


display = Display()
# 对象设置属性
display.width = 1024
display.height = 768

display.show()
display.showsize()
print("宽高:%d, %d" % (display.width, display.height))
