## 合并列表
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2  # list2在list1后面追加，合并成新列表
print(list3)

list1 += list2  # list2在list1后面追加，数据全部在list1中，不会生成新列表
print(list1)

## split() 分割长成列表
str1 = "hello world python"
str_list = str1.split(" ")  # 安装分隔符转成列表
print(str_list)  # ['hello', 'world', 'python']

## join() 字符串列表转成字符串
join_str = ",".join(str_list)  # 使用逗号将列表分割转成字符串
print(join_str)  # hello,world,python

## join只能将字符串列表转成字符串，
## 如果不是字符串列表，先转成字符串列表，如下的列表推导式
list4 = ["A", "B", "C", 100, 200]

str4 = ",".join([str(i) for i in list4])
print(str4)

## isinstance() 判断数据类型
list5 = ["A", "B", "C", 100, 200]
if isinstance(list5, list): # 如果为列表，再遍历
    for i in list4:
        print(i)

list5 = ["A", "B", "C", 100, 200]
# e = enumerate(list5)