
### 1.函数

	def test1():
	    return 10
	# 调用函数
	print(test1())  # 10


### 2.使用lambda表达式实现

> 如果需要使用多次，就调用lambda表达式对象

	f = lambda: 10
	# 调用lambda表达式
	print(f())	# 10

> **还可以简化为下面：**不创建对象，只能调用一次

	print((lambda: 10)()) # 10


