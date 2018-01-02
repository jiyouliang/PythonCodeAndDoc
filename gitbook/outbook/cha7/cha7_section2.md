### 文件编码
	

	# Windows默认按GBK处理中文，可以显示设置文件编码类型
	
	f = open("中文文件.txt", "r", encoding="utf-8")
	print(f.encoding)  # 显示编码