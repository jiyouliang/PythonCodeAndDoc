# 异常用来处理，可能会出现问题的代码
# 将代码放到 try 里面去执行，如果代码出现异常，则立刻跳转到最近的except去处理。
# try 里面尽量只写一句代码，就是可能出现问题的代码，再去针对异常。
result = 0
try:
    result = 1 / 0
    print(int("A"))
except ZeroDivisionError as e:
    print(e)
finally:
    print("不管程序有没有异常，都要执行！")
print(result)
