
# lambda默认参数

> 如果不给b传参，默认d的值为30
	
	f = lambda a, b=30: a + b
	
	print(f(3))  # 33
	print(f(1, 3))  # 4



