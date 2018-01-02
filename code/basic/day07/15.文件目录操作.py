import os

# 路径：
# 绝对路径：从磁盘的根目录开始，到指定文件的完整路径
# 相对路径：相对于某个目录位置的路径, .. 表示上一级目录， . 表示当前目录

print(os.getcwd())  # 获取当前文件所在目录

# 转义字符：
# s = "hello\nworld" -> "hello\\nworld"
# s = r"helloworld"

# 记住，处理路径的时候，字符串前面加上r
####### 2. 判断某个文件/目录 是否存在，存在返回True，否则返回False
print(os.path.exists(r"python.md"))

######################################
# 删除文件：可以通过相对路径、绝对路径操作
# 如果文件不存在，报错
######################################
print(os.remove(r"temp.txt"))
# print(os.remove(r"D:\Gitbook\temp.txt")) # 绝对路径删除
# print(os.remove(r"..\temp.txt")) # 删除上一级目录下的temp.txt

######## 4. 给指定文件重命名 : os.rename(old_name, new_name)
# os.rename("test.txt", "hello.txt")

### 目录操作：
# 5. 获取指定目录下的所有文件（默认是当前目录），返回一个列表

file_name_list = os.listdir(r"C:\Users")
print(file_name_list)

####### 6. 在指定位置创建目录，创建一个目录（如果目录存在则报错）
# os.mkdir(r"C:\test")

# 7. 在指定位置创建多级目录
# os.makedirs(r"C:\test\test\test\test")

######## 8. 删除指定路径一个空目录
# os.rmdir(r"C:\test\test\test")

# 9. 删除多级目录
# os.removedirs(r"C:\test\test")
