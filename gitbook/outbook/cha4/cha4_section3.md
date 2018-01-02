# 带参数的lambda表达式

> lambda表达式接收参数

### 1.函数

	def add(a, b):
    return a + b


### 2.使用lambda表达式实现

> 如果需要使用多次，就调用lambda表达式对象

	f = lambda a, b: a + b

	print(f(1, 2))

> **还可以简化为下面：**不创建对象，只能调用一次

	print((lambda a, b: a + b)(1, 2))

### 3.带参数lambda表达式其他例子

> **函数实现**

	def max1(a, b):
	    if a > b:
	        return a
	    else:
	        return b
	
	
	print(max1(1, 5))

> **改成lambda表达式**
	
	f2 = lambda a, b: a if a > b else b
	
	print(f2(3, 6))

> **简化lambda**

	print((lambda a, b: a if a > b else b)(5, 9))
