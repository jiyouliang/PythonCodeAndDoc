# 递归累加 1 + 2 + ... + n
def f(num):
    if num == 1:
        return num
    else:
        return num + f(num - 1)


# 调用递归函数
print(f(100)) # 5050
