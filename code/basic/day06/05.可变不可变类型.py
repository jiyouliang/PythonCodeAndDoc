# 可变类型有： 列表、字典、集合,可以修改数据为可变类型
list1 = ["A", "B", "C"]

list1[0] = "new"
print(id(list1))

# 不可变类型有： 数字、字符串、元组


age1 = 18
age2 = age1
print("age1=%d,age2=%d" % (age1, age2))
print("age1 id=%d，age2 id=%d" % (id(age1), id(age2)))
print("----------------------------")
age2 += 10
print("age1=%d,age2=%d" % (age1, age2))
print("age1 id=%d，age2 id=%d" % (id(age1), id(age2)))
