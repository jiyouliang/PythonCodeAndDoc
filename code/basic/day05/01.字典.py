# 字典：key-value形式的数据类型，和java中Map类似
name_dict = {"name": "张三", "age": 18, "addr": "中国广东省深圳市"}

## 字典不能通过下标取值，通过key获取value
# print(name_dict[0])

print(name_dict["name"])

## 创建空字典
num_dict = {}
print(num_dict.fromkeys(["A", "B"], 100))  # {'A': 100, 'B': 100}

## 创建dict对象
d1 = dict(A=100, B=101, C=108)
print(d1)  # {'A': 100, 'B': 101, 'C': 108}

