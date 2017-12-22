## 1.直接创建列表，生成1~10偶数列表
list1 = [2, 4, 6, 8, 10]

## 2.利用range()函数生成列表,2~11，步长2
list2 = list(range(2, 11, 2))
print(list2)

## 3.while循环生成列表
list3 = []
i = 2
while i <= 10:
    if i % 2 == 0:
        list3.append(i)
    i += 1
print(list3)

## for循环迭代 + range()
list4 = []
for i in range(2, 11):
    if i % 2 == 0:
        list4.append(i)
print(list4)

## 列表推导式（列表生成式）：创建列表/处理列表数据
list5 = [i for i in range(2, 11) if i % 2 == 0]
print("list5=%s" % list5)
"""
for i in range(2, 11):
    if i % 2 == 0:
        list5.append(i)
"""

## 生成1~11之间所有偶数的平方 列表
list6 = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print("list6=%s" % list6)
"""
list6 = []
for i in range(1, 11):
    if i % 2 == 0:
        list6.append(i ** 2)
print("list6=%s" % list6)
"""

## 生成10个 "666"列表
list7 = ["666" for _ in range(10)]  # 临时变量i不使用，可以用下划线代替
# list7 = ["666" for i in range(10)]
print("list7=%s" % list7)
"""
list7 = []
for i in range(10):
    list7.append("666")
print("list7=%s"%list7)
"""

lis = ["Demo", "Me", "Test", "Python", 8]
## 获取列表长度大于3字符串，生成新的列表
list8 = [i for i in lis if len(str(i)) > 2]
print("list8=%s" % list8)
"""
list8 = []
for i in lis:
    if len(i) > 3 :
        list8.append(i)
print("list8=%s"%list8)
"""

## 列表推导式格式：
"""

[x for x in list if...]
签名x代表返回值，
x迭代变量list
for循环后面必须是if条件
"""
list9 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = [i for i in list9 if i % 3 == 0]
print(a)
