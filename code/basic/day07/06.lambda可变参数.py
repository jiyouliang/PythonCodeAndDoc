# 函数：可变参数
def test(*args):
    for i in args:
        print(i)


test(1, "a", 3)

# 元组类型可变参数

f = lambda *args: list(args)

print(f(1, 2, 3))  # [1, 2, 3]


# 等同于下面函数

def test2(*args):
    return list(args)


print(test2(1, 2, 3))  # [1, 2, 3]

# 字典类型可变参数
# 返回字典
f = lambda **kwargs: kwargs

print(f(name="张三", age=18))  # {'name': '张三', 'age': 18}

# 返回新创建字典
f = lambda **kwargs: {key: value for key, value in kwargs.items()}
print(f(name="杨过", age=18))  # {'name': '杨过', 'age': 18}

# 返回字典value组成的列表
f = lambda **kwargs: [value for key, value in kwargs.items()]
print(f(name="杨过", age=24))  # ['杨过', 24]


# lambda表达式做为参数传递

# 函数接收的参数是函数
def func(a, b, f1):
    return f1(a, b)


print(func(10, 20, lambda a, b: a + b))
