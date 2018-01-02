import time


f = open("test.txt", "w+", encoding="utf-8")

f.write("nihaoshijie1!\n")
f.write("nihaoshijie2!\n")
f.write("nihaoshijie3!\n")
f.write("nihaoshijie!4\n")
f.write("nihaoshijie!5\n")


f.seek(0)
print(f.read())


# 当程序执行到这里，会暂停10秒，10秒后再继续执行。
time.sleep(10)



# 将缓冲区的数据写入到磁盘文件里，并不清空缓冲区，而且也不用关闭文件。
f.flush()


# 表示将缓冲区的数据写入到磁盘文件里，并清空缓冲区（清空就是告诉操作系统，这块区域我不用了，你想给谁用就给谁用）——
# f.close()