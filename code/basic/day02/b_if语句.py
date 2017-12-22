"""
if语句
在Python中，bool值的True就是1，False就是0
不为0 if条件都成立
"""

age = int(input("请输入年龄"))

if age >= 18:
    print("成年人")
else:
    print('未成年人')
    print("不能上网")

if 1:
    print("不为0都成立")
    print(True + 1)# 2