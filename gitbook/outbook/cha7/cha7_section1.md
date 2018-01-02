# 打开关闭文件


| read() | close() |
| :---: | :---: |
| 读取文件,并返回内容字符串 | 关闭文件表示清空缓冲区的数据，并写入到磁盘文件里（如果是写操作）|


### 1.打开文件

	# 第一个参数是文件名（字符串）
	# 第二个参数是操作权限（w表示写write, r表示读read）
	f = open("python.md", "r")
	print(f.read())

### 2.关闭文件

	# 关闭文件，文件不存在，则创建
	
	f1 = open("python.txt", "w")
	f1.write("Hello, python.")
	f1.close()