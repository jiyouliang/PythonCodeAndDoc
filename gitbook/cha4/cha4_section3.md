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


