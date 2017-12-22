"""
通过input()输入的都是字符串
字符串索引和切片
"""
name = "heima"
print(name[0])  # 获取第1个位置的元素，通过下标索引取值

# 切片：取一段数据 name[start:end)
print(name[0:2])  # he

# 负数从反方向取值
print(name[-3:-1])  # im
# 设置步长
print(name[-5:-1:2])  # hi
print(name[::2])  # hia，从前往后，步长2取值hia
print(name[::-1])  # amieh，字符串翻转
