## lambda 表达式（匿名函数）
# １. lambda表达式是单一的一种表达式语句，没有语句块
# 2. lambda 为了编写简单的函数而设计， def 可以处理复杂的业务逻辑
# 3. lambda 默认会有返回值（不是return）
# 4. 可以没有参数，也可以有多个参数


## lambda表达式就是匿名函数

def test1():
    return 10


print(test1())  # 10

# 上面代码用lambda表达式：
f = lambda: 10
print(f())

# 简化为：

print((lambda: 10)()) # 10
