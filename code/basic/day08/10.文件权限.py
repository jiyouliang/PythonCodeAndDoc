# 文件操作主要有三个权限：
# r - read: 读取文件， 1. 如果文件存在，则可以读取文件， 2. 如果文件不存在，则报错

# f = open("hahahah.txt", "r")

# w - write: 读文件， 1. 如果文件存在，则可以写入数据（会清空原来的数据） 2. 如果文件不存在，则新建文件

# f = open("hahahaha.txt", "w")

# a - append：追加数据，1. 如果文件存在，则在文件末尾追加数据，2.如果文件不存在，则新建文件


f = open("python.md", "a", encoding="utf-8")
f.write("新数据")
f.close()
