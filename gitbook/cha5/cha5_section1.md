# 函数中的可变参数

### 例子

> 代码：

	def test(*args):
	    for i in args:
	        print(i)
	
	
	test(1, "a", 3)

> 输出：

	1
	a
	3

