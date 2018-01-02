## 函数
def add(a, b):
    return a + b


# 调用函数
print(add(1, 2))

# -----------------------------------------------------------
## 使用lambda表达式改写
f = lambda a, b: a + b

print(f(1, 2))

# -----------------------------------------------------------
## 简写

print((lambda a, b: a + b)(1, 2))


# 带参数lambda例子2

def max1(a, b):
    if a > b:
        return a
    else:
        return b


print(max1(1, 5))

f2 = lambda a, b: a if a > b else b

print(f2(3, 6))

# 简化lambda
print((lambda a, b: a if a > b else b)(5, 9))
