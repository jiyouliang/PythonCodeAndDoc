def getsize():
    width = 320
    height = 480
    return width, height


size = getsize()
print(size)

# 拆包
width, height = getsize()
print("拆包width=%d,height=%d" % (width, height))
