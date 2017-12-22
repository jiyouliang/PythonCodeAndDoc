list1 = ["A", "B", "C", "D"]
## 浅拷贝：只是增加一个数据引用，任何引用修改数据，其他引用对应修改
list2 = list1
list2[1] = "BBC"
print(list1)
print(list2)

## copy() 深拷贝：拷贝新的一份数据给新的列表，和原来列表没有关系
list3 = ["A", "B", "C", "D"]
list4 = list3.copy()
list4[1] = "BBC"
print(list3)
print(list4)

print("list3 id=%d, list3[0] id=%d" % (id(list3), id(list3[0])))
print("list4 id=%d, list4[0] id=%d" % (id(list4), id(list4[0])))

print("----------------------------")
