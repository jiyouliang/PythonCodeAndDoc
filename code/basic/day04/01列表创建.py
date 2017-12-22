## 列表格式为：中括号[]
# 创建一个列表
list1 = ["heima", 88, 13.5]
print(list1)
# print(type(list1))

# 扩展：创建系列range，并将系列转成list列表
r1 = range(5)  # (0, 1, 2, 3, 4)，创建0~4直接的系列
print(r1)

r2 = range(1, 5)  # 创建系列(1, 2, 3, 4)，这里设置起始值
print(list(r2))  # [1, 2, 3, 4]

r3 = range(0, 6, 2)
print(list(r3))  # [0, 2, 4] ，设置步长2

# 转成list
print(list(r1))  # [0, 1, 2, 3, 4]
