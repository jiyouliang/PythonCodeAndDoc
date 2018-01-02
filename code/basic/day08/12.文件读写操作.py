filename = "python.md"

################### 读操作 ###################
# 从文件指针位置开始，向后读取所有的内容，并返回字符串，如果有参数，参数是一个数字，表示向后读取的字节数
f = open(filename, "r", encoding='utf-8')
print(f.read())
f = open(filename, "r", encoding='utf-8')
print(f.read(3))  # 读取3个字节
f = open(filename, "r", encoding='utf-8')
print(f.readline())  # 读取一行

# 返回一个列表，列表的每个元素，都是每行的内容(会包括换行符）
f = open(filename, "r", encoding='utf-8')
print(f.readlines())
