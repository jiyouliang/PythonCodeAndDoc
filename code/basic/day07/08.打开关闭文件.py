# 第一个参数是文件名（字符串）
# 第二个参数是操作权限（w表示写write, r表示读read）
f = open("python.md", "r")
print(f.read())

# 关闭文件，文件不存在，则创建

f1 = open("python.txt", "w")
f1.write("Hello, python.")
f1.close()
